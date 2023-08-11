from rest_framework import serializers

from .models import Book, Author, ReviewModel, BookInstance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = ['first_name']
        fields = ['id', 'first_name', 'last_name', 'email']


class BooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'copies', 'author']

    # name_of_book =serializers.CharField(source='title')

    # author = AuthorSerializer()

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name="author-detail"
    # )


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ["user", 'book', "price", "date_return"]

    # def create(self, validated_data):
    #     return BookInstance.objects.create(borrow_id=self.context["borrow_id"], **validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ["id", "name", "description"]

    def create(self, validated_data):
        return ReviewModel.objects.create(book_id=self.context['book_id'], **validated_data)


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email']


class CreateBooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'copies', 'author']

    # name_of_book =serializers.CharField(source='title')

# class BookSerializer (serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     isbn = serializers.CharField(max_length=13)
#     genre = serializers.CharField(max_length=8)


# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=150)
#     last_name = serializers.CharField(max_length=150)
#     email = serializers.EmailField
