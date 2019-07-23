from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostListView(ListView):

    model = Post
    template_name = "blog_curso/post_list.html"
    # paginate_by = 2

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        queryset = queryset.order_by("-id")
        return queryset


class PostFormView(FormView):
    form_class = PostForm

    success_url = reverse_lazy('posts_list')
    template_name = "blog_curso/post_edit.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return super(PostFormView, self).form_valid(form)


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().prefetch_related(
        "post_set"
    )
    serializer_class = UserSerializer

posts = PostListView.as_view()
post_new = login_required(PostFormView.as_view(), login_url="/admin/login")
