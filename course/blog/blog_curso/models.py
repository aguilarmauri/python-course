from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',
                               on_delete=models.SET_NULL,
                               null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image_post = models.ImageField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Tiene que tener una relacion con el post y con el user
    post: es el post al que pertenece el comentario
    user: es el author del comentario (no del post)
    """
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE)
    post = models.ForeignKey('blog_curso.Post',
                             on_delete=models.CASCADE)
    content = models.TextField()

