from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PostForm
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
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print form.cleaned_data.get("title")
        instance.save()
        return redirect(instance.get_absolute_url())
    # if request.method == "POST":
    #     title request.POST.get("title")
    #     content request.POST.get("content")
    #     Post.objects.create(title=title)
    #     Post.objects.create(content=content)
        
    context = {
        "form": form,
    }
    # return HttpResponse("<h1>Create</h1>")
    return render(request,"common/post_form.html", context)
    

def post_detail(request, id=None):
    # return HttpResponse("<h1>Detail</h1>")
    # instance = Post.object.get(id=2)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":instance.title,
        "instance": instance
    }
    return render(request,"common/post_detail.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())        

    context = {
        "title":instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request,"common/post_form.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")