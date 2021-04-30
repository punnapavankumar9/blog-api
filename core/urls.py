from django.urls import path, include
from .views import list_blogs, detail_view, create_blog

app_name = 'core'

urlpatterns = [
    path('', list_blogs, name='blogs_list'),
    path('create/', create_blog, name='create_blog'),
    path('<pk>/', detail_view, name='detail_view'),
]