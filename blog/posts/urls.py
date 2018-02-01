from django.urls import path
from .views import (PostCreateView, PostUpdateView, PostListView,
                    PostDetailView)

app_name = 'posts'

urlpatterns = [
    path('posts/<int:pk>', PostDetailView.as_view(), name="detail"),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name="update"),
    path('create', PostCreateView.as_view(), name="create"),
    path('', PostListView.as_view(), name="list"),
]
