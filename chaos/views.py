from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from chaos.CodeProvider import CodeProvider
from chaos.ModeProvider import ModeProvider


def response(request):
    return HttpResponse(status=CodeProvider().calculate_and_register_code())


def select(request):
    context = {
        'current_mode': ModeProvider.get_active_mode(),
        'choices': CodeProvider.possible_choices
    }

    return render(request, 'chaos/select.html', context)


def set_mode(request):
    ModeProvider().set_mode(request.POST['mode'])
    return HttpResponseRedirect(reverse('chaos:select'))