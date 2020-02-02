from django.db import models
import datetime as dt


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    FASHION = 'FS'
    MUSIC = 'MS'
    ART = 'AT'
    NATURE = 'NT'
    SHARE_GALLERY = [
        (FASHION, 'Fashion'),
        (MUSIC, 'Music'),
        (NATURE, 'Nature'),
        (ART, 'Art'),
    ]
    category = models.CharField(max_length=2, choices=SHARE_GALLERY, default=FASHION, )

    def is_upperclass(self):
        return self.share_gallery in {self.FASHION, self.ART}


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        pass

    def get_image(self):
        pass

    @classmethod
    def get_image(cls, image_id):
        image = Image.objects.filter(id=image_id)
        

    def __str__(self):
        return self.name
