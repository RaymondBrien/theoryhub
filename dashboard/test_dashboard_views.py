import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import QuizNote
from .forms import QuizNoteForm


# TODO test user can only see their OWN notes



class TestDashboardBaseViews(TestCase):
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
    
    # TODO
    def test_UserNotes_view_renders(self):
        response = self.client.get(reverse('user_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/notes_page.html')
    
    def test_UserNotes_redirects_to_login_if_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('user_notes'))
        self.assertRedirects(response, '/accounts/login/?next=/dashboard/notes/')

    
class TestQuizNotes(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.quiznote = QuizNote.objects.create(user=self.user, note='Test note')
        self.quiznote.save()
        
        self.user2 = User.objects.create(username='testuser2', password='testpassword')
        self.client.login(username='testuser2', password='testpassword')
        self.quiznote2 = QuizNote.objects.create(user=self.user2, note='Test note 2')
        self.quiznote2.save()
    
    def test_render_notes_page_includes_quiz_note_form(self):
        """Test when loading notes page that the user can make a
        post request to post QuizNote instance"""
        response = self.client.get(reverse('user_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['quiz_note_form'], QuizNoteForm)
        
    def test_user_note_submission(self):
        self.client.login(username='testuser', password='testpassword')
        self.quiznote = QuizNote.objects.create(user=self.user, note='Test note')
        response = self.client.get(reverse('user_notes'))
        self.assertTrue(QuizNote.objects.filter(note='Test note').exists())
    
    def test_user_note_edit(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_note', args=(self.quiznote.id,)), {'note': 'Edited note'})
        self.assertEqual(QuizNote.objects.get(id=self.quiznote.id).note, 'Edited note')
    def test_user_note_deletion(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_note', args=(self.quiznote.id,)))
        self.assertFalse(QuizNote.objects.filter(id=self.quiznote.id).exists())
    
    def test_user_cannot_see_other_users_notes(self):
        self.client.login(username='testuser', password='testpassword')
        self.quiznote = QuizNote.objects.create(user=self.user, note='New Test Note')
        self.client.logout()
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.get(reverse('user_notes'))
        self.assertNotIn(b'New Test Note', response.content)