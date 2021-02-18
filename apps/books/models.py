from django.db import models

# Create your models here.
class Book(models.Model):
    """Model definition for Book."""

    # TODO: Define fields here

    title = models.CharField("Titulo", max_length=50)
    description = models.TextField("Descripción")

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return str(self.id) + ".- " + str(self.title)
