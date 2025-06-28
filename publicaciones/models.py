from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=1000, null=False, blank=False)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} por {self.autor}'
    
class Comentarios(models.Model):
    publicacion = models.ForeignKey(Publicaciones, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentario de {self.autor} en {self.publicacion.titulo}'
