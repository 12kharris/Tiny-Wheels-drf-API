

# Tiny Wheels Django Rest Framework API
Tiny wheels is a website where users can view posts and diecast vehicle collections of other users. The site is aimed at diecast vehicle enthusiasts who wish to share their enjoyment of the hobby with others. This half of the project is the backend API of the app. Its purpose is to handle all of the CRUD (create, read, update, delete) functionality for data. It acts as an interface between the front-end website and the database store of all of the app data.

The live API can be found at https://tiny-wheels-drf-api-4afe6c445f29.herokuapp.com/

## Technologies Used
The following technologies were used and their install commands listed next to them
- Django - For development framework: pip3 install django==3.2.4
- Django Cloudinary Storage - For connecting API to cloudinary for image storage: pip install django-cloudinary-storage==0.3.0
- Pillow - For allowing images to be stored in the database: pip install Pillow
- Django Rest Framework - Used to create the views and JSON serializers for returning data and handling requests: pip install djangorestframework==3.12.4
- Django Filter - Enables filtering functionality in requests: pip install django-filter==2.4.0
- Django Allauth - Hanldes user authentication: pip install dj-rest-auth==2.1.9, pip install django-allauth==0.50.0
- Django JWT - For creation and passing of web tokens between the client and this app for continuous logged in status: pip install djangorestframework-simplejwt==5.3.1
- psycopg2 - Handles connecting to postgresql database: pip3 install dj_database_url==0.5.0 psycopg2
- Django CORS Headers - Handles restricting API requests to specified urls


## Languages Used
The following programming languages were used for this project
- Python3 - For simple database querying, view routing and view generation. Python is the language used by the Django framework
- PSQL - For complex database querying

## Acknowledgements
All code which has been adapted from online sources has been commented with a link to the original source in each file.
- Using queries in the filter for a Count function - https://stackoverflow.com/questions/11418522/django-how-to-annotate-queryset-with-count-of-filtered-foreignkey-field
- Implementing check constraints in django models - https://medium.com/@ishakokutan/django-constraints-fa81d09cfa94
- Instructions for setting up the django rest framework logic and installing all necessary packages were provided by Code Institute in their Django REST Framework Module

## Planning
Before development, planning of the look of the application and the structure of its database was done to streamline development.
Below is an entity relationship diagram for how the database structure would look.

