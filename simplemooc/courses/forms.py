from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=35)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida',
        widget=forms.Textarea
    )

    def send_mail(self, course):
        subject = f'Contato sobre o curso {course}'

        context = {
                    'name': self.cleaned_data.get('name'),
                    'email': self.cleaned_data.get('email'),
                    'message': self.cleaned_data.get('message')
        }

        template_name = 'courses/contact_email.html'
        send_mail_template(subject=subject,
                           template_name=template_name,
                           context=context,
                           recipient_list=[settings.CONTACT_MAIL])

