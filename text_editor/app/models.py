from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)  # enables image/file buttons
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
