from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}' 
 
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    work = models.CharField(max_length=50, null=True)
    about = models.TextField(max_length=300, null=True)
    image = models.ImageField(upload_to='posts', null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='tag_for_posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 