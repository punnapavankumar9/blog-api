from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from core.serializers import BlogSerializer
from core.models import Blog
from django.contrib.auth.models import User
# Create your views here.


@api_view(['GET'])
def list_blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 1
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
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    if request.method == 'DELETE':
        blog.delete()
        return Response(data={"deleted":'True'}, status=status.HTTP_204_NO_CONTENT)