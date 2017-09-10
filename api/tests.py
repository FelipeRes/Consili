from django.test import TestCase
from django.urls import reverse


# Para testar, basta chamar
# python manage.py test api.tests
class APITest(TestCase):

    # python manage.py dumpdata -o text_fixtures.json --exclude=contenttypes
    fixtures = ['text_fixtures.json']

    def setUp(self):
        self.token = self.get_token()

    def get_token(self, username='gildaswise', password='rootroot'):
        request_data = {'username': username, 'password': password}
        response = self.client.post(reverse('api:api-token'), data=request_data)
        self.assertEqual(response.status_code, 200)
        return 'Token %s' % response.data['token']

    # Route integrity tests

    def test_profile_list(self):
        response = self.client.get(reverse('api:profile-list'))
        self.assertEqual(response.status_code, 200)

    def test_profile_detail(self):
        response = self.client.get(reverse('api:profile-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_category_list(self):
        response = self.client.get(reverse('api:category-list'))
        self.assertEqual(response.status_code, 200)

    def test_category_detail(self):
        response = self.client.get(reverse('api:category-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_task_list(self):
        response = self.client.get(reverse('api:task-list'))
        self.assertEqual(response.status_code, 200)

    def test_task_detail(self):
        response = self.client.get(reverse('api:task-detail', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_risk_list(self):
        response = self.client.get(reverse('api:risk-list'))
        self.assertEqual(response.status_code, 401)

    def test_risk_detail(self):
        response = self.client.get(reverse('api:risk-detail', args=(1,)))
        self.assertEqual(response.status_code, 401)

    def test_purchase_list(self):
        response = self.client.get(reverse('api:purchase-list'))
        self.assertEqual(response.status_code, 401)

    def test_purchase_detail(self):
        response = self.client.get(reverse('api:purchase-detail', args=(1,)))
        self.assertEqual(response.status_code, 401)

    # Permission tests
    # HTTP_AUTHORIZATION = self.token

    def test_token(self):
        request_data = "{\n\t\"name\": \"Testing\"\n}"
        response = self.client.put(reverse('api:category-detail', args=(1,)),
                                   content_type='application/json', data=request_data)
        self.assertEqual(response.status_code, 401)
        response = self.client.put(reverse('api:category-detail', args=(1,)),
                                   content_type='application/json', data=request_data,
                                   HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)
