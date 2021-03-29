from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Resultado(models.Model):
    eixoEconomico_resultado = models.FloatField()
    eixoSocial_resultado = models.FloatField()
    eixoDiplomatico_resultado = models.FloatField()
    eixoCivil_resultado = models.FloatField()
    usuario_resultado = models.ForeignKey(User, on_delete=models.CASCADE)
    data_resultado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resultados'

    def __str__(self):
        return str(self.usuario_resultado)


class Disciplina(models.Model):
    nome_disc = models.CharField(max_length=80)

    class Meta:
        db_table = 'disciplina'

    def __str__(self):
        return self.nome_disc


class Sala(models.Model):
    nome_sala = models.CharField(max_length=80)
    adm_sala = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo_sala = models.CharField(max_length=255)
    codigo_sala = models.CharField(max_length=10)
    desc_sala = models.TextField()
    jogo_sala = models.IntegerField(default=0)
    visibilidade_sala = models.BooleanField(default=True)
    disciplina = models.ManyToManyField(Disciplina)

    class Meta:
        db_table = 'sala'

    def __str__(self):
        return self.nome_sala

class Alunos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    class Meta:
        db_table = 'alunos'

    def __str__(self):
        return str(self.usuario)

    def get_sala(self):
        return self.sala


class Mensagem(models.Model):
    usuario_mensagem = models.ForeignKey(User, on_delete=models.CASCADE)
    sala_mensagem = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data_mensagem = models.DateTimeField(auto_now=True)
    texto_mensagem = models.TextField()

    class Meta:
        db_table = 'mensagem'

    def __str__(self):
        return self.usuario_mensagem


class Conquista(models.Model):
    nome_conquista = models.CharField(max_length=80)
    desc_conquista = models.TextField()
    usuario_conquista = models.ManyToManyField(User)

    class Meta:
        db_table = 'conquista'

    def __str__(self):
        return self.nome_conquista
