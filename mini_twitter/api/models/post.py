from django.db import models
from api.models.author import Author

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return f"{self.text[:10]}... (@{self.author.user.username})"