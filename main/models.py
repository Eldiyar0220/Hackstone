from django.db import models

# Create your models here.
from django.db import models

from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    marka_model = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    # year = models.PositiveIntegerField(null=False)

    text = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) #это после запятой decimal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marka_model


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    # def get_image_url(self):
    #     if self.image:
    #         return self.image.url
    #     return ''
    #







