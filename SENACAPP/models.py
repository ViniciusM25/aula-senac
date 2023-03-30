from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length = 200)
    def __str__(self):
        return self.nome





class Animal(models.Model):


    nome = models.CharField(max_length = 200)
    peso= models.TextField()
    altura = models.CharField(max_length = 200)
    descricao = models.CharField(max_length = 200)
    imagem = models.ImageField(upload_to = 'img', blank = True, null = True)



    def __str__(self):
        return self.nome
    


    