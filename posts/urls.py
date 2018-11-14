from django.urls import path, include
from rest_framework import routers
from posts.views import PostsList, CommentViewSet

router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', PostsList.as_view(), name='api-posts'),
]

urlpatterns += router.urls
