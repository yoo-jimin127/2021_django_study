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