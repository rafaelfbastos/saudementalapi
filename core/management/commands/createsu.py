# script_criar_superusuario.py
import os
from django.contrib.auth.models import User

def criar_superusuario():
    username = os.getenv('SUPER_USER', 'change-me'),
    email = os.getenv('SUPER_USER_EMAIL', 'change-me')
    password = os.getenv('SUPER_USER_PASSWORD', 'change-me')

    # Verifique se o superusuário já existe
    if not User.objects.filter(username=username).exists():
        # Crie o superusuário
        User.objects.create_superuser(username, email, password)
        print(f'Superusuário {username} criado com sucesso!')
    else:
        print(f'Superusuário {username} já existe.')

if __name__ == '__main__':
    criar_superusuario()


