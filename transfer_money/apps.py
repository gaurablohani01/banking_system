from django.apps import AppConfig


class TransferMoneyConfig(AppConfig):
    name = 'transfer_money'

    def ready(self):
        import transfer_money.signals
