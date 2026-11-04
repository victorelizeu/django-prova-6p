from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


class PostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(organizacao=self.request.user.perfil.organizacao)


class PostDetail(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
