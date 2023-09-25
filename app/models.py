from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
class Genero(models.Model):
     nome = models.CharField(max_length=50)
     def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editora = models.ForeignKey(Editora,on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    preco = models.PositiveBigIntegerField()
    data = models.PositiveBigIntegerField()
    publicacao = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.autor} {self.editora} {self.genero} {self.preco} {self.data} {self.publicacao}'
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    UF = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} {self.UF}'
    
class Emprestimo(models.Model):
    data_emprestimo = models.CharField(max_length=50)
    livro = models.CharField(max_length=50)
    leitor = models.CharField(max_length=50)
    data_devolucao = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.data_emprestimo} {self.livro} {self.leitor} {self.data_devolucao}'
    
    
class Leitores(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.nome} {self.email} {self.cpf}'
    

