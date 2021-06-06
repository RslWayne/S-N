from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import News, Like, Image, Dislike, Profile
from .forms import CommentForm, ProfileForm


def news_page(request):
    news = News.objects.all()
    return render(request,'user_dir/index.html',{'news':news})



def news_detail(request,news_id):
    news = News.objects.get(id=news_id)
    likes = news.like_set.all().count()
    images = news.image_set.all()
    comments = news.comment_set.all()
    form = CommentForm(initial={'news':news,'user':request.user})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    return render (request,'user_dir/article.html',{'news':news,'likes':likes,'form':form,'comments':comments,'images':images})

def like(request,news_id):
    # profile = Profile.objects.get(user=request.user)
    new,created = Like.objects.get_or_create(user=request.user,news_id=news_id)
    if not created:
        return HttpResponse('You are already liked!')
    else:
        return redirect('home')


def dislike(request,news_id):
    # profile = Profile.objects.get(user=request.user)
    new,created =Dislike.objects.get_or_create(user=request.user, news_id=news_id)
    if not created:
        return HttpResponse('You are already disliked!')


def profile_settings(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    posts = user.post_set.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form': form,}
    return render(request, 'user_dir/profile.html', context)



def __str__ (self):
    return f"{self.user.username}-{self.created}"



def article_page(request):
    return render (request,'user_dir/article.html')