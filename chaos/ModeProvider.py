import os

import sys

from chaos import CodeProvider
from chaos.models import Chaos
import json


class ModeProvider:

    modes_json_path = 'modes.json'

    def set_mode(self, mode):
        # Deactivate current mode
        current_mode = self.get_active_mode()
        current_mode.is_active = False
        current_mode.save()

        # Activate new mode
        new_mode = self.get_by_name(mode)
        new_mode.is_active = True
        new_mode.save()

        # Reset codes calculation
        CodeProvider.delete_registered_codes()

    @staticmethod
    def get_active_mode():
        return Chaos.objects.filter(is_active=True)[:1].get()

    @staticmethod
    def get_by_name(mode):
        return Chaos.objects.filter(mode=mode)[:1].get()

    def get_percentage_by_code(self, code):
        options = self.get_mode_options()
        active_mode = self.get_active_mode()

        return options[str(active_mode)][str(code)]

    def get_mode_options(self):
        return json.load(open(os.path.join(sys.path[0], 'static/modes.json')))