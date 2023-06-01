from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
from django.core.paginator import Paginator


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by("created_at")
    comments_per_page = 25
    paginator = Paginator(comments, comments_per_page)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    print(paginator.num_pages)
    context = {
        'form': form,
        'comments': page_objects,
        'page_obj': page_objects,
    }

    return render(request, 'base/comment.html', context)


def create_reply(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.save()
            return HttpResponseRedirect('/')
    else:
        form = ReplyForm()

    replies = comment.replies.all().order_by('-pk')

    context = {
        'form': form,
        'comment': comment,
        'replies': replies
    }

    return render(request, 'base/reply.html', context)
