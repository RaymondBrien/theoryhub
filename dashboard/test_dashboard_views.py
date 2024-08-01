import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse, resolve


# TODO dashboard(function)
# TODO delete note (function)
# TODO edit note (function)
# TODO UserNote (class view)


class TestDashboardViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_dashboard_url_returns_200(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_view_returns_404_if_user_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard')) # TODO add user auth validation in view handling so can't be brute forced
        self.assertEqual(response.status_code, 404)