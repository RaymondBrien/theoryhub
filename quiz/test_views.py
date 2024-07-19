from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
 
from .models import Quiz, Question, Answer
from . import views


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
        
    # def test_render_quiz_list_page(self):    
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
    
    def test_single_quiz_view_correct_questions(self):
       # TODO debug  
        # resolver = resolve('/test-quiz/')
        # self.assertEqual(resolver.func, views.single_quiz)
        
        response = self.client.get(reverse('single_quiz', args=[self.quiz.slug]))
        self.assertEqual(response.status_code, 200)
        
        # Check that the questions in the response are the ones associated with the test quiz
        # self.assertIn(b'Question 1', response.content)

        # TODO: confirm all answers for each question are displayed.

    
    

