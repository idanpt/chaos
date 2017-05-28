import os
import sys
from django.core.exceptions import ObjectDoesNotExist

from chaos.models import Mode
import json


class ModeProvider:

    modes_json_path = 'modes.json'

    def activate_mode(self, mode):

        self.deactivate_all_modes()

        new_mode = self.get_or_create_by_name(mode)
        new_mode.is_active = True
        new_mode.save()

    def get_max_percentage_by_code(self, code):
        options = self.get_modes_options()
        active_mode = self.get_active_mode()

        return options[str(active_mode)][str(code)]

    @staticmethod
    def get_modes_options():
        return json.load(open(os.path.join(sys.path[0], 'static/modes.json')))

    @staticmethod
    def get_active_mode():
        try:
            return Mode.objects.filter(is_active=True)[:1].get()
        except ObjectDoesNotExist:
            # No active mode, raise exception
            raise Exception('No active mode is set. go to /select to activate one')

    @staticmethod
    def deactivate_all_modes():
        Mode.objects.all().update(is_active=False)

    @staticmethod
    def get_or_create_by_name(mode_name):
        try:
            mode = Mode.objects.filter(mode=mode_name)[:1].get()
        except ObjectDoesNotExist:
            mode = Mode(mode=mode_name, is_active=False).save()

        return mode