from django.test import TestCase
import pytest

# # Create your tests here.
# Admin can access quiz, set title and description, can save and publish quiz
# Admin can add multiple choice questions 
# Admin can edit quiz questions and answers

# Authenticated users can access quiz list and single quiz

    # TODO: def test_successful_answer_submission(self):
    #     """
    #     Test that a user can successfully submit an answer to a question.
    #     """
    #     quiz = Quiz.objects.create(title="Test Quiz", description="Test Description")
    #     question = Question.objects.create(quiz=quiz, text="Test Question")
    #     answer = Answer.objects.create(question=question, text="Test Answer", is_correct=True)
    #     response = self.client.post(reverse('quiz:single_quiz', args=[quiz.slug]), {'question': question.id, 'answer': answer.id})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Your answer is correct!")
    #     self.assertQuerysetEqual(Question.objects.filter(quiz=quiz), [])
    #     self.assertQuerysetEqual(Answer.objects.filter(question=question), [])
    # 
    # def test_unsuccessful_answer_submission(self):
    #     """
    #     Test that a user can submit an incorrect answer to a question.
    #     """
    #     quiz = Quiz.objects.create(title="Test Quiz", description="Test Description")
    #     question = Question.objects.create(quiz=quiz, text="Test Question")
    #     correct_answer = Answer.objects.create(question=question, text="Correct Answer", is_correct=True)
    #     incorrect_answer = Answer.objects.create(question=question, text="Incorrect Answer", is_correct=False)
    #     response = self.client.post(reverse('quiz:single_quiz', args=[quiz.slug]), {'question': question.id, 'answer': incorrect_answer.id})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Your answer is incorrect!")
    #     self.assertQuerysetEqual(Question.objects.filter(quiz=quiz), [])
    #     self.assertQuerysetEqual(Answer.objects.filter(question=question), [])
    # 
    # def test_unauthenticated_user_cannot_submit_answer(self):
    #     """
    #     Test that an unauthenticated user cannot submit an answer to a question.
    #     """
    #     quiz = Quiz.objects.create(title="Test Quiz", description="Test Description")
    #     question = Question.objects.create(quiz=quiz, text="Test Question")
    #     answer = Answer.objects.create(question=question, text="Test Answer", is_correct=True)
    #     response = self.client.post(reverse('quiz:single_quiz', args