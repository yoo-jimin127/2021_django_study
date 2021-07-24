from django.db import models

# Create your models here.
class Blog(models.Model) : #import해온 models를 가져옴
    title = models.CharField(max_length=200) #models를 가져오는데 character field의 최대 길이가 200개
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField() #작성한 시간을 나타내는
    body = models.TextField() #게시물의 내용

    def __str__(self): 
        return self.title

    def summary(self):
        return self.body[:100]