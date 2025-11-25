# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import CustomerUser, EmailVerifiecation

# @receiver(post_save, sender=CustomerUser)
# def _post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         # Create token
#         token_obj = EmailVerifiecation.objects.create(user=instance)

#         # Verification link
#         verify_link = f"http://127.0.0.1:8000/account/verify_email/{token_obj.token}/"
#         print("Verification Link:", verify_link)

#         # Send email
#         send_mail(
#             subject="Verify your email",
#             message=f"Click the link to verify your account:\n{verify_link}",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[instance.email],
#             fail_silently=False,
#         )