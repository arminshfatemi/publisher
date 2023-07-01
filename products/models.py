from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50,)
    email = models.EmailField(blank=True,)
    phone = models.CharField(max_length=12, blank=True)
    birthday = models.DateField(blank=True)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    author = models.ManyToManyField("Author",)
    category = models.ManyToManyField('Category', blank=True)
    is_enable = models.BooleanField(default=True)
    file = models.FileField('file', upload_to='files/%Y/%m/%d/')
    created_time = models.DateTimeField(auto_now_add=True)
    # writed_time =
    # bought_count = models.IntegerField(default=0,)

    # def increasing(self,):
    #     self.bought_count += 1

    def __str__(self):
        return f"{self.name}"

