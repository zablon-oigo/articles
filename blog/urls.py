from django.urls import path
from .views import post_detail,post_list,post_comment, post_search
from .feeds import LatestPostsFeed
app_name="blog"

urlpatterns=[
    path("", post_list, name='post_list'),
    path("tag/<slug:tag_slug>/",post_list, name='post_tag'),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"),
    path("<int:post_id>/comment/",post_comment, name='post-comment'),
    path('comment/<int:post_id>/', post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),
    
]