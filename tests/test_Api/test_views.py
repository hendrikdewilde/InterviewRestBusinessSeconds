import json
from unittest import TestCase

from django.test import RequestFactory

from Api.views import BusinessSecondsViewSet


class TestBusinessSecondsViewset(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_date_range_1(self):
        data = {
            'start_time': '2021-03-28T08:00:00-0200',
            'end_time': '2021-03-29T08:00:01-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 1
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 1)

    def test_list_date_range_2(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-29T08:00:01-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 1
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 1)

    def test_list_date_range_3(self):
        data = {
            'start_time': '2021-03-29T08:00:00-0200',
            'end_time': '2021-03-29T08:00:01-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 1
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 1)

    def test_list_date_range_4(self):
        data = {
            'start_time': '2021-03-29T08:00:00-0200',
            'end_time': '2021-03-29T17:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 32400
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 32400)

    def test_list_date_range_5(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-29T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 32400
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 32400)

    def test_list_date_range_6(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-30T17:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 64800
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 64800)

    def test_list_date_range_7(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-30T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 64800
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 64800)

    def test_list_date_range_8(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-03-31T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 97200
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 97200)

    def test_list_date_range_9(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-04-01T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 129600
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 129600)

    def test_list_date_range_10(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-04-02T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 162000
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 162000)

    def test_list_date_range_11(self):
        data = {
            'start_time': '2021-03-29T07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 162000
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 162000)

    def test_list_date_range_12(self):
        data = {
            'start_time': '2021-03-28T07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {
            'seconds': 162000
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json
        self.assertEqual(response.data['seconds'], 162000)

    def test_list_invalid_date_1(self):
        data = {
            'start_time': '2021-03-28 07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': 'The value is not a valid Time.The format must be YYYY-MM-DDThh:mm:ssTZD - '
                                  'Ie. 2019-01-04T16:41:24+0200'}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_invalid_date_2(self):
        data = {
            'start_time': '2021-03-28T07:00:00-0200',
            'end_time': '2021-04-03 18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': 'The value is not a valid Time.The format must be YYYY-MM-DDThh:mm:ssTZD - '
                                  'Ie. 2019-01-04T16:41:24+0200'}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_invalid_date_3(self):
        data = {
            'start_time': '2021-03-28T07:00:00-020',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': 'The value is to short.The format must be YYYY-MM-DDThh:mm:ssTZD - '
                                  'Ie. 2019-01-04T16:41:24+0200'}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_invalid_date_4(self):
        data = {
            'start_time': '2021-03-28T07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-020',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': 'The value is to short.The format must be YYYY-MM-DDThh:mm:ssTZD - '
                                  'Ie. 2019-01-04T16:41:24+0200'}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_invalid_date_5(self):
        data = {
            'start_time': '2021-03-28T07:00:00-02000',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'start_time': ['Ensure this field has no more than 24 characters.']}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_invalid_date_6(self):
        data = {
            'start_time': '2021-03-28T07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-02000',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'end_time': ['Ensure this field has no more than 24 characters.']}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_invalid_date_7(self):
        data = {
            'start_time': '2021-03-33T07:00:00-0200',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': 'The value is not a valid Time.The format must be YYYY-MM-DDThh:mm:ssTZD - '
                                  'Ie. 2019-01-04T16:41:24+0200'}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_empty_start_date(self):
        data = {
            'start_time': '',
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'start_time': ['This field may not be blank.']}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_empty_end_date(self):
        data = {
            'start_time': '2021-03-33T07:00:00-0200',
            'end_time': '',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'end_time': ['This field may not be blank.']}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_empty_start_date_and_end_date(self):
        data = {
            'start_time': '',
            'end_time': '',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': "Must include 'start_time' and 'end_time'."}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_no_start_date(self):
        data = {
            'end_time': '2021-04-03T18:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'start_time': ['This field is required.']}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_no_end_date(self):
        data = {
            'start_time': '2021-03-33T07:00:00-0200',
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'end_time': ['This field is required.']}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json

    def test_list_no_start_date_and_end_date(self):
        data = {
        }
        request = self.factory.get('/api/business_seconds', data)

        view = BusinessSecondsViewSet.as_view({'get': 'list'})

        response = view(request).render()

        expected_json = {'error': "Must include 'start_time' and 'end_time'."}

        assert response.status_code == 400
        assert json.loads(response.content) == expected_json
