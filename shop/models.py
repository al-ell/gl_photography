from django.db import models
from projects.models import Photo, Project


class Category(models.Model):
    """ Category model """
    class Meta:
        verbose_name_plural = 'Categories'

    # Import model from the projects app
    name = models.ForeignKey(Project, blank=True,
                             null=True, on_delete=models.CASCADE)


class Prints(models.Model):
    """ Prints model """
    class Meta:
        verbose_name_plural = 'Prints'
    # import from category model
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.CASCADE)
    # Import model from the projects app
    name = models.ForeignKey(Photo, null=True, blank=True,
                             on_delete=models.CASCADE)
    sku = models.CharField(max_length=150, null=False,
                           unique=True, default="00")
    friendly_name = models.CharField(max_length=200, default="", unique=True)
    image_url = models.URLField(max_length=1024, default="")
    image = models.ImageField(default="")
    description = models.TextField(null=False, default="")
    has_sizes = models.BooleanField(default=True)
    limited_edition = models.BooleanField(default=False, null=False)
    a4_price = models.DecimalField(max_digits=6, decimal_places=2,
                                    default=120.00)
    a5_price = models.DecimalField(max_digits=6, decimal_places=2,
                                    default=80.00)

    # Return price options for different sizes
    def get_price_options(self):
        return [
            ('A5', self.a5_price),
            ('A4', self.a4_price),
        ]

    def __str__(self):
        return self.name.name

    def get_friendly_name(self):
        return self.friendly_name
