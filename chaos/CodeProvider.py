import random
from django.db.models import Count
from chaos.models import ResponseCode
from chaos.ModeProvider import ModeProvider


class CodeProvider:

    possible_choices = ['normal', 'degraded', 'failure']
    response_types = [200, 401, 500]

    def calculate_and_register_code(self, filtered_types):
        if not filtered_types:
            raise Exception('Response pool is full, run "manage.py clearpool" to clear it')

        code = random.choice(filtered_types)

        # add new code to DB
        ResponseCode(code=code).save()

        return code

    def get_filtered_response_types(self, aggregation):
        mode_provider = ModeProvider()
        filtered_codes = []

        # Remove codes that code__count exceeds percentage limit
        for code, count in aggregation.items():
            percentage_limit = mode_provider.get_max_percentage_by_code(code)

            if count < percentage_limit:
                filtered_codes.append(code)

        return filtered_codes

    def get_codes_aggregation(self):
        aggregations = ResponseCode.objects.all().values('code').annotate(Count('code'))

        # Pre-fill dictionary with all code types set to 0
        result = dict((str(type),0) for type in self.response_types)

        for code in aggregations:
            result[str(code['code'])] = code['code__count']

        return result

    @staticmethod
    def delete_registered_codes():
        ResponseCode.objects.all().delete()
