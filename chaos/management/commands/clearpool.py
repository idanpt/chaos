from django.core.management.base import BaseCommand

from chaos.management.CodeProvider import CodeProvider


class Command(BaseCommand):
    help = 'Clears response pool'

    def handle(self, *args, **options):

        CodeProvider.delete_registered_codes()
        self.stdout.write('Response pool cleared!')
