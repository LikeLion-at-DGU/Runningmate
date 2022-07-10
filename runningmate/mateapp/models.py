from email.policy import default
from itertools import product
from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField


# from addproject.models import *
from addproject.models import Project

# Create your models here.

class Calendar(models.Model): # 대시보드 캘린더 모델
    id = models.AutoField(primary_key=True)
    # title = models.ForeignKey(Project, on_delete=models.PROTECT) # project에서 제목 불러오기 연결된 요소들이 같이 삭제되지 않도록 
    title = models.CharField(max_length=20 ,null=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    startday = models.DateField(null=True)
    endday = models.DateField(null=True)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)
    place = models.CharField(max_length=20)
    body = models.TextField()

    COLOR_PALETTE = [
        ("#50cfbc","1",),("#fe7782","2",),("#45bfff","3",),("#ffbc54","4",),("#735bf2","5",),
        ]
    color = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
    
    class Meta:
        verbose_name = "캘린더"
        verbose_name_plural = "캘린더(들)"
# 캘린더 모델을 다룰거다라는 request를 보냄 but 반영이 안돼서 에러가뜸
# no such column 은 migrations 오류임

# class Project(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     writer = models.ForeignKey(User,on_delete=models.CASCADE)
#     pub_date = models.DateField() # 시간이 필요 없어서 변경함
#     body = models.TextField()
# 캘린더랑 Todo 연결해서 필요 없어짐 ..

# 프로젝트 관리에서 받아오기 떄문에 필요 없음 
# class TodoTitle(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     user = models.ForeignKey(User,on_delete=models.CASCADE) # 외래키를 유저 모델과 연동하겠다. 유저객체가 삭제됐을 때 연동된 객체를 같이 삭제하겠다
    # on_delete 설정을 안하면 그대로 남게된다. 네이버 지식인 같은 것임
    # 만약 온딜리트 설정을 해놨다면 회원탈퇴시 같이 삭제되는 것임 

# class Todo(models.Model):
#     content = models.TextField()
#     project = models.ForeignKey(Calendar ,on_delete=models.CASCADE, related_name='todos')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.post
    
    # def todocomment(self):
    #     return self.post

# 게시판 모델 구현 필요기능
# 게시글 작성 날짜 models.DateField()
# 게시글 제목
# 게시글이 현재로 부터 



class Post(models.Model):
    day = models.DateField(auto_now_add=True) # 현재 생성일자를 출력
    title = models.CharField(max_length=30) # 할 일 리스트를 게시판 형식 제목으로 받음
    body = models.TextField()
    user = models.ForeignKey(User,verbose_name="작성자",on_delete=models.CASCADE) # 옆에 작성한 사람 얼굴이 떠야하니까 유저 모델 및 on_delete 적용
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="posts")



    def __str__(self):
        return self.title

class Comment(models.Model):
    day = models.DateField(auto_now_add=True) # 댓글 입력 날짜 출력
    user = models.ForeignKey(User,on_delete=models.CASCADE) # 한 명의 유저한테 여러명의 댓글 관계를 맺는모델, 기본 모델이라소 related_name 쓸 필요없다
    content = models.CharField(max_length=200) # 댓글을 입력할 창
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name ='comments') 
    file = models.FileField(upload_to="comment/", blank=True, null=True) # 파일을 전송할 수 있도록 만듬    
   
    def __str__(self):
        return self.content


 # 유저한명당 여러개의 코멘트가 가능해서 1(유저) N(코멘트)로써 적용됨
    # 한 개의 게시글에도 여러개의 코멘트가 가능함
    #  포스트는 게시글이고 이건 댓글인데, Post에 대한 Foreign을 작성해야함
    # related_name 은 나중에 추적을 할 때 쓰는거임
    # on_delated 는 게시글 삭제시 댓글을 다 삭제한다는 것임

