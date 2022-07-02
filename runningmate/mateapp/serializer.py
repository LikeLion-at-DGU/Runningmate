# todo 데이터 직렬화 파일
# 데이터를 json 형식으로 전달하기 위함

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description',) # Todo 테이블의 필드
    