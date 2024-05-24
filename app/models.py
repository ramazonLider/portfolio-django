from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    url = models.URLField()
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=255)
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="part")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="blogs/")

    def __str__(self) -> str:
        return self.name
        