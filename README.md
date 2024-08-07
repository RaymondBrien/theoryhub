# [THEORYHUB🎵✨](https://theoryhub-253c97b41326.herokuapp.com)
### *Your Pathway to Musical Excellence*

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub)

![screenshot](./static/images/favicon.jpg)


[Live Site](https://theoryhub-253c97b41326.herokuapp.com/)


The TheoryHub is an online platform designed to help users prepare for music theory exams, specifically for ABRSM grade 5. Built with Django, this web application provides a comprehensive set of quizzes and resources to enhance your understanding of music theory concepts essential for your musical progress and required by ABRSM for grades 6 and above performance exams.

> [!NOTE]
> BLUE: Please note that this is currently a developed MVP - check out the documentation below for more information, including the Future Features section
![here](#future-features).

## Top Features ✨

<details>
<summary>Click to expand</summary>

- **User Authentication** 🔒: Sign up for an account to access personalized features and track your progress.
- **Quiz Library** 📚: Explore a wide range of quizzes formatted just like the real newly-formatted grade 5 theory exams online for ABRSM with multiple choice questions.
- **Interactive Quizzes** ✏️: Take quizzes with multiple-choice questions and receive instant feedback on your performance.
- **Progress Tracking** 📈: Monitor your progress through a user-friendly dashboard, displaying your quiz attempts, scores, and overall performance.
- **User Dashboard** 🗂️: View a comprehensive log of all your quiz attempts and scores, along with a private space for personal notes. Track what you’ve learned, jot down areas for improvement, and plan your future study goals.
- **Admin Panel** 🔑: Administrators can create new quizzes, manage user accounts, and view quiz analytics.

</details>

## Technologies Used  ⚙️

<details>
<summary>Click to expand</summary>

- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) was used as my local IDE for development.
- [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-grey?logo=githubactions&logoColor=2088FF)](https://github.com/features/actions) is integrated into the repository workflow to ensure that code could not be pushed to the repository if the debug setting was enabled.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-grey?logo=githubpages&logoColor=222222)](https://pages.github.com) used for hosting the deployed front-end site.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management system.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Adobe Firefly](https://img.shields.io/badge/Adobe_Firefly-grey?logo=adobefirefly&logoColor=FF6F61)](https://www.adobe.com/products/firefly.html) was used to generate a favicon inspired by ink painting and the music stave shape.

- **Gunicorn** (20.1.0): A Python WSGI HTTP server for running Django applications.
- **django-allauth** (0.57.2): A Django package for handling user authentication, registration, and social account management.
- **psycopg2** (2.9.9): A PostgreSQL adapter for Python, used for interacting with PostgreSQL databases.
- **pytest** (8.3.2) & **pytest-django** (4.8.0): Testing frameworks for writing and running tests in Django applications.

</details>


## Wireframes  🗃️

In the table below are the base wireframes for the app. This was built using [Google Sites Starter Page](https://sites.google.com/new).

As the project developed, these wireframes were followed for overall structure, to ensure navigation, accessibility and discoverability were maintained at all times.
As the project continues to grow and evolve, further images will be added for quizzes.
For a list of future features, please see the [future Features](#future-features--) documentation.

<details>
<summary>Home 🏠</summary>

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| <img src="./static/wireframes/mobile/mobile_home-9.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_home-1.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/desktop/desktop-home.png" style="width:150px; height:auto;"/> |

Navigation and structure are built following these wireframes.
</details>

<details>
<summary>Signup 📝</summary>

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| <img src="./static/wireframes/mobile/mobile_signup-11.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_signup-3.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/desktop/desktop-signup.png" style="width:150px; height:auto;"/> |

Signup structure using allauth has been used, using the same basic structure outlined here.
</details>

<details>
<summary>Login 🔓 </summary>

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| <img src="./static/wireframes/mobile/mobile_login-10.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_login-2.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/desktop/desktop-login.png" style="width:150px; height:auto;"/> |

Login structure using allauth has been used, using the same basic structure outlined here.
</details>

<details>
<summary>User Dashboard 👤</summary>

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| <img src="./static/wireframes/mobile/mobile_user_dashboard-12.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_user_dashboard-4.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/desktop/desktop-user-dashboard.png" style="width:150px; height:auto;"/> |

The basic structure of features and page flow has been followed throughout development - the use of more images including a profile image will be a future feature.
</details>

<details>
<summary>Admin Dashboard 🛠️</summary>

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| <img src="./static/wireframes/mobile/mobile_admin_dash-13.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_admin_dashboard-5.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/desktop/desktop-admin-dashboard.png" style="width:150px; height:auto;"/> |

The admin dashboard functionality has been structured roughly as originally planned. As documented in issue #26, the admin dashboard will have a front end interface in the future.
</details>

<details>
<summary>Question Page 📚 </summary>

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| <img src="./static/wireframes/mobile/mobile_question-14.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_question-7.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/desktop/desktop-question.png" style="width:150px; height:auto;"/> |

The question form structure is built closely to the wireframes originally planned, most notably the use of multiple choice questions as a main feature. The use of more images for questions will appear as a future feature.
</details>

<details>
<summary>Mobile and Tablet Features 📱💻</summary>

| Mobile Misc | Tablet Misc |
|-------------|-------------|
| <img src="./static/wireframes/mobile/mobile_misc-15.jpg" style="width:150px; height:auto;"/> | <img src="./static/wireframes/tablet/tablet_misc-6.jpg" style="width:150px; height:auto;"/> |

</details>


## UX  🎨

<details>
<summary>Click to expand</summary>
### Colour Scheme

The color scheme for the application is designed to create functional and clean interface. The primary and secondary colors are used for text and highlights to ensure readability and visual appeal, though future iterations will develop this further.

Accessibility and discoverability has been a priority. Boostrap styles have at times been overridden.

- **Primary Text**: `#000000`
- **Primary Highlights**: `#E84610`
- **Secondary Text**: `#4A4A4F`
- **Secondary Highlights**: `#009FE3`

### CSS Overview

The CSS file defines the following styles:

- **Body Background**: `#F9FAFC`
- **Navigation**:
  - Active Link: `#f9f9f9` with dotted text-decoration
  - Nav Links: `#000` with a transition effect
  - Navbar Border: `#000` solid 1px
- **Select Elements**: Transparent background, no border
- **Messages**:
  - Info Alert: `#5bc0de` with light text
  - Success Alert: `#378d37` with light text
  - Warning Alert: `#f0ad4e`
  - Danger Alert: `#d9534f` with dark text
- **Copyright**: `#f9f9f9` background with `#999` text
- **Card Padding**: `1rem`
- **Divider**: `#e0e0e0` solid 1px
- **User Info List**: Padding and no list-style
- **Mark Tags**:
  - Submit: `#0d6efd` with dark text
  - Alert: `#ffc107` with black text
  - Delete: `#dc3545` with white text
- **Note Box**: `#d9534f` border with padding and centered text
- **Question Text**: `#999` solid 1px border at the bottom
- **Answer Options**: `#dc3545` text color with padding

</details>

## Database Architecture  🏗️

<details>
<summary>Click to expand</summary>

The database architecture features multiple entities managed in three main apps within the TheoryHub project.
Namely, these apps are: 'quiz', 'dashboard' and 'about'.

> [!TIP]
> For an up-to-date, interactive rendering of database architecture, please click [here](https://mermaid.live/edit#pako:eNq1VE1vozAQ_SuWpd7SKk2IWbhV6nmlbrWXFRJyYUqsgk3tsfqR8t_XNoQWkk20h_qAmJnnec_jBztaqBJoSkHfCl5p3mQyk8Stmwdlkez6wC8hkYjyMzaohawICqzhM4vwiqRQEkFin-32HX8b0HdWvN_bh0YYI5Q81d7H1u3ITaH0F4KSI5CaG8yRP4EcOf7B0KnLy4-PUCEpyah6kaAzeg7vswH_7F48vN_g0z-VE3BCeJiAdKCpZhQNkEKDey1zjhPdY9u5Wj-AKfv_38iQNbWtZiJLMIUWLbpzn9B6tGjb8qA4EImGVzAVaZCjNTM73FkweMYEQebzAMx9dEA3Vo_wtso9zWzUA-uxi84d9zjtG2le3DWcU8cDLJ9Yfg8eamo2Yl9yptZQTG0wMI7KBqW9uv0pvyi8uCC_oOY-b7aiNcfNdGDlb_1S6II2oBsuSvdTCbPLKG6hgYx6UMn1k-_ZORy3qO7fZEFT1BYWVCtbbWn6yGvjot5hw09pD2m5pOmOvtKUra7WSZIsmXuuriMWL-hbyF5H0SaKlxsWs038o1vQd6Xc_uVVvE4itmLxmrFomaxDsz-h5nt3fwHuAJLw).


<details>
<summary>Quick Summary</summary>

## Database Models

### About
- **id**: Unique identifier
- **title**: Title of the content
- **content**: Detailed text content

### UserQuizSubmission
- **id**: Unique identifier
- **user_score**: Score achieved by the user
- **last_taken**: Date when the quiz was last taken
- **Relationships**: 
  - Links to `User` (owner of the submission)
  - Links to `Quiz` (the quiz that was taken)

### QuizNote
- **id**: Unique identifier
- **note**: Content of the note
- **created_at**: Date and time the note was created
- **Relationships**: 
  - Linked to `User` (creator of the note)
  - Linked to `Quiz` (the quiz the note is associated with)

### Quiz
- **id**: Unique identifier
- **title**: Title of the quiz
- **slug**: URL-friendly identifier
- **description**: Description of the quiz
- **created_on**: Date and time the quiz was created
- **updated_on**: Date and time the quiz was last updated
- **image**: Image associated with the quiz
- **status**: Status of the quiz (published/unpublished)

### Question
- **id**: Unique identifier
- **question_text**: The text of the question
- **question_image**: Optional image for the question
- **points**: Number of points the question is worth
- **Relationships**: 
  - Linked to `Quiz` (the quiz that includes this question)

### Answer
- **id**: Unique identifier
- **answer_content**: The text of the answer
- **answer_option**: The option number for the answer
- **correct**: Indicator if the answer is correct
- **Relationships**: 
  - Linked to `Question` (the question this answer belongs to)

</details>

The 'quiz' and 'dashboard' apps are used for interactive functionality between the database and the user, and the user is established in the database using the standard the Django user model for scalability and compatibility, as you will see documented in the appendix.

N.B.
As the project has developed, the database architecture has been refined to improve performance and functionality for additional features. The additional features that were not present in the original design are:
1. The 'about' model, used in the about app for handling dynamic updates about the project to inject into a welcome section within the project, acting as a scalable landing page with easy modularity.
2. The 'QuizNote' model, used to enable users to interact with the database with full CRUD functionality, making their own personal notes within their own dashboard.
3. A change of name to the UserScore model, now called UserQuizSubmission for improved semantics.

The changes are documented visually in the appendix
([available here](#appendix)).

This modular approach ensures that each model handles its data in a self-contained manner, ensuring future scalability and ease of custom database queries where necessary for future development.

The application's database design follows a modular approach, with the primary focus and largest amount of data handling for two main features: the dashboard and the quizzes. This architecture ensures a clear separation of concerns, allowing each entity to handle its respective data in a self-contained and scalable manner.

The [ERD](#appendix) illustrates the relationships between these entities and their associated models.


### Dashboard Features

The dashboard holds around 60% of the data handling, enabling the full CRUD functionality of the QuizNote feature for users to create, read, update and delete instances as they wish, personal to them within their own user dashboard. Key models include:

- **QuizNote**: Represents a user note.
- **UserQuizSubmission**: Stores data on a user's score for a given quiz, and when they submitted it. Multiple quiz attempts are allowed.

### Quiz Entity

The Quiz entity is comprised of models dedicated to managing quizzes, questions, and answer options. Key models include:

- **Quiz**: Represents a collection of questions.
- **Question**: Stores the question text and associated metadata.
- **Answer**: Holds the answer options for each question, including the correct answer.

This separation of concerns facilitates future scalability, enabling features like dynamic quiz generation for personalised user progression plans based on topics needing most improvement, question randomization, and advanced analytics for question performance and difficulty analysis.

</details>


## Future Features  🎉

<details>
<summary>Click to expand</summary>

- **User Roles**: Map users to specific roles to host integrated forums and discussions on different topics for improved social connection.
- **UI Personalisation**: Personalised user interface features including profile photos, fonts and screen color filters for a more dyslexia-friendly service.
- **Gamification Elements**: User models include further metadata to enable leaderboards or achievement badges and timed competitions for various ages groups.
- **Curriculum Integration**: Mapping quizzes to specific ABRSM music theory curricula or exam requirements, enabling targeted preparation and progress tracking.
- **Social Features**: Introducing study groups, forums, or collaborative learning features to foster community engagement and knowledge sharing.
- **Adaptive Learning**: Implementing algorithms for personalized question recommendations based on user performance and learning patterns.
- **Multimedia Support**: Incorporating multimedia elements, such as audio clips, more images and sheet music, to enhance the learning experience.

</details>

## Getting Started ☑️

<details>
<summary>Open first steps 🚀</summary>

To get a local copy of the project up and running, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/RaymondBrien/theoryhub
   ```

2. Navigate to the project directory:
   ```
   cd theoryhub
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Open your web browser and visit `http://localhost:8000` to access TheoryHub.

</details>

<details>
<summary>Open contributing 🤝</summary>

We welcome contributions from the community! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

### Suggestions and Future Enhancements 💡

We are constantly striving to improve the Music Theory Practice Hub and make it more engaging and effective for users. If you have any suggestions for additional features or scalable enhancements, please feel free to submit them as issues in the repository. We welcome collaboration and ideas from the community to shape the future of this platform.

Some potential areas for future development include:

- Gamification elements (e.g., badges, leaderboards) to increase user engagement and motivation.
- Integration with specific music theory curricula or exam requirements.
- Social features (e.g., study groups, forums) to foster collaboration and knowledge sharing among users.

If you have expertise or interest in any of these areas, we encourage you to get involved and contribute to the project's growth.

</details>



<details>
<summary>Open acknowledgments 🙏</summary>

Feel free to explore the Music Theory Practice Hub and enhance your music theory skills! If you have any questions, suggestions, or ideas for future enhancements, please don't hesitate to reach out or submit an issue. Happy practicing! 🎶

</details>

## Agile Development Process 👟
<details>
<summary>Click to expand</summary>
### GitHub Projects

[GitHub Projects](https://github.com/users/RaymondBrien/projects/3) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the Kanban board and GANTT charts.

![screenshot](./static/images/agile.png)

### GitHub Issues

[GitHub Issues](https://github.com/RaymondBrien/theoryhub/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories, define milestone deadlines, milestone iterations and arrange user stories by priority level on a weekly basis.

<details>
<summary>List of User Stories</summary>
- As a **User**, I want to **delete a quiz note** for **keeping workspace tidy, or for completed reminders**.

- As a **user**, I want to **edit** for **updating quiz notes or fixing typos**.

- As an **admin**, I want to **create quizzes** for **quicker quiz creation**.

- As a **user**, I want to **write a note in my dashboard notes page** for **making notes on what to revise over next time**.

- As a **User**, I want to **update my account information or delete my account** for **account security**.

- As an **Admin**, I want to **create a blog post** for **users to read and improve their theory knowledge**.

- As a user, I want to initiate any media or actions myself so that I have a positive user experience.

- As a user, I want my information to be pre-filled so that I don't have to enter it multiple times.

- As a user, I want to be able to view detailed progress information so that I can analyze my performance and identify areas for improvement.

- As a user, I want to be able to access a dashboard showing my progress so that I can track my performance and identify areas for improvement.

- As a user, I want to be able to view my score for a completed specific quiz so that I can identify areas for improvement.

- As a user, I want to be able to submit my answers for a quiz so that I can complete the quiz.

- As a user, I want to be able to start a quiz so that I can answer the questions.

- As a user, I want to be able to view a list of available quizzes so that I can select and take a quiz.

- As a user, I want to be able to create a new account so that I can access the quizzes.

- As a user, I want to be able to access a sign-up form so that I can create a new account.

- As an admin, I want to be able to edit the answer options for questions in a quiz so that I can correct or update the content.

- As an admin, I want to be able to edit existing questions in a quiz so that I can correct or update the content.

- As an admin, I want to be able to view detailed analytics for a specific quiz so that I can analyze user performance.

- As an admin, I want to be able to access a dashboard showing analytics for each quiz so that I can understand user performance and identify areas for improvement.

- As an admin, I want to be able to delete user accounts so that I can remove inactive or non-compliant users.

- As an admin, I want to be able to view details of a user account so that I can monitor activity and ensure compliance.

- As an admin, I want to be able to access a list of all registered user accounts so that I can view and manage them.

- As an admin, I want to be able to save and publish a quiz so that users can access and take it.

- As an admin, I want to be able to add multiple-choice questions to a quiz so that users can answer them.

- As an admin, I want to be able to set the title and description of a quiz so that users can easily identify the quiz.

- As an admin, I want to be able to access a quiz creation interface so that I can create new quizzes.

For feature screenshots, please see the user story testing documentation [here](TESTING.md).


</details>

Open Issues are now all future features milestone issues or won't have features.
- [Open Issues](https://github.com/RaymondBrien/theoryhub/issues) [![GitHub issues](https://img.shields.io/github/issues/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub/issues)


- [Closed Issues](https://github.com/RaymondBrien/theoryhub/issues?q=is%3Aissue+is%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub/issues?q=is%3Aissue+is%3Aclosed)


### MoSCoW Prioritization

I have decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration - these have been added to the future features milestone.

</details>

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://theoryhub-253c97b41326.herokuapp.com).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]  
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method
> if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

<details>
<summary>Click to expand</summary>
This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/RaymondBrien/theoryhub) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/RaymondBrien/theoryhub.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RaymondBrien/theoryhub)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/RaymondBrien/theoryhub)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

Any differences between local and deployed versions are minimal and purely due to screen resolution.

</details>


## Credits

### Content


| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |
| [Django Forms Documentation](https://docs.djangoproject.com/en/4.2/ref/forms/) | forms | Django documentation for handling forms with validation efficiently |

| [TravelTimN GitHub](https://github.com/TravelTimN/) | Quiz models and project structure | project mentor |

# Appendix

<details>
<summary>
Entity Relationship Diagram (ERD)

*[(Back to Database Architecture Section)](#database-architecture)*

</summary>
ORIGINAL ERD:
<img src="./static/images/erd_models-v2.png">

UPDATED ERD:

```mermaid
erDiagram

    About {
        int id
        string title
        text content
    }

    UserQuizSubmission {
        int id
        int user_score
        date last_taken
    }
    UserQuizSubmission }o--|| User : "owner"
    UserQuizSubmission }o--|| Quiz : "quiz"

    QuizNote {
        int id
        text note
        datetime created_at
    }
    QuizNote }o--|| User : "user"

    Quiz {
        int id
        string title
        string slug
        text description
        datetime created_on
        datetime updated_on
        string image
        int status
    }

    Question {
        int id
        text question_text
        string question_image
        int points
    }
    Question }o--|| Quiz : "quiz_id"

    Answer {
        int id
        text answer_content
        int answer_option
        int correct
    }
    Answer }o--|| Question : "question_id"

    %% Relationships
    QuizNote }o--|| Quiz : "quiz"
    UserQuizSubmission }o--|| User : "owner"
    UserQuizSubmission }o--|| Quiz : "quiz"
```

</details>

[Back to Top](#your-pathway-to-musical-excellence)