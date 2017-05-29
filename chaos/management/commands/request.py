from collections import Counter

from django.core.management.base import BaseCommand
from django.http import HttpResponse

from chaos.management.CodeProvider import CodeProvider
from chaos.management.ModeProvider import ModeProvider


class Command(BaseCommand):
    help = 'Makes 100 requests to Chaos Responder and outputs the results'

    def handle(self, *args, **options):

        code_provider = CodeProvider()
        code_provider.delete_registered_codes()

        responses = []
        results = {}

        for i in range(100):
            types = code_provider.get_filtered_response_types(
                code_provider.get_codes_aggregation()
            )
            responses.append(
                HttpResponse(status=code_provider.calculate_and_register_code(types)).status_code
            )

        for code, count in Counter(responses).items():
            results[code] = str(count) + '%'

        self.stdout.write('Mode: ' + str(ModeProvider.get_active_mode()))
        self.stdout.write('Status Code results: \n' + str(results))
        self.stdout.write('Status Codes received: \n' + str(responses))
