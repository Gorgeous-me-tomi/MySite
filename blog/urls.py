from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='home-page'),
    path('', views.all_posts, name='posts-page'),
    path('posts/search/', views.search_posts, name='search-tru-posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail-page'),
    path('tag/<tag_name>', views.post_on_tag, name='post-on-tag'),
    # path('authors/<pk>', views.personal_details, name='author-details')
]