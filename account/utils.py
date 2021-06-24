#здесь мы будем создовать метод который будет отпрвлять код активации and и в настройках надо указывать опреде,,,,, метода
from django.core.mail import send_mail

def send_activation_code(email, activation_code):
    #создаем здесь ссылку чтоб пользователь при clicking ссылку активировал свой аккаунт
    activation_url = f'http://localhost:8000/v1/api/account/activate/{activation_code}'
    message = f"""
        Thank you signing up.!
        Please, activate your account.
        Activation link {activation_url}
"""
    send_mail(
       'activate your account',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False

    )