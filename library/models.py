from django.db import models

# Create your models here.
class Genre(models.Model):

    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character ISBN number</a>')
    pages = models.SmallIntegerField()

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    # models.CASCADE tells the book object to delete itself if the associated Author is deleted
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book", related_name='books')
    
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    


