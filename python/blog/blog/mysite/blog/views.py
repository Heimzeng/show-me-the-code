from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponse
from .models import Article, Updates
import markdown
from PIL import Image
def index(request):
    class paginator:
      posts = Article.objects.all().order_by('-date')
    for post in paginator.posts:
    	post.content = markdown.markdown(post.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/index.html', context={'paginator': paginator})
def detail(request, pk):
    post = Article.objects.get(pk=pk)
    post.content = markdown.markdown(post.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/base.html', context={'post': post})
def base(request, pk):
	post = Article.objects.get(pk=pk)
	post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
	return render(request, 'blog/base.html', context={'post': post})
def about(request):
  record_list = Updates.objects.all().order_by('-date')
  for record in record_list:
      record.content = markdown.markdown(record.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
  return render(request, 'blog/about.html', context={'record_list': record_list})
def upload(request):
  if request.method == 'POST':
    reqfile = request.FILES['file']  
    image = Image.open(reqfile)  
    image.save("blog/static/blog/img/1.jpeg","jpeg")  
    return HttpResponse("ok")
  elif request.method == 'GET':
    return render(request, 'blog/upload.html')