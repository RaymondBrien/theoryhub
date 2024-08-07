# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


# Feature-by-Feature Testing

## Navigation

### Description
Ensures smooth transitions between pages and that all links direct users to the correct destinations.

### Testing Process
1. **Access the Main Navigation Menu**: Clicking on each link in the navigation menu to ensure it leads to the correct page (Home, QuizList, Quizzes, Dashboard).
2. **Internal Page Links**: Testing all internal page links to verify they navigate to the intended sections within the same page.
3. **Browser Navigation**: Using the browser's back and forward buttons to ensure they function properly without breaking the page.

### Results
- All navigation links direct to the correct pages or sections.
- Links work as expected and open in the appropriate tab.
- Navigation is be intuitive and consistent across different pages.

## Responsive Design

### Description
Verifies compatibility across various devices and screen sizes, ensuring the site is usable on mobile phones, tablets, and desktops.

### Testing Process
1. **Browser Resize**: Manually resizing the browser window to test how the layout adapts to different screen sizes (e.g., mobile, tablet, desktop).
2. **Device Emulators**: Using device emulators in browser developer tools to test responsiveness on specific devices (e.g., iPhone, Android phones, tablets).
3. **Physical Devices**: Testing the website on actual physical devices where possible to ensure the design is functional and visually appealing across a range of devices.

### Expected Results
- The site layout adjusts correctly and be fully functional on various screen sizes.
- Content is legible, and interactive elements should be accessible without distortion.
- No horizontal scrolling necessary on mobile devices.

### Results
- The site layout adjusts correctly is fully functional on a variety of screen sizes and devices
- Content is legible, and interactive elements should be accessible without distortion

## Quiz and Dashboard Displays

### Description
Ensure that quizzes and templates are showcased properly with accurate descriptions, images, and links.

### Testing Process
1. **Object listings**: Check that all items listed on the page have accurate descriptions, images, and any associated links.
2. **Link Functionality**: Test all project links to ensure they lead to the correct project pages or external sites.
3. **Content Alignment**: Ensure that text and images are properly aligned and formatted according to design specifications.

### Expected Results
- All quizzes, questions, answer options, quiz notes and user data tables should be displayed with correct descriptions, formatting, images, and links.

### Results
- All elements of quizzes and dashboard interactivity is formatted correctly and as expected.

## User Experience Testing:

- In usability testing, two users have accessed content using test user accounts on iphone and ipad early in the development process. Discoverability issues were raised with messages and issues were fixed.

- Accessibility testing confirmed compliance with accessibility standards screen reader compatibility, proper alt text for images and keyboard navigation using Axe Devtools accessibility testing.
![accessibility_testing](./static/images/documentation/validation/accessibility_testing.png)


## Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (this will be tested once the site has grown past MVP state):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

## Regression Testing:

After implementing fixes or updates, I ensured that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.



# Documentation and Logs:

## Code Validation

All relevant project files have been validated, for HTML, CSS, JavaScript and Python to ensure accessibility and good coding practices are met using:
- https://validator.w3.org/
- https://jigsaw.w3.org/css-validator/
- https://jshint.com/
- https://pep8ci.herokuapp.com/

| Language/File         | Image                                                                                  | Result |
|------------------|---------------------------------------------------------------------------------------------|------|
| HTML             | ![validate_html](./static/images/documentation/validation/validate_html.png)                | Yes  |
| CSS              | ![validate_css](./static/images/documentation/validation/validate_css.png)                  | Yes  |
| JS (edit_note.js)       | ![validate_edit_note_js](./static/images/documentation/validation/validate_edit_note_js.png) | Yes  |
| JS (quiz.js)       | ![validate_quiz_js](./static/images/documentation/validation/validate_quiz_js.png)           | Yes  |


## Browser Compatibility

