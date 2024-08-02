import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from .models import QuizNote
from .forms import QuizNoteForm


# TODO user creates note
# TODO edit note (function)
# TODO delete note (function)
# TODO UserNote (class view)


class TestDashboardViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_dashboard_url_returns_200(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_view_redirects_to_login_page_if_user_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/accounts/login/?next=/dashboard/')

    
class TestQuizNotes(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.quiznote = QuizNote.objects.create(user=self.user, note='Test note')
        self.quiznote.save()
    
    def test_render_notes_page_includes_quiz_note_form(self):
        """Test when loading notes page that the user can make a
        post request to post QuizNote instance"""
        response = self.client.get(reverse('user_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['quiz_note_form'], QuizNoteForm)
        
    def test_user_note_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('user_notes'), {'note': 'This is a test note'})
        self.assertEqual(response.status_code, 200)
        in
        # self.assertTrue(QuizNote.objects.filter(note='This is a test note').exists())
        self.assertIn('Quiznote added', response.content)