import logging
import datetime

from rest_framework import serializers

log = logging.getLogger(__name__)


class BusinessSecondsSerializer(serializers.Serializer):
    start_time = serializers.CharField(max_length=24)
    end_time = serializers.CharField(max_length=24)

    def validate(self, attrs):
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        if start_time in [None, ""] and end_time in [None, ""]:
            msg = {'error': "Must include 'start_time' and 'end_time'."}
            raise serializers.ValidationError(msg, code='invalid')

        return attrs

    def validate_content(self, value):
        value = str(value)
        if len(value) < 24:
            msg = {'error': "The value is to short."
                            "The format must be YYYY-MM-DDThh:mm:ssTZD - "
                            "Ie. 2019-01-04T16:41:24+0200"}
            raise serializers.ValidationError(msg, code='invalid')

        if '-' not in value and ':' not in value:
            msg = {'error': "The value is not a valid Time. "
                            "The format must be YYYY-MM-DDThh:mm:ssTZD - "
                            "Ie. 2019-01-04T16:41:24+0200"}
            raise serializers.ValidationError(msg, code='invalid')

        format = "%Y-%m-%dT%H:%M:%S%z"
        try:
            valid_time = datetime.datetime.strptime(value, format)
        except:
            msg = {'error': "The value is not a valid Time."
                            "The format must be YYYY-MM-DDThh:mm:ssTZD - "
                            "Ie. 2019-01-04T16:41:24+0200"}
            raise serializers.ValidationError(msg, code='invalid')

        return valid_time

    def count_seconds_for_start_date(self, start_time, end_time):
        # Set temp values
        temp_time_8 = start_time.replace(hour=8, minute=0, second=0)
        temp_time_17 = start_time.replace(hour=17, minute=0, second=0)

        # Count seconds for start date - 1st day
        if start_time < end_time:
            if start_time.isoweekday() < 6:
                if start_time < temp_time_8 and end_time < temp_time_8:
                    seconds = 0
                elif start_time <= temp_time_8 and end_time >= temp_time_17:
                    seconds = 9 * 60 * 60
                elif start_time < temp_time_8 and end_time <= temp_time_17:
                    temp_var = end_time - temp_time_8
                    seconds = int(temp_var.seconds)
                elif start_time >= temp_time_8 and start_time <= temp_time_17 and end_time >= temp_time_17:
                    temp_var = temp_time_17 - start_time
                    seconds = int(temp_var.seconds)
                elif start_time >= temp_time_8 and start_time <= temp_time_17 and end_time <= temp_time_17:
                    temp_var = end_time - start_time
                    seconds = int(temp_var.seconds)
                else:
                    seconds = 0
            else:
                seconds = 0
        else:
            seconds = 0
        return seconds

    def count_business_seconds(self, start_time, end_time):
        seconds = self.count_seconds_for_start_date(start_time, end_time)

        # Count full days
        day_counter = datetime.timedelta(days=1)
        start_time += day_counter
        start_time = start_time.replace(hour=8, minute=0, second=0)

        no_days = 0
        while start_time.date() < end_time.date():
            if start_time.isoweekday() < 6:
                no_days += 1
            start_time += day_counter
        else:
            seconds += no_days * 9 * 60 * 60

        seconds += self.count_seconds_for_start_date(start_time, end_time)

        return seconds
