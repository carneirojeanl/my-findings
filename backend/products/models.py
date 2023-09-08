from django.db import models


class Product(models.Model):
    TECH = 'TECH'
    EBOOK = 'EBOOK'
    ONLINE_COURSE = 'ON_COURSE'
    OTHER = 'OTHER'
    CATEGORIES = (
        (TECH, "Tech"),
        (EBOOK, "Ebook"),
        (ONLINE_COURSE, "Online Course"),
        (OTHER, "Other"),
    )

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    content = models.TextField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default=OTHER)
    link = models.URLField(max_length=300)
    # upload_to: pictures meaning storing the images uploaded inside the media/pictures folder in the root folder
    # of the project.
    picture = models.ImageField(upload_to='pictures', null=True, blank=True)




