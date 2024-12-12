# Task Buddies

https://github.com/Loudotcom/ci-final-project

A simple and fun to-do list website.

**Live website**

The live link, hosted on Heroku:  [Task_Buddies](https://final-code-institute-project-76c9d9aad788.herokuapp.com/)

![Am I Responsive](/media/Pastedimage20241211213954.png)

## Purpose of the project

Task Buddies is a to-do list website where users can create their own personal, customisable list of tasks. The purpose was to help motivate and support anyone who struggles with traditional to-do lists, and make the process of completing tasks more enjoyable. This full-stack project uses Django and Bootstrap frameworks.

***

# UX - User Experience

## User Stories:

 Admin
 
- As a Site Admin I can delete user accounts so that I can remove users whose content is against our content guidelines.

User   

- As a Site User I can register for the site so that I can sign in and create to-do lists.

- As a Site User I can sign in so that I can access my to-do list at any time
   
 - As a Site User I can create, read, update and delete tasks so that I can keep my to-do list updated.
 
 - As a Site User I can add a status to individual tasks so that I know which tasks are completed, which have been started and which are still to start.

 - As a Site User I can add notes to my tasks so that I remember more specific information about what I need to do.
   
## Design

Ultimately, I plan for users to be able to personalise their task list pages, including choosing a logo colour, page colour theme and a mascot.  I took one example and chose to create a tortoise sprite, a symbol of slow and steady progress, thumb up and holding a flag showing that he is rooting for the user and celebrating their wins with them. I chose a vibrant purple for the logo and footer to go with the green and brown of this mascot.

## Wireframes

Desktop

Desktop - Home/Sign In Page

![[Pasted image 20241212013137.png]]

Desktop - Sign Up Page

![[Pasted image 20241212013355.png]]

Desktop - Task List 

![[Pasted image 20241212014124.png]]
Desktop - Edit Task Page 

![[Pasted image 20241212014339.png]]
Desktop - Delete Task Page

![[Pasted image 20241212014519.png]]

Desktop - Sign Out Page

![[Pasted image 20241212014647.png]]

## Final View

### Desktop View:

Desktop - Home/Sign In Page

![Desktop Home View](/media/DesktopHomeView.png)

Desktop - Sign Up Page

![Desktop Sign In Page](/media/Pastedimage20241211203957.png)

Desktop - Task List 

![Desktop Task List](/media/Pastedimage20241211204430.png)

Desktop - Edit Task Page

![Desktop Edit Page](/media/Pastedimage20241211204459.png)

Desktop - Delete Task Page

![Desktop Delete Page](/media/Pastedimage20241211204528.png)

Desktop - Sign Out Page

![Desktop Sign Out](/media/Pastedimage20241211204753.png)

Tablet view:

Tablet - Home/Sign In Page

![Tablet Sign In Page](/media/Pastedimage20241211205620.png)

Tablet - Sign Up Page

![Tablet Sign Up](/media/Pastedimage20241211205637.png)

Tablet - Task List 

![Tablet Task List](/media/Pastedimage20241211220118.png)

Tablet - Edit Task Page

![Tablet Edit Task](/media/Pastedimage20241211220055.png)

Tablet - Delete Task Page

![Tablet Delete Task](/media/Pastedimage20241211220147.png)


Tablet - Sign Out Page

![Tablet Sign Out](/media/Pastedimage20241211205543.png)

**Mobile View (Medium - 375px):**

Mobile - Home/Sign In Page

![[MobileHome-ezgif.com-video-to-gif-converter.mp4]]

**Mobile View (Medium - 375px):**

Mobile - Home/Sign In Page

![[MobileHome-ezgif.com-video-to-gif-converter.mp4]]

Mobile - Sign Up Page

![[MobileSignUp-ezgif.com-video-to-gif-converter.mp4]]

Mobile - Task List 

![[MobileTaskList-ezgif.com-video-to-gif-converter.mp4]]

Mobile - Edit Task Page

![Mobile Sign Out](/media/Pastedimage20241211215609.png)

Mobile - Delete Task Page

![Mobile Delete Task](/media/Pastedimage20241211215634.png)

Mobile - Sign Out Page

[Mobile Sign Out](/media/Pastedimage20241211215717.png)

***

# Features

## Existing Features

**Success/Error Message**

- Users can see when they have successfully signed out and edited tasks from their task list from a banner message at the top of the screen. Otherwise, an error message is displayed.

![Feature1](/media/Pastedimage202412121140131.png)

![Feature2](/media/Pastedimage20241212113913.png)

![Feature3](/media/Pastedimage20241212113023.png)

***

**The Logo**

- I designed this logo with the help of [Logo.com](https://www.logo.com/)'s logo generator. I liked the informal but easy-to-read font and customised it by changing the colour to a vibrant purple and adding the paw print over the 'i' of 'buddies' to reference the multiple animal mascots to be added in future iterations. I plan for the colour of the logo to be customisable by the user.

![Logo](/media/Pastedimage20241212091126.png)

***

**Navbar**

- I kept the navbar simple, with a clean white background and the links to other pages in a standard grey font.

![Navbar](/media/Pastedimage20241212091144.png)

***

**Authorisation**

- Site users can sign up, sign in, and sign out, keeping their task lists saved for future visits.

![Auth1](/media/Pastedimage20241212092300.png)
![Auth2](/media/Pastedimage20241212092328.png)

***

**Mascot**

![Mascot](/media/Pastedimage20241212091324.png)

- One of my main features/elements, and that sets my to-do list apart, is the addition of an animal mascot. I plan to introduce many animal characters that users can choose from, they could interact in some way with the user, through animation or with supportive messages.

***

**Footer

- The footer section currently has copyright information, and there are options to easily add additional links as the site grows. The colour of the footer matches the logo color to keep consistency and frame the site.

![Footer](/media/Pastedimage20241212091341.png)

***

**Notes**

- The ability to add notes to a task would be a useful next feature, as at the moment users are restricted to the task name word limit.

**Message/Media Upon Completion**

- A valuable feature for the next iteration would be to add more of a celebration when a user completes (i.e. deletes) a task. Currently, there is a simple encouraging message above the buttons on the Delete Task page but there are many options for media or messages upon completion. As with the colour scheme and mascot, I would like this to eventually be customisable by each user individually so they make a task page that looks and interacts with them in a way that is uniquely theirs.

***

# Database Schema - Entity Relationship Diagram

![ERD](/media/Pastedimage20241128112655.png)

I created the entity relationship diagram (ERD) above during the planning stage of my project. As I elected to keep to the minimum viable product and I wanted to keep my site simple from a usability point of view, I chose to use one entity with few basic attributes. 

***

# Agile Methodologies - Project Management

Using [Github Projects](https://github.com/users/Loudotcom/projects/4/views/1), I created a kanban board with 6 main user stories. 

I used the MoSCoW prioritisation method to establish which features were most crucial to the project to create a minimal viable product (must-haves), which would add value to the project if time allowed (should-haves), desirable but not vital features (could-haves), and those features to be considered for future iterations (won't-haves).

**The Must-Haves**

Those related to CRUD functionality, as a project requirement, were my must-have features, as well as the ability for users to sign in and out of the site:


![[Pasted image 20241211124351.png]]

**The Should-Haves**

The should-haves were features I planned to include in my final submission before I started writing the code.  A combination of style-choice and time-constraint meant I decided not to include them. However, these options are included in the model (see 'Status' and 'Notes' in the ERD above) and therefore can be easily implemented in the next iteration:

![Todo](/media/Pastedimage20241211124407.png)

**The Could-Haves and The Won't-Haves**

The could-have and won't-have user stories were related to the additional features below for possible future iterations. I had many creative ideas on how this MVP could be built upon to create a dynamic and appealing site.

## Features Left to Implement

In the next iteration, I would work to implement the Task Notes user story. I am not sure whether the Task Status user story would be the most important considering the target audience. I think the celebration image/video/audio or the customisation of profile/mascots/colour-themes would add more value. 

- Add a deadline to tasks 
- Categorise tasks
- Image/video/audio once tasks marked as 'completed'
- Add images to tasks
- Create a profile
- Share lists with other users
- Add tasks to online calendar 

***

# Deployment

## Connecting to GitHub 

Following the below steps and [Code Institute's Github Template](https://github.com/Code-Institute-Org/ci-full-template), I created a repository which was editable locally in Gitpod and stored in a remote repository in my Github account.

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new, relevant repository name and click '**Create repository'.
5. To create a new workspace in Gitpod, click the green '**Open**' button and as long as Gitpod is an extension in your browser, it will open in Gitpod.

## Django Project Setup

To set up my Django project, I followed the following [Setup & Deployment Guidebook 2024](https://docs.google.com/document/d/1-r9y0sGzJf7iusWypPUd2Qrf9ODoslHfmzpAq0G2OU0/edit?tab=t.0#heading=h.qwn8zjty0594)

## Heroku deployment

To start the deployment process, please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user, this may require two-factor authentication.
    
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
    
3. Enter an app name and choose your region. Click '**Create App**'.
    
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your:
    
    - **CLOUDINARY_URL** : **cloudinary://....**
    - **DATABASE_URL** : **postgres://...**
    - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
    - **SECRET_KEY** and value
    
5. Add the Heroku URL for your live site into **ALLOWED_HOSTS** in your projects **settings.py file**.
    
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
    
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
    
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
    
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
    
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC** may be removed from the Config Vars once you have saved and pushed any image and/or CSS code within your project.

***

# Testing

## Validator Testing

### HTML

I used [HTML W3C Validator](https://validator.w3.org/) to validate my HTML files. 
As each page included Django's Template Language (DTL), which was throwing errors, I used the 'view page source' option after right-clicking the site in the browser, and copying the code into the 'validate by input' option.


---

### CSS

I used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate my style.css file.


![[Pasted image 20241212070054.png]]

![[Pasted image 20241212070117.png]]

---

### JavaScript

All JavaScript code included in my project was imported and I have not made any additional changes, therefore it has not been validated.

---

### Python Validation

I used [CI Python Linter](https://pep8ci.herokuapp.com/#) to validate the Python code in files that I created or edited. 

I validated the following files, which all returned 'All clear, no errors found':
admin.py
forms.py
models.py
urls.py
views.py

Please see below for a screenshot of the results of my views.py file. 

![Python](/media/Pastedimage20241212000540.png)

---

### Lighthouse Report

I carried out a test using the Lighthouse Chrome extension using incognito mode and screenshots of the resulting reports for mobile and desktop are below. Accessibility was an important factor in creating this website, so I am extremely pleased with this result.

![[Pasted image 20241211222453.png]]

![[Pasted image 20241211222511.png]]

### Wave Accessibility Evaluation

To test for accessibility specifically, I used the Wave web accessibility evaluation tool. I have screenshot the result below. Again, I am pleased the site's accessibility standard was deemed satisfactory.

![Wave](/media/Pastedimage20241211222815.png)

---

## Manual Testing

All features were tested on different device sizes (Mobile, Tablet and Desktop) using the responsive mode in Google Chrome's developer tools and checked in the Microsoft Edge browser. Please see gifs below for manual test examples for a desktop-size screen on Google Chrome. 

These same tests were carried out for mobile and tablet screen sizes. 

A bug was found when testing the mobile screen size; on the sign up page for smaller and medium-sized mobile phone screens the sign up button was obscured by the footer. This was fixed by adding media queries to my style.css file.

**Desktop** -  Sign Up

Users can create an account with a username and password. 

Result: Pass


![[DesktopRegister-ezgif.com-video-to-gif-converter.mp4]]

***

**Desktop** - Create Task

Users can create a task which then appears in their task list.

Result: Pass

![[DesktopAddTask-ezgif.com-video-to-gif-converter.mp4]]

***

**Desktop** - Edit Task

Users can edit the tasks in their task list

Result: Pass

![[DesktopEditTask-ezgif.com-video-to-gif-converter.mp4]]

***


**Desktop** - Delete Task

Users can delete the tasks in their task list.

Result: Pass

![[DesktopDeleteTask-ezgif.com-video-to-gif-converter.mp4]]

***


**Desktop** - Sign Out

Users can sign out of their account.

Result: Pass

![[DesktopSignOut-ezgif.com-video-to-gif-converter.mp4]]

***


**Desktop** - Sign in

Users can sign in to their account.

Result: Pass

![[DesktopSignIn-ezgif.com-video-to-gif-converter.mp4]]

***


**Desktop** - Return to Task List 

When signed in and on the edit or delete pages, users can easily return to their task list.

Result: Pass

![[DesktopReturntoTaskList-ezgif.com-video-to-gif-converter.mp4]]


---

## Credits


- I used a previous successful Code Institute to-do project called [Task Genie]([https://todo-genie-65081f96d293.herokuapp.com/accounts/login/?next=/](https://todo-genie-65081f96d293.herokuapp.com/accounts/login/?next=/)) by [Tedbot2000]([https://github.com/Code-Institute-Submissions/todo-genie-01](https://github.com/Code-Institute-Submissions/todo-genie-01)) as inspiration

 - In preparation for my project I coded along with two walkthrough Django to-do list projects on YouTube which I used to help me create the first draft of my code:

	 - YouTube Channel: Dennis Ivy 
		 [https://www.youtube.com/watch?v=llbtoQTt4qw](https://www.youtube.com/watch?v=llbtoQTt4qw)
		 [https://github.com/divanov11/Django-To-Do-list-with-user-authentication](https://github.com/divanov11/Django-To-Do-list-with-user-authentication) 
		
	- YouTube Channel: Cloud With Django 
		 [https://www.youtube.com/watch?v=sHieKUtwQcM](https://www.youtube.com/watch?v=sHieKUtwQcM)
		 [https://github.com/cloud-with-django/Django-task-list-app-Project-3-YT](https://github.com/cloud-with-django/Django-task-list-app-Project-3-YT)


- For some practical steps in Django I used the Codestar Blog project from [Code Institute](https://learn.codeinstitute.net/) as a guide

- I used the AI tool [Perplexity](https://www.perplexity.ai/) throughout production for debugging

- I used the ReadMe by [Hata-na-tata](https://github.com/Anka-S/hata-na-tata/) by [Anka-S](https://github.com/Anka-S) as inspiration and a template for this document

---

## Content

- I created the Task Buddies logo using [logo.com](https://logo.com/) and the favicon was automatically generated from my finalised logo by the site

- I created the tortoise sprite using the AI image generator [Microsoft Create](https://create.microsoft.com/en-us/features/ai-image-generator) 

- The CDN framework used for ready-made styling was [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/download/)

- [Balsamiq](https://balsamiq.com/) was used for wireframe

- [Perplexity](https://www.perplexity.ai/) was used for writing the text in the Home/Sign In page


---