I have run tests using the following browsers:
- [Chrome](https://www.google.com/chrome)
- [Safari](https://support.apple.com/downloads/safari)
- [Opera](https://www.opera.com/download)


I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | QuizList | Dashboard | Single Quiz | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](./static/images/documentation/browser-testing/chrome/chrome_home.png) | ![screenshot](./static/images/documentation/browser-testing/chrome/chrome_quiz_list.png) | ![screenshot](./static/images/documentation/browser-testing/chrome/chrome_dashboard.png) | ![screenshot](./static/images/documentation/browser-testing/chrome/chrome_single_quiz.png) | Works as expected |
| Safari | ![screenshot](./static/images/documentation/browser-testing/safari/home.png) | ![screenshot](./static/images/documentation/browser-testing/safari/quiz-list.png) | ![screenshot](./static/images/documentation/browser-testing/safari/dash.png) | ![screenshot](./static/images/documentation/browser-testing/safari/single.png) | Works as expected |
| Opera | ![screenshot](./static/images/documentation/browser-testing/opera/home.png) | ![screenshot](./static/images/documentation/browser-testing/opera/quiz_list.png) | ![screenshot](./static/images/documentation/browser-testing/opera/dashboard.png) | ![screenshot](./static/images/documentation/browser-testing/opera/single.png) | Works as expected |


## Responsiveness

I have tested my deployed project on multiple physical and virtual devices to check for responsiveness issues.

| Device | Home | Quiz List | Single Quiz | Dashboard | Notes Page | Results |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (iPhone 13, Opera) | ![screenshot](./static/images/documentation/device-testing/mobile/mobile-home.png) | ![screenshot](./static/images/documentation/device-testing/mobile/mobile-quiz-list.png) | ![screenshot](./static/images/documentation/device-testing/mobile/mobile-single.png) | ![screenshot](./static/images/documentation/device-testing/mobile/mobile-dashboard.png) | ![screenshot](./static/images/documentation/device-testing/mobile/mobile-notes.png) | Works as expected |
| Tablet (iPad 12", Safari) | ![screenshot](./static/images/documentation/device-testing/tablet/tablet-home.png) | ![screenshot](./static/images/documentation/device-testing/tablet/tablet-quiz-list.png) | ![screenshot](./static/images/documentation/device-testing/tablet/tablet-single.png) | ![screenshot](./static/images/documentation/device-testing/tablet/tablet-dashboard.png) | ![screenshot](./static/images/documentation/device-testing/tablet/tablet-notes.png) | Works as expected |
| Desktop (Mac, Chrome) | ![screenshot](./static/images/documentation/device-testing/desktop/desktop-home.png) | ![screenshot](./static/images/documentation/device-testing/desktop/desktop-quiz-list.png) | ![screenshot](./static/images/documentation/device-testing/desktop/desktop-single.png) | ![screenshot](./static/images/documentation/device-testing/desktop/desktop-dashboard.png) | ![screenshot](./static/images/documentation/device-testing/desktop/desktop-notes.png) | Works as expected |
| XL Monitor | ![screenshot](./static/images/documentation/device-testing/xl/xl-home.png) | ![screenshot](./static/images/documentation/device-testing/xl/xl-quiz-list.png) | ![screenshot](./static/images/documentation/device-testing/xl/xl-single.png) | ![screenshot](./static/images/documentation/device-testing/xl/xl-dashboard.png) | ![screenshot](./static/images/documentation/device-testing/xl/xl-notes.png) | Scaling starts to have minor issues |


## Lighthouse Audit

I have tested my deployed project using the Lighthouse Audit tool to check for any major issues.

I have tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](./static/images/documentation/lighthouse/mobile/lh-home-mob.png) | ![screenshot](./static/images/documentation/lighthouse/desktop/lh-home-desktop.png) | Some minor warnings |
| Quiz List | ![screenshot](./static/images/documentation/lighthouse/mobile/lh-quiz-list-mob.png) | ![screenshot](./static/images/documentation/lighthouse/desktop/lh-quiz-list-desktop.png) | Some minor warnings |
| Single Quiz | ![screenshot](./static/images/documentation/lighthouse/mobile/lh-single-mob.png) | ![screenshot](./static/images/documentation/lighthouse/desktop/lh-single-desktop.png) | Some minor warnings |
| Dashboard | ![screenshot](./static/images/documentation/lighthouse/mobile/lh-dashboard-mob.png) | ![screenshot](./static/images/documentation/lighthouse/desktop/lh-dashboard-desktop.png) | Some minor warnings. As a future feature, the dashboard will be styled to include improved contrast for user data for accessibility. |
| Notes Page | ![screenshot](./static/images/documentation/lighthouse/mobile/lh-notes-mob.png) | ![screenshot](./static/images/documentation/lighthouse/desktop/lh-notes-desktop.png) | Some minor warnings |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
|  | Quiz list page is expected to load on 'getting started' button click | Tested the feature by doing clicking button | The feature behaved as expected, and it did redirect to quiz list. | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt1.png) |
|  | Button click for 'getting started' is expected to redirect to login page if user is not logged in | Tested the feature by logging out and clicking button | Redirected to login page as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt2.png) |
|  | Global navigation should be accessible via burger icon to avoid screen overcrowding | Tested on mobile in devtools and on iphone | Burger icon for navbar appears as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt3.png) |
| Quiz List | | | | | |
|  | Button click for specific quiz expected to redirect to specific quiz | Tested the feature by clicking on buttons available in quiz list when logged in | The feature behaved as expected, and it did redirect to specific quiz | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt4.png) |
|  | Quiz url is not intended to be accessible by brute force for unauthenticated users | Tested the feature by logging out and entering a single quiz url manually | Feature redirected to sign in page as expected. | Test concluded and passed. | ![screenshot](./static/images/documentation/defensive-testing/dt5.png) |
|  | If accessing single quiz url and not logged in, user should be redirected to single quiz once logging in from the login page | Tested the feature by logging out and entering a single quiz url manually, then logging in | Feature redirected to sign in page as expected, then directly to desired quiz url | Test concluded and passed. | ![screenshot](./static/images/documentation/defensive-testing/dt6.png) |
| Single Quiz | | | | | |
|  | Upon clicking start quiz on a single quiz page, the quiz is revealed and a list of questions are presented with a submit button at the bottom. First question should scroll into view and starting information box should become smaller | Tested the feature by starting a quiz | The feature behaved as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt7.png) |
|  | Users should be able to submit quiz only when all the questions have been answered. | Attempted to submit quiz without answering all questions | The unanswered questions were highlighted and quiz submission was not successful, as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt8.png) |
|  | Users should be redirected to quiz result page once valid quiz answers are submitted, showing their score for that quiz | Tested the feature by completing a quiz | Redirect to quiz result page with score as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt9.png) |
| Dashboard | | | | | |
|  | Dashboard should only be available for authenticated users | Tested the feature by logging out and brute forcing via url to dashboard | Redirect to login page occured instead, as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt11.png) |
|  | Dashboard should only display users' own quiz score data | Tested the feature by completing a quiz, noting the result and checking the dashboard to confirm the result was showing | The dashboard listed latest quiz result as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt12.png) |
| Notes Page | | | | | |
|  | Notes page should only be available for authenticated users | Tested the feature by logging out and brute forcing url to notes page | Redirect to login occurred as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt13.png) |
|  | Notes should only display users' own notes | Tested the feature by making a new note as another user (user B). Logged back in as user A to confirm user B's note was note displaying for user A | Only user A's own notes were displayed. User B's notes were only available for user B to see. | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt14.png) |
|  | A note edit button should display note content in form, form should scroll into view and user can submit an edit successfully with a confirmation message for user feedback. The notes page should now display the edited note for that user | Tested the feature by clicking edit and making an edit to a note | The note content was editable and upon saving, the new note displayed as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt15.png) |
|  | Users should be able to delete a note, with a confirmation message | Tested the feature by deleting a note | The confirmation delete modal displayed as expected. The note was successfully deleted and no longer displayed on the user's notes page | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt16.png) |
| Additional Defenses | | | | | |
|  | Navigation bar should be listed at top (not burger icon, like for mobile users) | Tested the feature by opening the same page as both logged in and logged out | The feature displayed as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt10.png) |
|  | Clicking browser back button should not break the site, nor allow users to access content once logged out, even if previously logged in. | Tested the feature by logging out and pressing back button. | Briefly showed page before redirecting to login page. Further view authentication and a next element in the redirect was added. Tested again for all pages and now completely secure, redirecting immediately to login, then the desired page, as expected | Test concluded and passed | ![screenshot](./static/images/documentation/defensive-testing/dt17.png) |


