from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_comment = form.save(commit=False)
            user_comment.user = request.user
            user_comment.save()
            # form.save()
            return redirect('index')
        else:
            return render(request,'index.html',context)
    comment = Comment.objects.all() # bir modelin içindeki her value değerini çek 
    tersComment = reversed(comment)

    form = CommentForm()
    context = {
        'yorum':tersComment,
        'form':form,
    }
    return render(request,'index.html',context)

def sil(request):
    if request.method == 'POST':
        silId = request.POST['silValue']
        silComment = Comment.objects.filter(id=silId)
        silComment.delete()
        return redirect ('index')


