from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Comment
from .models import User

# Create your views here.
def wall(request):
    if 'user' in request.session:
        context={
            "posts":Post.objects.all(),
            'user': User.objects.get(id=request.session['user'])
        }
        return render(request, 'wall.html', context)
    else:
        return redirect('/')

#creates new post for the logged in user
def createPost(request):
    if 'user' in request.session:
        errors=Post.objects.validator(request.POST)
        if(len(errors)>0):
            for key, val in errors.items():
                messages.error(request, val)
            return redirect('/wall')
        else:
            loggedUser = User.objects.get(id=request.session['user'])
            Post.objects.create(content=request.POST['post'], user=loggedUser)
            return redirect('/wall')
    else:
        return redirect('/')

#creates a new comment to the post
def createComment(request):
    if 'user' in request.session:
        errors=Post.objects.validator(request.POST)
        if(len(errors)>0):
            for key, val in errors.items():
                messages.error(request, val)
            return redirect('/wall')
        else:
            loggedUser = User.objects.get(id=request.session['user'])
            print('comment generator')
            Comment.objects.create(content=request.POST['comment'], user=loggedUser, post=Post.objects.get(id=request.POST['id']))
            return redirect('/wall')
    else:
        return redirect('/')

def destroy(request):
    if 'user' in request.session:
        Post.objects.get(id=request.POST['postID']).delete()
        return redirect('/wall')
    else:
        return redirect('/')