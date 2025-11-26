from django.db import models

# Model representing an author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model representing a book
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    # One-to-many relationship: One author can write many books.
    # 'related_name="books"' allows accessing an author's books via author.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


    def __str__(self):
        return self.title
