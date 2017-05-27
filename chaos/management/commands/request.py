from django.core.management.base import BaseCommand
from urllib.request import urlopen
from pprint import pprint
from collections import Counter


class Command(BaseCommand):
    help = 'Makes 100 requests to Chaos Responder and outputs the results'

    def handle(self, *args, **options):
        responses = []

        for i in range(5):
            responses.append(
                urlopen('http://localhost:8000/chaos').status
            )

        pprint(responses)
        self.stdout.write('Codes counts: ' + str(Counter(responses).items()))
