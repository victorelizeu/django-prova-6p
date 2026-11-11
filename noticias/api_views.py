from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(request.user, 'perfil') and request.user.perfil.papel == 'admin'


class PostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(organizacao=self.request.user.perfil.organizacao)

    def perform_create(self, serializer):
        serializer.save(organizacao=self.request.user.perfil.organizacao)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(organizacao=self.request.user.perfil.organizacao)