![ERD](https://res.cloudinary.com/da2ant1dk/image/upload/v1728850583/media/images/o4g7azdl4cehiinule6l.png)

### User Stories
Below is a link to the GitHub project board with all of the development tasks for the API section of this project. Each task is linked to a relevant sprint. These tasks were orignally created on Azure DevOps but moved over to GitHub projects midway through development.

https://github.com/users/12kharris/projects/3
https://dev.azure.com/kurtharris1541/Tiny%20Wheels/_workitems/recentlyupdated



## Models
Below are the django models used in this project and their function

### Profile
The Profile model houses all information for a user beyond what is stored in the User model by django allauth. It is automatically created when a new user is created. 

### Post
The Post model is used for holding all data regarding a post which has been made by a user. It has links to an owning profile, the Like model and the Comment model.

### Tag
The Tag model allows a user to tag a post they have made to categorise a post. A user will be able to filter on the available tags on the front end

### Likedislike
The Likedislike model allows users to like or dislike a post. It determines the difference between a like and a dislike with the IsLike field. A user can only have a like or a dislike on a post, not both.

### Follower
This model provides the following functionality of the app. It holds the profile of the user who initiated the follow and the profile of the user they are now following

### Collection
The collection is automatically created when a new profile is created. Each user has a collection where they can upload their various model vehicles for others to see

### CollectionItem
This model holds the data for each individual item in a collection. It holds the Series of the diecast model and the quantity of that item

### Series
The Series model houses the different series which have appeared for each Brand of diecast vehicle

### Brand
The Brand model currently houses 2 vehicle brands but will be expanded in the future to accommodate more brands. It currently contains just Hot Wheels and Matchbox

## Endpoints
This section outlines the various endpoints for the api and what they return

### /profiles/
Returns an array of all profiles registered with the app. 

### /profiles/<int: id>/
Returns a profile object with the specified id. Accepts PUT requests to update the Name and ProfileImage properties

### /brands/
Returns an array of all brands

### /series/
Returns an array of all series

### /collections/
Returns an array of all collection objects for all users

### /collections/<int: id>/
Returns an array of all items in the specified collection

### /collections/item/<int: id>/
Returns a CollectionItem object with the specified id. Allows PUT and DELETE requests if the user owns the item

### /collections/items/
Returns only the collection items for the collection the logged in user owns. Allows POST requests to add a collection item

### /comments/
Returns an array of all comments. Accepts POST requests to add a new comment.

### /comments/<int: id>/
Returns details of the specified comment. Accepts PUT and DELETE requests if the user owns the comment

### /followers/
Returns an array of all followers for all users. Accepts POST requests to add a new follow object

### /followers/<int: id>/
Returns an object of the specified follower entry. Accepts DELETE requests if the user owns the follower object

### /likes/
Returns all likes and dislikes from all users. Accepts POST requests to create a new like or dislike

### /likes/<int: id>/
Returns a specific like object. Accepts DELETE requests if the user owns the like object

### /posts/
Returns an array of all posts from all users. Accepts POST requests to create a new post

### /posts/<int: id>/
Returns an object of the specified post. Accepts PUT and DELETE requests if the user owns the post

### /posts/liked/
Returns all posts which the current user has liked

### /tags/
Returns all available tags which a post can use

The API also supports the endpoints from the standard django-rest-auth urls.


## Security
All non-safe methods such as POST, PUT and DELETE require a user to be logged in to perform. PUT and DELETE can also only be performed when the logged in user owns the object which the request is targeting.



## Testing
The following tests were done maually to ensure the backend of the application is functioning as expected. Both the local and deployed projects were tested.

### Attempt to edit a profile when not logged in
A user should not be able to edit a profile when not logged in. When logged out, the PUT form disappears for the profile detail view and the API does not accept a PUT request. This test is a PASS.

### Attempt to edit a profile the user doesn't own
A user should not be able to edit another user's profile. When logged in but viewing another's profile,  the PUT form disappears for the profile detail view and the API does not accept a PUT request. This test is a PASS.

### Attempt to create a post when not logged in
Only logged in user should be able to create a post. When logged out, the POST form is not available and the API does not accept a POST request. This test is a PASS.

### Attempt to edit a post when not logged in
Logged out users should not be able to edit a post. When logged out, the PUT form disappears and the API does not accept the PUT request. This test is a PASS.

### Attempt to edit a post you don't own
Users should not be able to edit a post they don't own. In this case, the PUT form disappears and the API does not accept the PUT request. This test is a PASS.

### Attempt to like a post when logged out
Only logged in users should be able to like posts. When logged out, the POST form disappears and the API does not accept the POST request. This test is a PASS.

### Attempt to delete a like you don't own
Users should not be able to delete a like they don't own. In this case, the DELETE option disappears and the API does not accept the DELETE request. This test is a PASS.

### Attempt to follow a user when logged out
Logged out users should not be able to follow a profile. In this case, the POST option disappears and the API does not accept the POST request. This test is a PASS.

### Attempt to unfollow a user when you don't own the follow object
Users should not be able to unfollow on another user's behalf. In this case, the DELETE option has disappeared and the API no longer accepts the DELETE request. This test is a PASS.

### Attempt to edit a collection item when logged out
A logged out user should not be able to edit a collection item. In this case, the PUT and DELETE options are absent and the API does not accept these requests. This test is a PASS.

### Attempt to delete a collection item you don't own
Only an owning user should be able to delete one of their collection items. In the case of a different user attempting this, the DELETE option is no longer available and the API does not accept the delete request. This test is a PASS.


## Deployment
Below are the steps to deploy this project
- Create a Procfile for Heroku and add the following commands:
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi
- Create a Heroku project and add the following config vars for Cloudinary: API_KEY, API_SECRET, CLOUD_NAME
- Add the DATABASE_URL config var
- Add the DISABLE_COLLECTSTATIC = 1 config var
- Add the allowed CLIENT_ORIGIN and CLIENT_ORIGIN_DEV config vars for CORS
- Git commit and push
- Deploy the branch
 


## Code Validation
There are 2 issues raised in the python linter. One was for using a bare 'except' which is not best practice but not an issue. The other is for some lines being too long. I cannot reformat the code to make this line shorter unless I create a new variable to assign the result of the .first() function but at the stage of validation, this was not feasible as it would require more testing on the application.
![python val err](https://res.cloudinary.com/da2ant1dk/image/upload/v1728941745/python_validation_error_wkaehk.png)

## Known Issues
In the deployed site, there was an instance of a post where liking it or disliking it would increase the Likes/Dislikes_count by 2. I was not able to replicate this locally. The post was deleted and the issue has not appeared in any other posts.

## Problems encountered
- Django's ORM can be too restrictive with joins using filter and select_related so I had to use raw SQL to overcome this for liked posts. For some reason, using lk."IsLike" = 'true' stopped the queries from returning results. The query worked in pgadmin so not sure why this was. Therefore I had to move the filtering for liked/disliked into the react side of app.
- Using the Count function when annotating a queryset was sometimes doubling the correct count. This was happening with the comments_count on the Post model. To get around this quickly, a count of the length of the array of results returned when filtering for the comments for the post was used which resolved the issue.


## Future Features
Below are features which I would like to add to the application in the future.
- Adding more brands would be a good start for expanding the use of the application.
- Obtaining a list of all possible models for each brand (possibly from their Wikis?) and only being able to select from these when adding a collection item would be a better user experience and would act as a restriction on the type of items which could be added to a collection as currently, you could upload anything to your collection if you desire.
- Adding a view for the most followed accounts. I did implement a followers and following count to each profile but using the OwningProfile and FollowedProfile as the objects to count did not work as the followers count was always the same as the following count. As a result this was removed but it would be more efficient to add this back
- Pagination was removed due to time constraints resulting in infinite scrolling being deemed low priority. It is possible for 100s of posts to be made so over time the API would take longer to return results so it would be good to add pagination back in