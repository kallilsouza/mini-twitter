from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=256, null=True, blank=True)
    followers = models.ManyToManyField('Author', blank=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f"@{self.user.username}"