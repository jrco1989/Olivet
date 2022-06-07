from django.db import models

# Create your models here.

class Comments(models.Model):
    email = models.CharField(max_length=40)
    name =  models.CharField(max_length=100)
    comment =  models.TextField()
    ESTADO = (
        (True, 'Resuelto'),
        (False, 'Pendiente'),
    )
    
    estado = models.BooleanField(
        choices=ESTADO,
        default=False,
    )

    class Meta:
        verbose_name_plural = 'comentarios'
