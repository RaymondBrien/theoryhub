import unittest
import pytest
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
 
from .models import Quiz, Question, Answer
from quiz.forms import AnswerSelection
from dashboard.models import UserQuizSubmission



class TestQuizViews(TestCase):
    
    def setUp(self):
        # Crete superuser
        self.user = User.objects.create_superuser(username='testuser', password='testpassword', email='test@testemail.com')
        # Create a published quiz
        self.quiz = Quiz(title='Test Quiz', description='This is a test quiz', slug='test-quiz', status=1)
        
        # Create questions for the quiz
        self.question1 = Question(quiz_id=self.quiz, question_text='Question 1')
        
        # Create answers for the questions
        self.answer1a = Answer(question_id=self.question1, answer_option=1, answer_content='Answer 1a', correct=True)
        self.answer1b = Answer(question_id=self.question1, answer_option=2, answer_content='Answer 1b', correct=False)
        
        self.quiz.save()
        self.question1.save()
        self.answer1a.save()
        self.answer1b.save()
        
    def test_render_quiz_list_page_for_authenticated_users(self):
        # Expect page available for authenticated users
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Quiz', response.content)
    
    # Expect not available if not logged in
        self.client.logout()
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test Quiz', response.content)
    

# TODO: confirm all answers for each question are displayed.


class TestSingleQuizView(TestCase):
# TODO move all into one class so setup is consistent
# TODO replace names with first setup names for test functionality
# TODO run tests for all quiz views
    
    # def setUp(self):
    #         self.user = User.objects.create_user(username='testuser', password='testpassword')
    #         self.client = Client()
    #         self.quiz = Quiz.objects.create(title='Test Quiz', slug='test-quiz', status=1)
    #         self.question1 = Question(quiz_id=self.quiz, question_text='Question 1')
    #         self.question2 = Question(quiz_id=self.quiz, question_text='Question 2')
    #         self.answer1a = Answer(question_id=self.question1, answer_option=1, answer_content='Answer 1a', correct=True)
    #         self.answer1b = Answer(question_id=self.question1, answer_option=2, answer_content='Answer 1b', correct=False)

    #         self.quiz.save()
    #         self.question1.save()
    #         self.answer1a.save()
    #         self.answer1b.save()
    
    def test_successful_submission_redirects_to_quiz_result(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('single_quiz', kwargs={'slug': 'test-quiz'}),
                                    {'question_1': self.answer1a, 'question_2': self.answer1b})
        self.assertEqual(response.status_code, 302) # TODO test again once url quiz_result exists 
        self.assertEqual(response.url, reverse('quiz_result', kwargs={'quiz_id': self.quiz.id}))

    def test_invalid_submission_redirects_to_quiz_page(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('single_quiz', kwargs={'slug': 'test-quiz'}),
                                    {'question_1': 999, 'question_2': 999})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/single_quiz.html')

    def test_unauthenticated_user_redirects_to_login_page(self):
        self.client.logout()
        response = self.client.get(reverse('single_quiz', kwargs={'slug': 'test-quiz'}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/quiz/test-quiz/')

    def test_quiz_not_published_redirects_to_home_page(self):
        unpublished_quiz = Quiz.objects.create(title='Unpublished Quiz', slug='unpublished-quiz', status=0)
        response = self.client.get(reverse('single_quiz', kwargs={'slug': 'unpublished-quiz'}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_submission_saves_to_database(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('single_quiz', kwargs={'slug': 'test-quiz'}),
                                    {'question_1': self.answer1a, 'question_2': self.answer1b})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserQuizSubmission.objects.filter(owner=self.user, quiz=self.quiz).exists())

    
    


# TODO: confirm all answers for each question are displayed.