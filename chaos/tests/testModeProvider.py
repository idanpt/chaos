from django.test import TestCase
from chaos.ModeProvider import ModeProvider


class ModeTestCase(TestCase):
    codes = [200, 401, 500]
    provider = False

    def setUp(self):
        self.provider = ModeProvider()

    def test_activate_mode(self):
        new_mode_name = 'some new mode'

        self.provider.activate_mode(new_mode_name)

        new_mode = self.provider.get_active_mode()

        self.assertEqual(new_mode_name, str(new_mode))
        self.assertTrue(new_mode.is_active)


    def test_get_max_percentage_by_code(self):
        self.provider.activate_mode('normal')
        self.assertEqual(self.provider.get_max_percentage_by_code(200), 100)

        self.provider.activate_mode('degraded')
        self.assertEqual(self.provider.get_max_percentage_by_code(200), 50)





