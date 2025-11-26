from rest_framework import serializers
from  .models import Author, Book
from datetime import datetime

# Serializer for the Book model
# Includes custom validation for the publication_year field
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # get current year
        current_year = datetime.now().year


        # check if the 'value' input year is bigger than current_year
        # if it is, raise a validationerror
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
# Includes a nested BookSerializer to handle the one-to-many relationship
# The 'books' field maps to the related_name defined in the Book model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']