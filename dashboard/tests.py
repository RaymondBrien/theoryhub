import pytest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve

#TODO import models and forms

#https://djangostars.com/blog/django-pytest-testing/#:~:text=Point%20your%20Django%20settings%20to%20pytest&text=Create%20a%20file%20called%20pytest,flag%20when%20running%20the%20tests.

@pytest.mark.django_db
class TestDashboardViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_dashboard_url_returns_200(self):
        response = self.client.get(reverse(f'dashboard/{self.user.username}/'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_returns_404_if_user_does_not_exist(self):
        response = self.client.get('/dashboard/nonexistentuser/') # TODO add user auth validation in view handling so can't be brute forced
        self.assertEqual(response.status_code, 404)


class TestCommentFunctionality(TestCase):
    def test_user_can_comment_on_quiz(self):
        # TODO: Implement test logic
        pass

    def test_comment_is_validated(self):
        # TODO: Implement test logic
        pass

    def test_comments_are_shown_for_each_quiz_in_dashboard_specific_to_user_only(self):
        # TODO: Implement test logic
        pass

    def test_only_author_of_comment_can_edit_comment(self):
        # TODO: Implement test logic
        pass

    def test_only_author_of_comment_can_delete_comment(self):
        # TODO: Implement test logic
        pass

    def test_only_author_comment_can_see_their_own_comments(self):
        # TODO: Implement test logic
        pass

    def test_cannot_see_others_comments(self):
        # TODO: Implement test logic
        pass