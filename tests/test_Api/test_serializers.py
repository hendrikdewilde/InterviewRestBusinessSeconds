import datetime
from collections import OrderedDict
from unittest import TestCase

from rest_framework.exceptions import ErrorDetail

from Api.serializers import BusinessSecondsSerializer


class TestBusinessSecondsSerializer(TestCase):

    def test_serialized_date_range_1(self):
        data = {
            'start_time': '2021-03-28T08:00:00-0200',
            'end_time': '2021-03-29T08:00:01-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-28T08:00:00-0200'),
                                                         ('end_time', '2021-03-29T08:00:01-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-28 08:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-03-29 08:00:01-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 0

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 1

        assert serializer.errors == {}

    def test_serialized_date_range_2(self):
        data = {
            'start_time': '2021-03-29T08:00:00-0200',
            'end_time': '2021-03-29T08:00:01-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T08:00:00-0200'),
                                                         ('end_time', '2021-03-29T08:00:01-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 08:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-03-29 08:00:01-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 1

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 1

        assert serializer.errors == {}

    def test_serialized_date_range_3(self):
        data = {
            'start_time': '2021-03-29T08:00:00-0200',
            'end_time': '2021-03-29T17:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T08:00:00-0200'),
                                                         ('end_time', '2021-03-29T17:00:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 08:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-03-29 17:00:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        assert serializer.errors == {}

    def test_serialized_date_range_4(self):
        data = {
            'start_time': '2021-03-29T09:00:00-0200',
            'end_time': '2021-03-29T13:30:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T09:00:00-0200'),
                                                         ('end_time', '2021-03-29T13:30:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 09:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-03-29 13:30:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 16200

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 16200

        assert serializer.errors == {}

    def test_serialized_date_range_5(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-30T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T07:00:00-0200'),
                                                         ('end_time', '2021-03-30T18:00:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 07:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-03-30 18:00:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 64800

        assert serializer.errors == {}

    def test_serialized_date_range_6(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-31T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T07:00:00-0200'),
                                                         ('end_time', '2021-03-31T18:00:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 07:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-03-31 18:00:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 97200

        assert serializer.errors == {}

    def test_serialized_date_range_7(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-04-01T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T07:00:00-0200'),
                                                         ('end_time', '2021-04-01T18:00:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 07:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-04-01 18:00:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 129600

        assert serializer.errors == {}

    def test_serialized_date_range_8(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-04-02T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T07:00:00-0200'),
                                                         ('end_time', '2021-04-02T18:00:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 07:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-04-02 18:00:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 162000

        assert serializer.errors == {}

    def test_serialized_date_range_9(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is True
        assert serializer.data == data
        assert serializer.validated_data == OrderedDict([('start_time', '2021-03-29T07:00:00-0200'),
                                                         ('end_time', '2021-04-03T18:00:00-0200')])

        self.assertIsInstance(serializer.validate_content(data['start_time']), datetime.datetime)
        assert str(serializer.validate_content(data['start_time'])) == '2021-03-29 07:00:00-02:00'

        self.assertIsInstance(serializer.validate_content(data['end_time']), datetime.datetime)
        assert str(serializer.validate_content(data['end_time'])) == '2021-04-03 18:00:00-02:00'

        self.assertIsInstance(serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_seconds_for_start_date(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 32400

        self.assertIsInstance(serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])), int)
        assert serializer.count_business_seconds(
            serializer.validate_content(data['start_time']),
            serializer.validate_content(data['end_time'])) == 162000

        assert serializer.errors == {}

    def test_serialized_empty_start_date(self):
        data = {
            'start_time': '',
            'end_time': '2021-04-03T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is False
        assert serializer.data == data
        assert serializer.validated_data == {}
        assert serializer.errors == {'start_time': [ErrorDetail(string='This field may not be blank.',
                                                                code='blank')]}

    def test_serialized_empty_end_date(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is False
        assert serializer.data == data
        assert serializer.validated_data == {}
        assert serializer.errors == {'end_time': [ErrorDetail(string='This field may not be blank.',
                                                              code='blank')]}

    def test_serialized_empty_start_date_and_end_date(self):
        data = {
            'start_time': '',
            'end_time': '',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is False
        assert serializer.data == data
        assert serializer.validated_data == {}
        assert serializer.errors == {'end_time': [ErrorDetail(string='This field may not be blank.',
                                                              code='blank')],
                                     'start_time': [ErrorDetail(string='This field may not be blank.',
                                                                code='blank')]}

    def test_serialized_no_start_date(self):
        data = {
            'end_time': '2021-04-03T18:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is False
        assert serializer.data == data
        assert serializer.validated_data == {}
        assert serializer.errors == {'start_time': [ErrorDetail(string='This field is required.',
                                                                code='required')]}

    def test_serialized_no_end_date(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is False
        assert serializer.data == data
        assert serializer.validated_data == {}
        assert serializer.errors == {'end_time': [ErrorDetail(string='This field is required.',
                                                              code='required')]}

    def test_serialized_no_start_date_and_end_date(self):
        data = {
        }

        serializer = BusinessSecondsSerializer(data=data)

        assert serializer.is_valid() is False
        assert serializer.data == data
        assert serializer.validated_data == {}
        assert serializer.errors == {'end_time': [ErrorDetail(string='This field is required.',
                                                              code='required')],
                                     'start_time': [ErrorDetail(string='This field is required.',
                                                                code='required')]}
