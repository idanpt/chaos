from django.test import TestCase

from chaos.CodeProvider import CodeProvider
from chaos.ModeProvider import ModeProvider
from chaos.models import ResponseCode


class CodeTestCase(TestCase):
    codes = [200, 401, 500]
    provider = False

    def setUp(self):
        CodeProvider.delete_registered_codes()
        self.provider = CodeProvider()

    def test_calculate_and_register_code(self):
        code = self.provider.calculate_and_register_code(self.codes)

        self.assertIn(code, self.codes)
        self.assertTrue(ResponseCode.objects.filter(code=code).exists())

    def test_get_filtered_response_types(self):

        aggregation = {
            '200': 5,
            '401': 0,
            '500': 0,
        }

        ModeProvider().activate_mode(mode='failure')

        filtered = self.provider.get_filtered_response_types(aggregation=aggregation)

        # In 'failure' mode and given status, filtered response types should be only '500'
        self.assertEqual(['500'], filtered)

    def test_get_codes_aggregation(self):

        self.provider.delete_registered_codes()

        ResponseCode(code=200).save()
        ResponseCode(code=200).save()
        ResponseCode(code=401).save()

        self.assertEqual(
            {
                '200': 2,
                '401': 1,
                '500': 0,
            },
            self.provider.get_codes_aggregation()
        )





