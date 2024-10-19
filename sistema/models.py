from django.db import models

class Assunto(models.Model):
    assunto = models.CharField(max_length=100)

    def __str__(self):
        return self.assunto

class Questao(models.Model):
    enunciado = models.CharField(max_length=300)
    assunto = models.ForeignKey(Assunto, related_name='questoes', on_delete=models.SET_NULL, null=True)
    solucao = models.TextField(max_length=1000)

    def __str__(self):
        return self.enunciado

class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, related_name='alternativas', on_delete=models.CASCADE)
    alternativa = models.CharField(max_length=200)

    def __str__(self):
        return self.alternativa

class MultiplaEscolha(Questao):

    def __str__(self):
        return self.enunciado

class VerdadeiroOuFalso(Questao):
    pass