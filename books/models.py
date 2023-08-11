from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=11)
    # password = models.CharField(max_length=23)


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # class Meta:
    #     # - infront make the list reversed
    #     ordering = ['first_name']


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'Romance')
    ]
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default="Finance")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # when models = set_null, set another arg with null = True. it can also be PROTECTED
    date_published = models.DateField(blank=True, null=True)
    copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.isbn}"

    class Meta:
        # - infront make the list reversed
        ordering = ['title']


class Address(models.Model):
    # street_nos = models.IntegerField()
    # house_nos = models.CharField()
    house_nos = models.PositiveIntegerField()
    street_name = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=200, default="Nigeria")


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_borrow = models.DateField(auto_now_add=True)
    date_return = models.DateField(auto_now_add=False)


class ReviewModel(models.Model):
    name = models.CharField(max_length=200)
    # date_and_time = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    # book = models.ManyToOneRel(Book, on_delete=models.PROTECT, to="Book", field_name="book")
    description = models.TextField(max_length=1200, default="Enter a  Review")
