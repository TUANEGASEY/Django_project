from django.apps import AppConfig


class MeuappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meuapp'
    verbose_name = 'Meu App'

    def ready(self):
        # Aqui você pode registrar sinais, inicializar tarefas em segundo plano, etc.
        # from django.db.models.signals import post_save
        # from django.dispatch import receiver
        # from .models import MeuModelo
        #
        # @receiver(post_save, sender=MeuModelo)
        # def meu_sinal(sender, instance, created, **kwargs):
        #     if created:
        #         print(f'Novo objeto criado: {instance}')
        pass
#
# # URL de redirecionamento após login
# LOGIN_REDIRECT_URL = '/'
# # URL de redirecionamento após logout
# LOGOUT_REDIRECT_URL = '/'
#

