from django.db import models

# Create your models here.
class pestinfo:
    def __init__(self, id, name, short_description, full_description, image_url):
        self.id = id
        self.name = name
        self.short_description = short_description
        self.full_description = full_description
        self.image_url = image_url
