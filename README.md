# 2021_django_study
2021 하계방학 장고 스터디

* venv의 activate에 실행할 수 있는 조건들

### MTV
* model : 데이터베이스 -> 커스터마이징 할 수 있는 데이터베이스 + 장고에서 그대로 사용할 수 있는 데이터베이스
1. 스프링: 우리가 db를 따로 설치했어야 함.
1. 장고: sqlite3가 이미 설치되어있음.
1. db 사용법은 따로 금방 배울 수 있음. 

* template : html + css + js : 눈으로 볼 수 있는 템플릿

* view : 함수 (python 기반)

### MVC
- model : MTV와 동일
- view : MTV 패턴에서의 template역할과 거의 같음
- controller : 함수(java 기반)

- 장고의 핵심 : view
-> 눈으로 볼 수 있는 템플릿은 front-end developer

- settings.py : 무엇을 추가할 것인지, 가져오는 db, API 등
- urls.py : url에서 추가되는 주소를 수동으로 설정해주는 부분
- manage.py : 장고를 실행할 때 쓰는 파일 (manage.py runserver)

- blog - 메인페이지, 로그인, 회원가입 등 -> 기능별로 app을 나눌 수 있다
    main app
    views.py : 게시물 관련만

- account app
    views.py : 계정 관리만
    model의 속성을 집어넣을 때의 편리성

* -> 나눠서 하는 이유 : views.py에서 여러 함수를 설정해야함. 협업 부분에 있어 수정 편리하도록
* -> url을 추가할 때 복잡도 최소화를 위해
--------------------------------------------------------------------------------
### app을 생성하였을 때 (startapp을 통해)
* migrations : 데이터베이스를 sqlite에 올려주는..저장된 것을 서버에 유지시켜주는 (안의 init)
	-> Blog라는 규칙을 만들었을 때 이 데이터베이스를 올려줄 것이다(터미널로 대화)
* admin : 장고 자체에서 super계정 (개발자만 들어갈 수 있는) (웹 관리자)
- 무엇을 썼는지, 어떤 회원이 등록했는지 등의 웹사이트의 전체적인 데이터(서버 배포 시 중요하게 작용)
* model : db관리(django.db를 가져옴 (db 명령어를 써도 가능))
* test.py : 테스트케이스 작성
* views.py : 하나의 html마다 각 html에 따라 view가 생성됨 (html을 생성하면 그 html과 관련된 함수가 최소 1개 이상씩 생겨남)
* url은 project 하위 폴더에 있음

* settings.py에 INSTALLED_APPS 추가할 경우 무조건 뒤에 , 붙여주기(에러 발생 가능성 높음)
---
### /admin : 관리자가 관리할 수 있는 계정
* __str__함수 (models.py에 있는) : 관리자가 알기 쉽도록 이 함수 안하면 001.어쩌구라고 나와있을 때
-> 관리자가 관리하기 쉬운 용도로(블로그 자체에는 영향이 가지 않는 함수 (가독성을 높이기 위한 용도 중 하나))

* python manage.py makemigrations 뒤에 migrate하면 Blog(생성한 규칙)이 등록됨
* 개발자 계정 만들기 위해서는 python manage.py createsuperuser로

* urls.py에 admin/은 개발자 계정이니 자동적으로 추가해주는 url
* -> admin으로 들어왔을 때 AUTH~ : 자동적으로 만들어진 것 제공
* -> MAIN (이게 추가한 앱 이름) -> s가 자동으로 붙음 

<<<패턴>>>
1. html을 만들면
2. view를 만들고
3. view를 만들면 url 연결을 해준다

* shortcuts: view와 templates를 연결해주는 함수들이 담겨있음.
* render : 약간 국민함수 느낌.. -> html을 사이트에 띄우는 역할.
* request 치면 요청했을 때 render가 연결해줌

* urls.py에 main.views import *
*    path('', home, name="home"), : 함수 이름, name=""안에 들어가는 것이 url을 무엇으로 할 것인지를 정해주는

* html에서의 blogs가 views의 'blogs'

* for문 {% for i in range %}
* from django.shortcuts import render, get_object_or_404 : object가 없을 때에는 4040에러를 띄워줌

* detail에서     path('<str:id>', detail, name="detail"),
* -> 상세페이지에서 해당 글이 몇번째인지 표시해주지 않으면 충돌 발생
* <str:id>를 사용하여 detail/1 등의 id값을 주소창에 띄워 충돌 방지

