from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    text = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def view_admin_site(self):
        return f"{self.title} | {self.author.full_name()}"

    def __str__(self):
        return self.view_admin_site()


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def view_admin_site(self):
        return f"{self.user_name} | {self.user_email}"

    def __str__(self):
        return self.view_admin_site()