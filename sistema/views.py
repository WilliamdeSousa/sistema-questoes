from django.http import Http404
from django.shortcuts import render

from .models import Assunto


def questionario(request, assunto_id):
    try:
        assunto = Assunto.objects.get(id=assunto_id)
    except Assunto.DoesNotExist:
        raise Http404("Assunto invalido")

    lista_questoes = assunto.questoes.all()

    context = {
        "assunto": assunto,
        "lista_questoes": lista_questoes
    }

    return render(request, "questionario.html", context)

def index(request):
    assuntos = Assunto.objects.all().order_by()
    context = {"assuntos": assuntos}
    return render(request, "index.html", context)
