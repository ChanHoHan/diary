from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Diary
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def introduce(request):
    return render(request, 'introduce.html')

@login_required
def contents(request):
    diarys = Diary.objects
    diary_list = Diary.objects.all()
    paginator = Paginator(diary_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'contents.html',{'diarys':diarys, 'posts':posts})

@login_required
def detail(request, daily_id):
    diary_detail = get_object_or_404(Diary, pk = daily_id)
    return render(request, 'detail.html',{'diary_detail':diary_detail})

@login_required
def new(request):
    return render(request, 'new.html')

@login_required
def delete(request, daily_id):
    post = get_object_or_404(Diary, pk = daily_id)
    post.delete()
    return redirect('contents')

@login_required
def edit(request, daily_id):
    diary_edit = get_object_or_404(Diary, pk = daily_id)
    return render(request, 'edit.html', {'diary_edit':diary_edit})

@login_required
def create(request):
    diary = Diary()
    diary.title = request.GET['title']
    diary.content = request.GET['content']
    diary.date = timezone.datetime.now()
    diary.save()
    return redirect('contents')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')


def update(request, daily_id):
    diary = Diary.objects.get(pk=daily_id)
    diary.title = request.GET['title']
    diary.content = request.GET['content']
    diary.date = timezone.datetime.now()
    diary.save()

    return redirect('contents')