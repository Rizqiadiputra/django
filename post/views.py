from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
# from django.views.generic import TemplateView
# Create your views here.
def post_home(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title":"My User List"
    }
    return render(request, "common/dashboard.html",context)

    # if request.user.is_authenticated():
    #     context = {
    #         "title":"My User List"
    #     }
    #     # return render(request, "common/dashboard.html",context)
    # else:
    #     context = {
    #         "title":"List"
    #     }
    #     return render(request, "common/landingpage.html",context)

def post_create(request):
    # return HttpResponse("<h1>Create</h1>")
    return render(request, "index.html",{})

def post_detail(request, id=None):
    # return HttpResponse("<h1>Detail</h1>")
    # instance = Post.object.get(id=2)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":instance.title,
        "instance": instance
    }
    return render(request,"common/post_detail.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")