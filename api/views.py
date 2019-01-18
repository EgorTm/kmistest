from __future__ import unicode_literals
from rest_framework import generics
from .serializers import PostSerializer
from ../blog.models import Post

# Create your views here.


class DetailsPostView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer
