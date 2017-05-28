from django.core.management.base import BaseCommand
from collections import Counter
from django.http import HttpResponse
from chaos.CodeProvider import CodeProvider


class Command(BaseCommand):
    help = 'Makes 100 requests to Chaos Responder and outputs the results'

    def handle(self, *args, **options):

        CodeProvider.delete_registered_codes()

        responses = []
        results = {}
        for i in range(100):
            responses.append(
                HttpResponse(status=CodeProvider().calculate_and_register_code()).status_code
            )

        for code, count in Counter(responses).items():
            results[code] = str(count) + '%'

        self.stdout.write('Status Code results: \n' + str(results))
        self.stdout.write('Status Codes received: \n' + str(responses))
