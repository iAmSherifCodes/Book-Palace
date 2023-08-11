from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("books", views.BookViewSet)
router.register('authors', views.AuthorViewSet)
router.register('reviews', views.ReviewViewSet, basename='reviews')
router.register('book-instance', views.BookInstanceViewSet, basename="book-instance")

books_routers = routers.NestedDefaultRouter(router, "books", lookup='book')
books_routers.register('reviews', views.ReviewViewSet, basename='book-review')


books_instance_routers = routers.NestedDefaultRouter(router, "book_instance", lookup="borrow")
books_instance_routers.register('book_instance', views.BookInstanceViewSet, basename='borrow-book')


urlpatterns = router.urls + books_routers.urls + books_instance_routers.urls


# urlpatterns = [
#     path('books/', include(router.urls)),
#     path('author/', include(router.urls))
# path('book/', views.book_list),
# path('book/<int:pk>', views.book_detail),
# path('book/<int:pk>/', views.BookDetail.as_view()),
# path('books/', views.BookList.as_view()),
# path('author/', views.AuthorList.as_view()),
# path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail")
# path('welcome/', views.welcome),
# path('hello/', views.hello),
# path('books/pk/', views.get_books)
# ]
