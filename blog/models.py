from django.db import models

#CKeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    desc = models.TextField(verbose_name='Descripción')
    content = RichTextField(verbose_name='Contenido')

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de Actualización'
    )

    class Meta:
        verbose_name = 'Publicación'
        verbose_name = 'Publicacione'
        ordering = ['-created']

    def __str__(self):
        return self.title