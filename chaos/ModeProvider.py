from chaos.models import Chaos
from chaos.CodeProvider import CodeProvider


class ModeProvider:

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