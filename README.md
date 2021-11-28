# blog-api

blog posting site api with follower-following system implemented and added comments to blog posts

 -  The site is hosted at https://blog-by-punna.herokuapp.com/api/core/

 
For parameters of post and get request and autherization key you must look into core/serilizers.py and views.py
 
## Examples: 
 -  https://blog-by-punna.herokuapp.com/api/core/ for listing blogs
 -  https://blog-by-punna.herokuapp.com/api/core/9/ for single blog with id 9
## user authentication

 - #### login request to get the auth token 
``` 
  curl --location --request POST 'https://blog-by-punna.herokuapp.com/api/accounts/login/' \
  --form 'username="*********"' \
  --form 'password="*********"'

  response
  {
         "token": "***************************"
  }
```
 - #### For registering as new user
   ``` 
   curl --location --request POST 'https://blog-by-punna.herokuapp.com/api/accounts/register/' \
   --form 'username="**********"' \
   --form 'email="******************"' \
   --form 'password="**********"' \
   --form 'password1="*************"'

   response
   {
       "username": "**********",
       "email": "***************",
       "token": "*****************************"
   }
   ```
 - #### Autherization token attaching to the protected routes
``` 
 curl --location --request GET 'https://blog-by-punna.herokuapp.com/api/core/1/' \
--header 'Authorization: Token *********************************'

```
```
#### append api/core/ to the main url and follow bellow metioned urls
    path('', list_blogs, name='blogs_list'),
    path('create/', create_blog, name='create_blog'),
    path('<int:pk>/', detail_view, name='detail_view'),
    path('<int:pk>/comments/', get_comment_list, name='get_comment_list'),
    path('<int:pk>/comment/post/', post_comment, name='post_comment'),
    path('actions/following/<pk>/', following_actions, name='following_actions'),
    path('actions/<int:pk>/<comment_id>/', comment_actions, name='comment_actions'),
```
