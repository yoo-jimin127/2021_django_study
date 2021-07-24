from django.shortcuts import render, get_object_or_404, redirect
# shortcuts: view와 templates를 연결해주는 함수들이 담겨있음.
# render : 약간 국민함수 느낌.. -> html을 사이트에 띄우는 역할.
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request): #각 html에 배정된 함수들은 가능하면 그 html의 이름과 동일하게 가면 좋음
    blogs = Blog.objects.all() #blog 작성 시 title, writer ... (모든 objects를 전부 가져온다는 의미)
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, id): #request와 동시에 id값도 자동으로 받아오도록(4번째 게시글을 눌렀을 때 그 상세 페이지를 가져오도록)
    blog = get_object_or_404(Blog, pk= id) #primary key : 기본키 (자동으로 읽어오는 값을 id값으로 하기로)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')