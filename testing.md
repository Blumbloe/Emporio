## Testing

### Testing User Stories
#### Testing User Goals
| Goal                                                | Result  | Comment                                                                                                              |
|-----------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------|
| Reviews   | Success | Users have the ability to leave comments on a designated part of the site. |
| Portfolio    | Success | The site contains images and links to other projects. |
| Stripe functionality | Success | The site contains stripe functionality |
| User friendly navigation and responsive design    | Success | The website is fully responsive across various devices and screen sizes.  |
| Login functionality   | Success | The site allows users to create and sign into an account. |

### Bugs

Throughout the development of the site I have been consistently checking for bugs or issues in the code some of those issues are as followed:

- The logout button was misaligned due to a styling issue so to fix this I deleted the styling and realigned the logout button using 
bootstrap margin styling.

### Manual Testing
I have manually tested each key feature on the site to ensure they have the proper functionality.

![Gif of navbar test](/emporio_project/static/documentation/navbar-test.gif)
![Gif of signup test](/emporio_project/static/documentation/signup-test.gif)
![Gif of login test](/emporio_project/static/documentation/login-test.gif)
![Gif of update test](/emporio_project/static/documentation/update-test.gif)
![Gif of delete test](/emporio_project/static/documentation/delete-test.gif)

#### Funcitonality testing

- The testing was completed on the following devices:

- Personal Computer
- Iphone 16e

The browsers used to test the site include:

- Google Chrome
- Safari
- Microsoft Edge

### Lighthouse
I have used the "lighthouse" feature within Chrome dev tools to test the sites performance, accessibility and best practices. I have checked both mobile and desktop device types.

#### Homepage 

Initial lighthouse testing diagnostics for the homepage show sufficient performance levels on both desktop and mobile.

![image of home-page lighthouse performance for desktop](/emporio_project/static/documentation/homepage-lighthouse-pc.png)

![image of home-page lighthouse performance for desktop](/emporio_project/static/documentation/homepage-lighthouse-pc.png)

#### Review page

![image of review-page lighthouse performance for desktop](/emporio_project/static/documentation/reviewpage-lighthouse-pc.png)
![image of review-page lighthouse performance for mobile](/emporio_project/static/documentation/reviewpage-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the review page show no issues on both desktop and mobile.

#### Sign-up page

![image of sign-up page lighthouse performance for desktop](/emporio_project/static/documentation/signup-lighthouse-pc.png)
![image of sign-up page lighthouse performance for mobile](/emporio_project/static/documentation/signup-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the sign up page show no issues on both desktop and mobile.

#### Login page

![image of login page lighthouse performance for desktop](/emporio_project/static/documentation/login-lighthouse-pc.png)
![image of login page lighthouse performance for mobile](/emporio_project/static/documentation/login-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the login page show no issues on both desktop and mobile.

#### Review listing page

![image of review listing page lighthouse performance for desktop](/emporio_project/static/documentation/listing-lighthouse-pc.png)
![image of review listing page lighthouse performance for mobile](/emporio_project/static/documentation/listing-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the review listing page show no issues on both desktop and mobile.

#### Update listing page

![image of update listing page lighthouse performance for desktop](/emporio_project/static/documentation/update-lighthouse-pc.png)
![image of update listing page lighthouse performance for mobile](/emporio_project/static/documentation/update-lighthouse-mobile.png)

Initial lighthouse testing diagnostics for the update listing page show minimal issues and need no changing.

#### Delete listing page

![image of delete listing page lighthouse performance for desktop](/emporio_project/static/documentation/delete-lighthouse-pc.png)
![image of delete listing page lighthouse performance for mobile](/emporio_project/static/documentation/delete-lighthouse-mobile.png)


Initial lighthouse testing diagnostics for the delete listing page show minimal issues and need no changing.

### Validation

[W3C](https://validator.w3.org/) validator has been used to check the HTML.

[W3C](https://jigsaw.w3.org/css-validator/) jigsaw has been used to check the CSS stylesheet. 

#### HTML

##### Home page

The initial check in the source for the home page came up with a few errors that were solved by unnesting the p tag, removing
a stray ul tag and replacing the h5 tags with h3 tags

![image of home page validation](/emporio_project/static/documentation/homepage-validation.png)

![image of home page post validation](/emporio_project/static/documentation/html-validation-success.png)

##### Review page

The initial check in the source for the review page came up with a warning which did not need acting upon.

![image of review page validation](/emporio_project/static/documentation/review-page-validation.png)

##### Review listing page

The initial check in the source for the review listing page came up with the same warning which also did not need acting upon.

![image of review listing page validation](/emporio_project/static/documentation/listing-validation.png)

##### Update review page

The initial check in the source for the update review  page came up with the same warning which also did not need acting upon.

![image of update review page validation](/emporio_project/static/documentation/update-validation.png)

##### Delete review page

The initial check in the source for the delete review page came up with the same warning which also did not need acting upon.

![image of delete review page validation](/emporio_project/static/documentation/delete-validation.png)

##### Sign up page

The initial check in the source for the sign up page came up with many errors however all were due to the form-with-validation
class clashing with the validator which I cannot change.

![image of sign up page validation](/emporio_project/static/documentation/signup-validation.png)

##### Login page

The initial check in the source for the sign up page also came up with many errors, all also being due to the form-with-validation
class clashing with the validator which I cannot change.

![image of login page validation](/emporio_project/static/documentation/login-validation.png)

#### CSS

The initial check for the css code came up with zero errors so no change was needed.

![image of css validation](/emporio_project/static/documentation/css-validation.png)

#### Javascript

The initial check for the javascript code came up with zero errors so no change was needed.

![image of javascript validation](/emporio_project/static/documentation/javascript-validation.png)

#### Python

##### Project

The initial check for the projects views file came up no errors.

![image of project views validation](/emporio_project/static/documentation/project-views-validation.png)

##### Users app

The initial check for the users views file came up with no errors found.

![image of users views validation](/emporio_project/static/documentation/project-views-validation.png)

##### Review app

The initial check for the users views file came up with a few errors which were solved by adding extra blank lines and
adding a newline at the end of the file

![image of review views validation](/emporio_project/static/documentation/review-views-validation.png)

The initial check for the review admin file came up with zero errors and did not need alteration.

![image of booking admin validation](/emporio_project/static/documentation/project-views-validation.png)

The initial check for the review model file came up with a singular error which was solved by adding an extra blank line

![image of review model validation](/emporio_project/static/documentation/review-model-validation.png)