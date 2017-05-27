from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from chaos.models import ResponseCode
from chaos.CodeProvider import CodeProvider
from chaos.ModeProvider import ModeProvider


def index(request):
    code = CodeProvider().calc_status_code()

    # add new code to DB
    ResponseCode(code=code).save()

    return HttpResponse(status=code)


def select(request):
    context = {
        'current_mode': ModeProvider().get_or_create_mode(),
        'choices': CodeProvider.possible_choices
    }

    return render(request, 'chaos/select.html', context)


def set_mode(request):
    ModeProvider().set_mode(request.POST['mode'])
    return HttpResponseRedirect(reverse('chaos:select'))