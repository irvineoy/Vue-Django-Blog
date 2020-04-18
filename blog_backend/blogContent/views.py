from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from blogContent.models import blogContents, commentContent
import json
from django.core import serializers 
# from django.template import loader 
# from django.db import models

# Create your views here.

def showBlogList(request):
    objectList = blogContents.objects.all()
    data = {}
    data['list'] = json.loads(serializers.serialize("json", objectList))
    return JsonResponse(data)


def showBlog(request):
    # print(request.GET['id'])
    objectContent = blogContents.objects.get(id=request.GET['id'])
    data = {
        'content': objectContent.content,
        'id': objectContent.id,
        'timesOfRead': objectContent.timesOfRead,
        'timesOfReply': objectContent.timesOfReply,
        'title': objectContent.title,
        'updataTime': objectContent.updataTime
    }
    return JsonResponse(data)
    
def addComment(request):
    commentContent.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        comment = request.POST['comment'],
        blogId = request.POST['blogid'],
    )
    return HttpResponse({"msg": 'success'})


def showComments(request): # todo
    # comments = commentContent.objects.get(id=request.GET['blogid'])
    comments = commentContent.objects.filter(blogId__exact=int(request.GET['blogid']))
    dataList = []

    for comment in comments:
        i = {
            'comment': comment.comment,
            'name': comment.name,
            'id': comment.id,
            'commentTime': comment.commentTime
        }
        dataList.append(i)
    data = {
        'list': dataList
    }
    return JsonResponse(data)


def home(request):
    return render(request, "index.html")



# for test
def addBlogList(request):
    blogContents.objects.create(
        title = 'Mac 命令行终端 设置代理 privoxy',
        content = 'HelloDjango 博客教程就要准备告一段落了，接下来我会开始以定期更新的方式向大家介绍 django-restframework + Vue 或者 React 这种更加现代化的前后端分离开发方式，大量公司都采用这种开发方式，如果你以找工作为目的而学习 django 的话，怎么能不学习这种开发模式呢？',
        timesOfReply = 0,
        timesOfRead = 0
    )
    return HttpResponse({"msg": 'success'})