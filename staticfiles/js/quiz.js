/* jshint esversion: 11 */

/**
 * This file contains the js code for single quiz page
 */

const quizStartButton = document.getElementById('quiz-start-btn');
const quizQuestionForm = document.getElementById('question-section');
const questionSection = document.getElementById('quiz-question-form');
const starterContent = document.getElementById('quiz-starter-content');

// show question form when start button is clicked
quizStartButton.addEventListener('click', () => {
    console.log('from quiz.js');
    quizQuestionForm.classList.remove('d-none');
    quizStartButton.classList.add('d-none');
    starterContent.classList.add('d-none');
    questionSection.scrollIntoView({ behavior: 'smooth' });

});