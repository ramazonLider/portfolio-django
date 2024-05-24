from django.shortcuts import render, get_object_or_404
from .models import Project, Category, Blog, Part
# Create your views here
def home(request):
    return render(request, "home.html")

def projects(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, "projects.html", {"projects" : projects, "categories" : categories})

def blogs(request):
    blogs = Blog.objects.all()
    parts = Part.objects.all()
    return render(request, "blogs.html", {"blogs" : blogs, "parts" : parts})

def detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blogs = Blog.objects.all()
    return render(request, "blog_detail.html", {"blog" : blog, "blogs" : blogs})