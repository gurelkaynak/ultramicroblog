from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions

#from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


