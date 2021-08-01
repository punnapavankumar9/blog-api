# blog-api

blog posting site api with follower-following system implemented and added comments to blog posts

 -  The site is hosted at https://blog-by-punna.herokuapp.com/api/core/

append api/core/ to the main url and follow bellow metioned urls
 
For parameters of post and get request and autherization key you must look into core/serilizers.py and views.py
 
## Examples: 
 -  https://blog-by-punna.herokuapp.com/api/core/ for listing blogs
 -  https://blog-by-punna.herokuapp.com/api/core/9/ for single blog with id 9
```
    path('', list_blogs, name='blogs_list'),
    path('create/', create_blog, name='create_blog'),
    path('<int:pk>/', detail_view, name='detail_view'),
    path('<int:pk>/comments/', get_comment_list, name='get_comment_list'),
    path('<int:pk>/comment/post/', post_comment, name='post_comment'),
    path('actions/following/<pk>/', following_actions, name='following_actions'),
    path('actions/<int:pk>/<comment_id>/', comment_actions, name='comment_actions'),
```
