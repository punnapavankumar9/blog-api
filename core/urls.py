from django.urls import path, include
from .views import list_blogs, detail_view, create_blog, post_comment, comment_actions, get_comment_list

app_name = 'core'

urlpatterns = [
    path('', list_blogs, name='blogs_list'),
    path('create/', create_blog, name='create_blog'),
    path('<pk>/', detail_view, name='detail_view'),
    path('<pk>/comments/', get_comment_list, name='get_comment_list'),
    path('<pk>/comment/post/', post_comment, name='post_comment'),
    path('actions/<pk>/<comment_id>/', comment_actions, name='comment_actions'),
]