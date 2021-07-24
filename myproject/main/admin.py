from django.contrib import admin
from .models import Blog #해당 폴더 안에 있는 Blog 규칙을 여기에 작성하겠다는 의미

admin.site.register(Blog) #admin안의 규칙 

# Register your models here.
