from django.test import TestCase
from api.models import Author
from django.contrib.auth.models import User
from api.models.post import Post

# Create your tests here.

class AuthorTestCase(TestCase):
    def setUp(self):
        user = User(username='test000', 
                    first_name='Test', 
                    last_name='000', 
                    email='test000@email.com')
        user.set_password('933#0bMp49!@m;')
        user.save()
        Author.objects.create(user=user, bio="Testing")
        user = User(username='test001', 
                    first_name='Test', 
                    last_name='001', 
                    email='test001@email.com')
        user.set_password('933#0bMp49!@m;')
        user.save()
        Author.objects.create(user=user, bio="Testing")
        user = User(username='test002', 
                    first_name='Test', 
                    last_name='002', 
                    email='test001@email.com')
        user.set_password('933#0bMp49!@m;')
        user.save()
        Author.objects.create(user=user, bio="Testing")
        return super().setUp()

    def test_can_users_follow_others(self):
        test000 = Author.objects.get(user__username='test000')
        test001 = Author.objects.get(user__username='test001')
        test002 = Author.objects.get(user__username='test002')
        
        test000.add_to_followers(test001)
        self.assertEqual(test000.is_followed_by(test001), True)
        self.assertEqual(test000.is_followed_by(test002), False)
    
    def test_can_users_unfollow_others(self):
        test000 = Author.objects.get(user__username='test000')
        test001 = Author.objects.get(user__username='test001')
        
        if not test000.is_followed_by(test001):
            test000.add_to_followers(test001)
        
        test000.remove_from_followers(test001)
        self.assertEqual(test000.is_followed_by(test001), False)

class PostTestCase(TestCase):
    def setUp(self):
        user = User(username='test000', 
                    first_name='Test', 
                    last_name='000', 
                    email='test000@email.com')
        user.set_password('933#0bMp49!@m;')
        user.save()
        Author.objects.create(user=user, bio="Testing")
        return super().setUp()

    def test_can_author_post(self):
        author = Author.objects.get(user__username='test000')
        text = 'Just a test'
        post = Post.objects.create(author=author, text=text)
        self.assertEqual(str(post), f"{text[:10]}... (@{author.user.username})")
        self.assertEqual(post.author.user.username, author.user.username)
        self.assertEqual(post.text, text)