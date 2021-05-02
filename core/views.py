from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from core.serializers import BlogSerializer, CommentSerailizer, CreateFollower, Followerserializer, Followingserializer
from core.models import Blog, Comment, UserFollowing
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@api_view(['GET'])
def list_blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_blog(request):
    if request.method == 'POST':
        # data = request.data.copy()
        # data['author'] = 1
        # request.data['author'] = 1

        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated,])
def detail_view(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(BlogSerializer(blog).data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        if blog.author.username == request.user.username:
            serializer = BlogSerializer(blog, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        return Response(data={'deleted':False, 'error':'you don\'t have access to delete this blog'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'DELETE':
        if blog.author.username == request.user.username:
            blog.delete()
            return Response(data={"deleted": True}, status=status.HTTP_200_OK)
        return Response(data={'deleted':False, 'error':'you don\'t have access to delete this blog'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_comment_list(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except:
        return Response({'error': 'blog doesn\'t exist'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == "GET":
        comments = Comment.objects.filter(blog=pk)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerailizer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def post_comment(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except:
        return Response({'error': 'blog doesn\'t exist'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'POST':
        serializer = CommentSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def comment_actions(request, pk,comment_id):
    try:
        comment = Comment.objects.get(user=request.user, blog=pk,pk=comment_id)
    except:
        return Response({'error': 'comment doesn\'t exist'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        if comment.user.username == request.user.username:
            serializer = CommentSerailizer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'updated':False, 'error':'you don\'t have access to delete this comment'}, status=status.HTTP_401_UNAUTHORIZED)

        
    if request.method == 'DELETE':
        if comment.user.username == request.user.username:
            comment.delete()
            return Response(data={"deleted": True}, status=status.HTTP_200_OK)
        else:
            return Response(data={'deleted':False, 'error':'you don\'t have access to delete this comment'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def following_actions(request, pk):
    if request.method == 'GET':
        if pk == 'followers':
            user = User.objects.get(id=request.user.id)
            followers = user.followers.all()
            paginator = PageNumberPagination()
            paginator.page_size = 10
            result_page = paginator.paginate_queryset(followers, request)
            serializer = Followerserializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        elif pk == 'following':
            user = User.objects.get(id=request.user.id)
            following = user.following.all()
            paginator = PageNumberPagination()
            paginator.page_size = 10
            result_page = paginator.paginate_queryset(following, request)
            serializer = Followingserializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response({'error':'query not found'},status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)

        try:
            user_1 = User.objects.get(pk=pk)
            following = user.following.get(following_user=user_1)

        except User.DoesNotExist:
            return Response({'message': 'the user you want to follow does not exist'}, status=status.HTTP_200_OK)
        
        except:
            following = None
        print(',pavan kumar',  type(following))
        if (following is None and user != user_1) or following is None:
            serializer = CreateFollower(data = {'following_user':pk})
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            following.delete()
            return Response({'message': 'user removed from following list'}, status=status.HTTP_200_OK)
        
