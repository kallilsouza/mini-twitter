from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import ObjectDoesNotExist

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=256, null=True, blank=True)
    followers = models.ManyToManyField('Author', blank=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f"@{self.user.username}"

    def followers_count(self):
        return self.followers.count()

    def add_to_followers(self, author):
        if self.pk == author.pk:
            raise ValidationError("Cannot be followed by self")
        if author in self.followers.all():
            return f"{author.user.username} already follows {self.user.username}"
        self.followers.add(author)
        return f"{author.user.username} followed {self.user.username}"
    
    def remove_from_followers(self, author):
        if not author in self.followers.all():
            return f"{author.user.username} does not follow {self.user.username}"
        self.followers.remove(author)
        return f"{author.user.username} unfollowed {self.user.username}"

    def is_followed_by(self, author):
        return author in self.followers.all()

@receiver(post_save, sender=User)
def handle_new_user(sender, **kwargs):
    user = kwargs['instance']
    try:
        author = user.author
    except ObjectDoesNotExist:
        author = Author.objects.create(user=user)