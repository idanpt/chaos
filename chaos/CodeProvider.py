import random
from chaos.models import ResponseCode


class CodeProvider:

    possible_choices = ['normal', 'degraded', 'failure']

    def calc_status_code(self):
        responses = [200, 401, 500]

        return random.choice(responses)

    def delete_registered_codes(self):
        ResponseCode.objects.all().delete()
