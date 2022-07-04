from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import Calendar, TodoComment, TodoTitle

def showmain(request):
    calendar = Calendar.objects.get(writer=request.user) # 글을 작성한 유저의 캘린더 정보만 가져오겠다.
    return render(request,'mateapp/mainpage.html')


def login(request):
    if request.user.is_authenticated:
        return render(request,'mateapp/mainpage.html')
   
    else:
        return render(request,'account/login.html')

def calendar(request):
    todos = TodoTitle.objects.all()
    return render(request,'mateapp/calendar.html', {'todos':todos})

def todo_detail(request, id):
    todo = get_object_or_404(TodoTitle, pk = id)
    all_comments = todo.comments.all().order_by('-created_at')
    return render(request, 'mateapp/detail.html', {'todo':todo, 'todocomments':all_comments})

def todo_new(request) :
    return render(request, 'mateapp/todo_new.html')

def todo_create(requset):
    new_todo = TodoTitle()
    new_todo.title = requset.POST['title']
    new_todo.save()
    return redirect('mateapp:todo_detail', new_todo.id)

def todo_delete(request, id):
    del_todo = TodoTitle.objects.get(id=id)
    del_todo.delete()
    return redirect('mateapp:calendar')

def todocomment_create(request, todo_id):
    new_todocomment = TodoComment()
    new_todocomment.content = request.POST['content']
    new_todocomment.post = get_object_or_404(TodoTitle, pk = todo_id)
    new_todocomment.save()
    return redirect('mateapp:detail', todo_id)

def todocomment_delete(request, todocomment_id):
    del_todocomment = get_object_or_404(TodoComment, pk = todocomment_id)
    del_todocomment.delete()
    return redirect('mateapp:caledar')

def timetable(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user) # Profile에서 요청받은 user의 정보만 불러옴
        profile.timetable = request.FILES.get('timetable')
        profile.save(update_fields=['timetable'])
    return redirect('mateapp:showmain') # render 보단 redirect 가 낫다.

