from __future__ import unicode_literals
from ..first_app.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")
    def __str__(self):
        return self.title

class QuoteManager(models.Manager):
    def validate_quote(self, post_data):
        errors = []

        if len(post_data['title']) < 1 or len(post_data['quote']) < 1:
            errors.append('fields are required')
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more characters')

        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more characters')
        if not int(post_data['rating']) > 0 or not int(post_data['rating']) <= 5:
            errors.append('invalid rating')
        return errors

    def create_quote(self, clean_data, user_id):
        # retrive or create author
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])
        # retirive or create book
        the_book = None
        if not Book.objects.filter(title=clean_data['title']):
            the_book = Book.objects.create(
                title=clean_data['title'], author=the_author
            )
        else:
            the_book = Book.objects.get(title=clean_data['title'])
        # returns a Quote object
        return self.create(
            quote = clean_data['quote'],
            rating = clean_data['rating'],
            book = the_book,
            quoter = User.objects.get(id=user_id)
        )

    def recent_and_not(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent quotes, and the first index
        containing the rest
        '''
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Quote(models.Model):
    quote = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="quotes")
    quoter = models.ForeignKey(User, related_name="quotes_left")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = QuoteManager()
    def __str__(self):
        return "Book: {}".format(self.book.title)