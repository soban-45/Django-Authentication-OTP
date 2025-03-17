import random
from django.core.mail import send_mail
from .models import OTP
from django.conf import settings


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email):
    print(email)
    otp = generate_otp()
    OTP.objects.create(email=email, otp_code=otp)

    send_mail(
        'Your OTP Code',
        f'Your OTP is: {otp}',
        settings.EMAIL_HOST_USER, 
        [email]
    )
