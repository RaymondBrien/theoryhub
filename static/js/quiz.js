/**
 * This file contains the js code for single quiz page
 */



const quizStartButton = document.getElementById('quiz-start-btn');
const quizQuestionForm = document.getElementById('question-section');
const quizSubmitButton = document.getElementById('quiz-submit-btn');
const questionSection = document.getElementById('quiz-question-form');

// show question form when start button is clicked
quizStartButton.addEventListener('click', () => {
    console.log('from quiz.js');
    quizQuestionForm.classList.remove('d-none');
    quizStartButton.classList.add('d-none');
    questionSection.scrollIntoView({ behavior: 'smooth' });

});



// add submit functionality to the button

// check all questions have been answered (see TIm handling)
// if not, show an alert, scroll to first question not answered, and return false
// if all questions have been answered, submit the form
// ensure view shows a success message
// redirect to quiz result page
// ensure that the quiz result page is created and that the view is updated to show the result
// check DB updated as UserQuizSubmission

// quizSubmitButton.addEventListener('click', () => {
//     quizQuestionForm.setAttribute('action', 'submit_quiz/');
// });