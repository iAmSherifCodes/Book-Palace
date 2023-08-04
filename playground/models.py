# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# # Create your models here.
#
# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=11)
#
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(unique=True)
#
#
# class Book(models.Model):
#     GENRE_CHOICES = [
#         ('FICTION', 'fiction'),
#         ('ROMANCE', 'romance'),
#         ('FINANCE', 'finance'),
#         ('SPORT', 'sport')
#     ]
#
#     title = models.CharField(max_length=150)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     date_published = models.DateField(blank=True, null=True)
#     isbn = models.CharField(max_length=150)
#     copies = models.IntegerField()
#     genre = models.CharField(max_length=12, choices=GENRE_CHOICES, default="sport")
#
#
# class Address(models.Model):
#     house_nos = models.PositiveIntegerField()
#     street_name = models.CharField(max_length="150")
#     city = models.CharField(max_length=150)
#     state = models.CharField(max_length=100)
#
#
# class BookInstance(models.Model):
#     book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     date_borrowed = models.DateField(auto_now_add=True)
#     date_returned = models.DateField(auto_now_add=True)
