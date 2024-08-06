from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestAboutView(TestCase):
    """
    Test about view renders successfully
    """

    def setup(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_about_page_renders(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about_list.html')
