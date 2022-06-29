from django import forms
from .models import Post, Comment, FreePost, FreeComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
            # 여기서 폼 추가하면 될 듯 싶은데
        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "강의명을 입력해주세요", # 입력 전 나오는 문구
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }

# class FreePostForm(forms.ModelForm):
#     class Meta:
#         model = FreePost
#         fields = ['title', 'body']

#     def __init__(self, *args, **kwargs):
#         super(FreePostForm, self).__init__(*args, **kwargs)

#         self.fields['title'].widget.attrs = {
#             'class': 'form-control',
#             'placeholder': "글 제목을 입력해주세요",
#             'rows': 20
#         }

#         self.fields['body'].widget.attrs = {
#             'class': 'form-control',
#             'placeholder': "글 제목을 입력해주세요",
#             'rows': 20,
#             'cols' : 100
#         }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }