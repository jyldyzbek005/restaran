from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='foods')
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookTable(models.Model):
    name = models.CharField(max_length=255)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.DateTimeField()
    persons = models.IntegerField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'клиент{self.name}забронировал место{self.table.name}'


class Response(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=277)
    message = models.CharField(max_length=2355)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    index = models.CharField(max_length=255)
    title = models.CharField(max_length=244)
    text1 = models.TextField(max_length=266)
    text2 = models.TextField(max_length=266)
    text3 = models.TextField(max_length=266)
    desc = models.TextField()

    def __str__(self):
        return self.name