* {{blog.summary}} <a href="{%url 'detail' blog.id%}">..more</a>
* -> 작은 따옴표 안의 detail은 url안의 잡은 path의 name (name="detail")
* -> 그 뒤의 blog는 pk값으로 준 (views.py에) id값을

* <form action="" method="post">
*    {% csrf_token %}
* : 주소를 모두 나타나게 하는 것을 막는
* csrf : 공격 방지 ->  post 방식으로 왔다갔다할 때 정보를 보호하기 위한 방법
* 토큰이 이를 막아주는
* 메소드가 post일 때 항상 csrf_token 써주기

- redirect: 한번에 바로가는. 
- render는 요청이 있을 때마다 이를 띄워주는, 정석적인
- from django.utils import timezone -> pub_date

- create(글 쓰는 액션) 화면은 없지만 함수를 만들고, url도 연결
- new_blog.title = request.POST['title'] -> 객체의 title요소에 POST방식
- -> new_blog의 title(Blog의 규칙(title))은 POST안의 title은 new.html에 있는 title(name)
- new_blog.pub_date = timezone.now()
- -> 현재 시간을 가져오는
- new_blog.save() : 작성한 내용을 그대로 데이터베이스 안에 업데이트 -> 자동으로 id가 생성됨
- return redirect('detail', new_blog.id) -> 내용 저장을 마치면 detail으로 넘어가고 이 때 함께 id로 넘어감

```<form action="{% url 'create' %}" method="post">```
----------------------------------------------------------------------
- edit_blog = Blog.objects.get(id=id)
- -> 수정된 아이들은 edit_blog
- 이를 blog로 표현 (pk 변경될 수 있으니 id)
    ```
    <p>제목 : <input type="text" name="title" value="{{blog.title}}"></p>
    <p>작성자 : <input type="text" name="writer" value="{{blog.writer}}"></p>
    본문 : <textarea name="body" id="" cols="30" rows="10">{{blog.body}}</textarea>
    ```
- -> value

```
def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})
```
- -> edit가 blog로 연결되어있으므로 action에 blog.id
--------------------------------------------------------------
<<8/1>>
- 템플릿 상속을 하는 이유 : 스프링부트 등의 툴을 사용해 예를 들어 네브바, 로고 등을 사용할 때 이를 페이지별로 다 적용해야함.
-> 매우 번거로움. 
-> 템플릿 상속을 통해 이를 한번에 할 수 있도록

부트스트랩에서 css코드 가져오기 -> css를 사용하겠다!

템플릿 상속을 위하여 부모 폴더 안에 templates 만들기

{% extends 'base.html' %}
{% block content %} 

base.html에
    <div class="container">
            {% block content %}
            {% endblock %}
    </div>
-> 빈 공간을 만들어서 여기서 상속되도록

settings.py의 디렉토리 DIRS에 앱이름, 템플릿 폴더 이름 추가해주기
-> 폴더 안의 것을 기본으로 삼아서 템플릿 상속하겠다는 의미


상속: URL에서도 사용됨. -> urls.py를 만들어서 부모의 urls.py 내용을 복붙해옴

admin이랑 home은 없애서 붙여넣기
main.views에서 main을 없애기
from django.contrib import admin
from django.urls import path, include
from .views import *

urls.py의 것들을 구분해주기 위해 부모의 urls.py에 main패스 연결
-> url을 보면 main/이 추가된 것을 확인할 수 있음

static & media
- 정적파일 (static): 
미리 서버에 저장되어있는 파일
서버에 저장된 그대로를 서비스해주는 파일 (img, js, css)
- 동적파일 (media):
서버의 데이터들이 어느정도 가공된 다음 보여지는(상황에 따라 달라지는)
(사용자가 업로드할 수 있는 파일)


- static 폴더를 만들기
- settings.py에 static 폴더를 넣음


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main', 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

-> main 폴더 안의 static 안의 모든 요소를 static에서 읽을 때 바로 읽을 수 있도록 시스템 상에서 명시해주는 것
-> warning 해결 : import os

python manage.py collectstatic
-> 이미지 파일을 가져다가 쓸 수 있도록 하는
-> 이미지를 개인 앱에 넣고 나서 이 명령어를 사용하여 static파일에 추가
-> 배포할 때 사용하기 때문에 이 파일에 넣는 작업이 필요

base.html에서 static을 사용한다고 할 때에는 {% load static %}


media에도 똑같은 작업 추가
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

media를 추가하고 나서는
부모 url에 
from django.conf.urls.static import static 
from django.conf import settings 추가

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
-> static을 더할 예정임. 그 안에 settings.MEDIA_URL을 추가하고, document_root에는 settings.py에 추가한 것들을 url으로써 추가하겠다는 의미

