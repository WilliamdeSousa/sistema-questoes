from django.contrib import admin

from .models import Questao, Alternativa, Assunto

admin.site.register(Questao)
admin.site.register(Alternativa)
admin.site.register(Assunto)