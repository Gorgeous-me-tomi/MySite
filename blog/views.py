from ast import arg
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse

from django.views import View
from django.views.generic import ListView
from django.db.models import Q


from .models import Author, Post, Tag, Comment
from .forms import CommentForm

posts = Post.objects.all().order_by('-date')
tags = Tag.objects.all()

# Create your views here.

@csrf_exempt
class HomeView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


@csrf_exempt
def all_posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': posts,
        'other_posts': posts,
        'tags': tags,
        # 'post_tags': posts.tags.all(),
        'post_category': 'All Posts',
    })

@csrf_exempt
def search_posts(request):
    q = request.GET.get('q')
    qs = posts.filter(title__contains=q)

    authour_qs = Author.objects.filter(Q(first_name__contains=q) | Q(last_name__contains=q))

    return render(request, 'blog/all-posts.html', {
        'all_posts': qs,
        'author_search': authour_qs,
        'other_posts': posts,
        'tags': tags,
        'post_category': f"Post filtered by '{q}'",
        'query': q.title(),
        'searched': True,
    })


@csrf_exempt
def post_on_tag(request, tag_name):
    requested_tag = Tag.objects.filter(caption=tag_name)
    try:
        post_tags = requested_tag[0].tag_for_posts.all()
    except: 
        return HttpResponse('Url is not found')
    return render(request, 'blog/all-posts.html', {
        'all_posts': post_tags,
        'other_posts': posts,
        'tags': tags,
        'post_category': f'{tag_name} Posts',
        'query': tag_name,
    })


class PostDetailView(View):
    @csrf_exempt
    def get(self, request, slug):
        requested_post = get_object_or_404(Post, slug=slug)
        author = requested_post.author
        comment_form = CommentForm()

        return render(request, 'blog/post-detail.html', {
            'post': requested_post,
            'post_tags': requested_post.tags.all(),
            'author': author,
            'author_posts': author.posts.all(),
            'comments': requested_post.comments.all().order_by('-id'),
            'comment_form': comment_form,
        })

    @csrf_protect
    def post(self, request, slug):
        requested_post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = requested_post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))


        author = requested_post.author

        return render(request, 'blog/post-detail.html', {
            'post': requested_post,
            'post_tags': requested_post.tags.all(),
            'author': author,
            'author_posts': author.posts.all(),
            'comments': requested_post.comments.all().order_by('-id'),
            'comment_form': comment_form,
        })
        

@csrf_exempt
def personal_details(request, pk):
    requested_author = get_object_or_404(Author, pk=pk)
    # print(requested_author)
    # print(requested_author.posts)

    return render(request, 'blog/personal_details.html', {
        'author': requested_author,
        'posts': requested_author.posts.all(),
    })





# class PersonalDetails(ListView):
#     template_name = 'blog/personal_details.html'
#     model = Post
#     ordering = ['-date']
#     context_object_name = 'posts'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:3]
#         return data