models.py에 image = models.ImageField(upload_to = "main/", blank=True, null=True)
-> 이미지를 올려도 되고, 안올려도 되고
-> media를 사용자들이 올릴 수 있도록

pip install pillow
이미지를 업로드할 수 있도록 도와주는 것 (필수적인 요소)

migrations의 0001과 pycache의 0001을 다 지우고 dbsqlite도 지움
그 다음 다시 super user를 생성해줌
-> 이렇게 해야 image를 추가할 수가 있음.

new.html에 <p>사진 : <input type="file" name="image"></p>을 추가
-> new post버튼에서 연결되는 new.html에 이미지 삽입이 추가될 수 있도록
<form action="{% url 'create' %}" method="post" enctype="multipart/form-data">
-> 인코딩 타입을 multipart/form-data로 설정한다는 의미

new_blog.image = request.FILES['image']
-> files형식으로 request

```<p><img src="{{blog.image.url}}" alt=""></p>``` 를 detail.html에 추가
-> 이미지가 없는 경우에는 어떻게 해야하나?
```
    {% if blog.image %}
        <p><img src="{{blog.image.url}}" alt=""></p>
    {% endif %}
```
-------------------------------
forms.py를 추가
```
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm) :
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'body', 'image']
```
-> modelForm : 모델스에 규칙을 추가하였는데, 이를 폼으로 가져오겠다는 의미
메타 클래스 : 이 클래스 내에서 이름표 역할을 함.
-> models에 필드 형식을 만들어놨으니, field값에 이 형식에 맞게 넣어라!
-> new.html의 입력받는 부분을 forms.py가 대신 만들어줄 것인데, 이 내용을 쓰기 위해 폼을 장고가 알아서 만들어줄 수 있도록 

views.py에 from .forms import BlogForm를 import
def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})
new 함수를 수정

<<꿀팁!!>>
ctrl+? :주석처리
ctrl + alt + 방향키 : 여러 줄에 같은 명령어를 입력

{{form.as_p}} : form의 요소들을 p 태그로 감쌈

<유효성 검사>
```
def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')
```
        new_blog = form.save(commit=False)
-> 유효하면 저장하지만 임시저장만 해달라, 커밋은 하지 말라
        new_blog.pub_date = timezone.now()
-> pub.date때문에 이걸 씀!
-------------------------------------------------------------------
<user 관리>
장고에서 주는 기능 사용

django-admin startapp account로 앱을 하나 더 생성해줌
settings.py에 account 추가해줌

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

-> login_view 함수 추가
form에서 로그인 받아야함.

account에 urls.py를 만들어줌
부모 url에    path('account/', include('account.urls')), 추가
login.html에서 폼태그를 읽어올 것임

base.html에서 login 버튼을 추가해준다
<a class="nav-link" href="{% url 'login' %}">Login</a>

views.py에 코드 추가
로그인은 보안이 중요하기에 POST 방식으로 넣어주어야함.
로그인에서도 유효성검사가 필요함 (장고 내에서 존재하는 형식 제한이 있는지 없는지를 확인하기 위하여)
-> 유효성검사가 통과하면 입력값을 form 안의 cleaned_data가 넘어감. == id넣으면 id에, password 넣으면 password에 넣어라.

user : username과 password가 있는 사용자를 user로 -> authenticate는 회원가입이 되어있다는 전제 하에 적은 것인데,
user가 해당 username과 password가 같은지를 대조확인

None이 아니면 login을 해라. login이라는 메소드를 불러오는. 이 때 두가지 매개변수가 필요한데, request와 user를 넘겨야함.
-> 하면 if문 탈출
-> 유효성검사 if문 탈출

로그인 되면 어디로 이동할 것인지? -> home으로 redirect
django login views : 모두 이와 비슷하게 코드가 구현되어있는 것을 확인할 수 있음

<이 패턴을 기억하자>
1) POST방식이냐?
2) form 데이터가 규칙에 맞냐? - 입력 형식이 올바르냐?
3) 회원가입한 데이터에 이 정보가 있냐?
-> 세가지 조건을 충족하면 로그인 완료

    {% if user.is_authenticated %}
        {{user.username}}
    {% endif %}
-> user가 is_auth한 상태이면 -> 로그인 한 상태면 username을 띄워줘라

register_view 추가
1) POST방식이냐?
2) form 데이터가 규칙에 맞냐?
-> 중복 회원가입 등에 대한 확인 가능

url 추가
상황에 따라 nav바가 바뀔 수 있도록 추가
