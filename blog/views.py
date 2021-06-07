from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment
from django.contrib import messages

# Create your views here.

def bloghome(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request,'blog/bloghome.html',context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict:
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'post': post, 'comments' : comments, 'user':request.user, 'replyDict':replyDict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        parentSno = request.POST['parentSno']
        post = Post.objects.get(sno=postSno)
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "your comment has been posted successfully..!!!")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "your reply has been posted successfully..!!!")




    return redirect(f'/blog/{post.slug}')
