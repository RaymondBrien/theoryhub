import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse, resolve

#TODO import models and forms
# https://docs.djangoproject.com/en/5.0/topics/testing/advanced/
#https://djangostars.com/blog/django-pytest-testing/#:~:text=Point%20your%20Django%20settings%20to%20pytest&text=Create%20a%20file%20called%20pytest,flag%20when%20running%20the%20tests.

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