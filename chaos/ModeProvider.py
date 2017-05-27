from chaos.models import Chaos
from chaos.CodeProvider import CodeProvider


class ModeProvider:

    def set_mode(self, mode):
        current_mode = self.get_or_create_mode()
        current_mode.mode = mode
        current_mode.save()

        CodeProvider.delete_registered_codes()

    def get_or_create_mode(self):
        # get mode from DB
        mode = Chaos.objects.filter()[:1]
        # Create initial mode if table is empty
        if not mode:
            mode.append(Chaos(mode='normal').save())

        return mode.get()