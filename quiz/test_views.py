from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
 
from .views import QuizList, single_quiz
from .models import Quiz, Question, Answer

# TODO list success criteria for each user story here 
# test superuser can make quiz
# test superuser can make questions
# test superuser can make answers

# test there a correct answer available
# test normal user cannot see quiz list if not authenticated
# test
# test
# test



class TestQuizViews(TestCase):
    
    def setUp(self):
        # Crete superuser
        self.user = User.objects.create_superuser(username='testuser', password='testpassword', email='test@testemail.com')
        
        # Create a published quiz
        # TODO: edit once slug added to model for url functionality
        self.quiz = Quiz(title='Test Quiz', description='This is a test quiz', status=1)
        
        # Create questions for the quiz
        self.question1 = Question(quiz_id=self.quiz, text='Question 1')
        self.question2 = Question(quiz_id=self.quiz, text='Question 2')
        
        # Create answers for the questions
        self.answer1a = Answer(question_id=self.question1, answer_content='Answer 1a', correct=True)
        self.answer1b = Answer(question_id=self.question1, answer_content='Answer 1b', correct=False)
        self.answer2a = Answer(question_id=self.question2, answer_content='Answer 2a', correct=False)
        self.answer2b = Answer(question_id=self.question2, answer_content='Answer 2b', correct=False)
        
        self.quiz.save()
        self.question1.save()
        self.question2.save()
        self.answer1a.save()
        self.answer1b.save()
        self.answer2a.save()
        self.answer2b.save()
        
    # def test_render_quiz_list_page(self):    
    def test_quiz_list_view(self):
        # Log in the superuser
        self.client.login(username='testuser', password='testpassword')
        
        # Make a GET request to the quiz list view
        response = self.client.get(reverse('quiz_list'))
        
        # Check that the response status code is 200 
        self.assertEqual(response.status_code, 200)
        
        # Check that the rendered template contains the quiz list
        self.assertIn(b'Test Quiz', response.content)
    
    # def test_render_single_quiz_page(self):
    # def test_successful_answer_submission(self):