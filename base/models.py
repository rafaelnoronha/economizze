from django.db import models
import uuid


class Base(models.Model):
    uuid = models.UUIDField(
        verbose_name='UUID',
        default=uuid.uuid4,
        unique=True,
        help_text='UUID Código único não sequencial',
    )

    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True,
        help_text='Se o registro está ativo ou não',
    )

    data_cadastro = models.DateField(
        verbose_name='Data do cadastro',
        auto_now_add=True,
        help_text='Data da criação do registro',
    )

    hora_cadastro = models.TimeField(
        verbose_name='Hora do cadastro',
        auto_now_add=True,
        help_text='Hora da criação do registro',
    )

    class Meta:
        abstract = True
