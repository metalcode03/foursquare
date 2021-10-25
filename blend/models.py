import os
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageDraw
from django.db import models
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile


BASE_DIR = Path(__file__).resolve().parent.parent
# Create your models here.


def blend_image(image):
    import numpy as np

    img = Image.open(image)
    img_path = os.path.join(BASE_DIR, 'assets/img/foursquare.jpg')
    img1 = Image.open(img_path)

    if img.height > img.width:
        img = img.crop((0, 0, img.width, img.height / 1.3))
    elif img.width > img.height:
        img = img.crop((img.width / 6, 0, img.width / 1.1, img.height))

    height, width = img.size
    lum_img = Image.new('L', [height, width], 0)

    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0, 0), (height, width)], 0, 360,
                    fill=255, outline="white")
    img_arr = np.array(img)
    lum_img_arr = np.array(lum_img)
    # display = Image.fromarray(lum_img_arr)
    final_img_arr = np.dstack((img_arr, lum_img_arr))
    play = Image.fromarray(final_img_arr)
    play.thumbnail((255, 255), Image.ANTIALIAS)

    img1.paste(play, (60, 440), mask=play)
    thumb_io = BytesIO()
    img1.save(thumb_io, img1.format)
    # image1 = Image.open(image.path)
    image1 = InMemoryUploadedFile(
        thumb_io,
        None, image.name,
        content_type=image.file.content_type,
        size=img.size,
        charset=image.file.charset,
    )
    return image1

class UploadAndBlendImg(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    fileUpload = models.ImageField(upload_to="image/")
    bgUpload = models.ImageField(upload_to="image/bg/", blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        
        inmemory = blend_image(self.fileUpload)
        
        self.bgUpload.save(
            self.fileUpload.name,
            inmemory,
            save=False
        )
        
        super(UploadAndBlendImg, self).save(*args, **kwargs)
        # super().save()

    def __str__(self):
        return self.fileUpload.path

