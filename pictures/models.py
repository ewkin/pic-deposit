from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Picture(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    small_picture = ImageSpecField(source='picture',
                                      processors=[ResizeToFill(480, 220)],
                                      format='JPEG',
                                      options={'quality': 60})
    description = models.TextField()

    def __str__(self):
        return self.title
#
# pic = Picture.objects.all()[0]
# print(pic.small_picture.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
# print(pic.small_picture.width) # > 100

