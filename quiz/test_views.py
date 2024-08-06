from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Quiz, Question, Answer


class TestQuizListView(TestCase):

    def setUp(self):
        """Set up superuser and a published quiz"""
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email='test@testemail.com'
        )
        self.quiz = Quiz(
            title='Test Quiz',
            description='This is a test quiz',
            slug='test-quiz',
            status=1  # published
        )
        self.quiz.save()

    def test_render_quiz_list_page_for_authenticated_users(self):
        """Verify quiz list page is available for authenticated users."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Quiz', response.content)

        self.client.logout()
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test Quiz', response.content)

    def test_only_published_quizzes_are_shown(self):
        """Validate unpublished quiz not available to users"""
        private_quiz = Quiz.objects.create(
            title='Private Quiz', slug='private-quiz', status=0)
        response = self.client.get(reverse('quiz_list'))
        self.assertNotIn(b'Private Quiz', response.content)


class TestSingleQuizView(TestCase):
    def setUp(self):
        """
        Create a superuser and a published quiz with questions and answers
        """
        self.user = User.objects.create_superuser(
            username='testuser', password='testpassword')
        # quiz
        self.quiz = Quiz.objects.create(
            title='Test Quiz', slug='test-quiz', status=1)  # published
        # questions
        self.question1 = Question(
            quiz_id=self.quiz, question_text='Question 1')
        # answers
        self.answer1a = Answer(
            question_id=self.question1,
            answer_option=1,
            answer_content='Answer 1a',
            correct=True
            )
        self.answer1b = Answer(
            question_id=self.question1,
            answer_option=2,
            answer_content='Answer 1b',
            correct=False
            )

        self.answers = [self.answer1a, self.answer1b]

        self.quiz.save()
        self.question1.save()
        self.answer1a.save()
        self.answer1b.save()

    def test_renders_single_quiz_page(self):
        """
        Test that single quiz page renders correctly for authenticated users.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('single_quiz', args=['test-quiz']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Quiz', response.content)
        self.assertIn(b'Question 1', response.content)
        self.assertIn(b'Answer 1a', response.content)
        self.assertIn(b'Answer 1b', response.content)

    def test_user_can_submit_answer(self):
        """Test successful answer submission"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse(
            'single_quiz',
            kwargs={'slug': 'test-quiz'}), {'question_1': self.answer1a})
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_redirects_to_login_page(self):
        """Test unauthenticated user cannot access single quiz page"""
        self.client.logout()
        response = self.client.get(reverse(
            'single_quiz',
            kwargs={'slug': 'test-quiz'}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=/quiz/test-quiz/')
