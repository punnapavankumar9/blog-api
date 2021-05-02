# blog1
blog posting site api
`    path('', list_blogs, name='blogs_list'),
    path('create/', create_blog, name='create_blog'),
    path('<int:pk>/', detail_view, name='detail_view'),
    path('<int:pk>/comments/', get_comment_list, name='get_comment_list'),
    path('<int:pk>/comment/post/', post_comment, name='post_comment'),
    path('actions/following/<pk>/', following_actions, name='following_actions'),
    path('actions/<int:pk>/<comment_id>/', comment_actions, name='comment_actions'),`
