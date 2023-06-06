from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import ListView

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()

    context = {
        'form': form,
    }
    return render(request, 'base/add_comment.html', context)


class ListOfComments(ListView):
    paginate_by = 25
    model = Comment
    ordering = ['-pk']


    def post(self, request):
        selected_value = request.POST.get('select_value')
        comments = Comment.objects.all().order_by(selected_value)
        paginator = Paginator(comments, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'base/comment_list.html', {'page_obj': page_obj})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_by'] = self.paginate_by
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('replies')
        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-id')
        # validate ordering here
        return ordering


def create_reply(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.save()
            return HttpResponseRedirect('/')

        else:
            form = ReplyForm()

    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, 'base/reply.html', context)
