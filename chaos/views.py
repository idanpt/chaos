from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from chaos.CodeProvider import CodeProvider
from chaos.ModeProvider import ModeProvider


def response(request):
    code_provider = CodeProvider()
    types = code_provider.get_filtered_response_types(
        code_provider.get_codes_aggregation()
    )

    return HttpResponse(status=code_provider.calculate_and_register_code(types))


def select(request):
    context = {
        'current_mode': ModeProvider.get_active_mode(),
        'choices': CodeProvider.possible_choices
    }

    return render(request, 'chaos/select.html', context)


def set_mode(request):
    ModeProvider().activate_mode(request.POST['mode'])
    CodeProvider.delete_registered_codes()

    return HttpResponseRedirect(reverse('chaos:select'))