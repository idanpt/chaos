import random
from chaos.models import ResponseCode


class CodeProvider:

    possible_choices = ['normal', 'degraded', 'failure']
    response_types = [200, 401, 500]

    def calc_status_code(self):


        return random.choice(self.get_filtered_response_types())


    def get_filtered_response_types(self):
        aggrigation = ResponseCode.objects.all().distinct().count()


    @staticmethod
    def delete_registered_codes():
        ResponseCode.objects.all().delete()