## User Story Testing

Each user story has been tested and documented below. Any open user stories are listed in the future features milestone (milestone 8).

| User Story | Screenshot |
| --- | --- |
| User can delete a quiz note | ![screenshot](./static/images/documentation/defensive-testing/dt16.png) |
| User can edit a note | ![screenshot](./static/images/documentation/defensive-testing/dt15.png) |
| User can make notes on a notes page | ![screenshot](./static/images/documentation/defensive-testing/dt13.png) |
| User initiates media and actions | ![screenshot](./static/images/documentation/defensive-testing/dt6.png) |
| User information is pre-filled | ![screenshot](./static/images/documentation/defensive-testing/dt15.png) |
| User can view progress details | ![screenshot](./static/images/documentation/defensive-testing/dt12.png) |
| User can access progress dashboard | ![screenshot](./static/images/documentation/defensive-testing/dt12.png) |
| User can submit quiz answers | ![screenshot](./static/images/documentation/defensive-testing/dt9.png) |
| User can start a quiz | ![screenshot](./static/images/documentation/defensive-testing/dt6.png) |
| User can view quiz list | ![screenshot](./static/images/documentation/device-testing/desktop/desktop-quiz-list.PNG) |
| User can create account | ![screenshot](./static/images/documentation/create-account.png) |
| User can access sign-up form | ![screenshot](./static/images/documentation/create-account.png) |
| Admin can edit quiz answers | ![screenshot](./static/images/documentation/admin-1.png) |
| Admin can edit quiz questions | ![screenshot](./static/images/documentation/admin-1.png) |
| Admin can delete user accounts | ![screenshot](./static/images/documentation/admin-2.png) |
| Admin can view user details | ![screenshot](./static/images/documentation/admin-2.png) |
| Admin can access user accounts list |![screenshot](./static/images/documentation/admin-3.png) |
| Admin can save and publish quiz | ![screenshot](./static/images/documentation/admin-4.png) |
| Admin can add multiple-choice questions | ![screenshot](./static/images/documentation/admin-1.png) |
| Admin can set quiz title and description | ![screenshot](./static/images/documentation/admin-4.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Screenshot |
| --- | --- | --- |
| 1 passed | 16 passed | ![screenshot](documentation/tests/js-test-coverage.png) |
| x | x | repeat for all remaining tests |

#### Jest Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/RaymondBrien/theoryhub/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ARaymondBrien%2Ftheoryhub%20label%3Abug&label=bugs)](https://github.com/RaymondBrien/theoryhub/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/RaymondBrien/theoryhub/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/RaymondBrien/theoryhub/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/RaymondBrien/theoryhub/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/RaymondBrien/theoryhub/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/RaymondBrien/theoryhub)](https://github.com/RaymondBrien/theoryhub/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/RaymondBrien/theoryhub/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/RaymondBrien/theoryhub/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/RaymondBrien/theoryhub/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.


