from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    CATEGORIES = (
        ('NEWS', 'School News'),
        ('DANCE_TIPS', 'Dance Tips'),
        ('OPINIONS', 'Opinions')
    )

    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __int__(self):
        print(self.category)
        return self.category

    def __str__(self):
        return str(self.category)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imageURL = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def return_full_name(self):
        return self.author.get_full_name()


