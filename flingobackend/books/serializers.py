from rest_framework import serializers
from books.models import Booksbase

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booksbase
        fields=('BookId','BookName','BookPrice','BookpicName')