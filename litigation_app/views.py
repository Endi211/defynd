from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .forms import LitigationRegisterForm
from clients.models import Customer
from django.utils.translation import gettext as _
from dotenv import load_dotenv
import os

# Create your views here.

load_dotenv()


def litigation(request):
    if request.method == 'POST':
        form = LitigationRegisterForm(request.POST)
        if form.is_valid():
            litigation_current_app = form.save(commit=False)

            client = Customer.objects.get(email=litigation_current_app.email)
            litigation_current_app.customer = client

            litigation_current_app.save()

            send_mail(
                subject=_("New litigation case"),
                message=_(f'Customer with name ') + f'[C0{client.code}]{client.name} {client.last_name}' + _(' made an application') +
                        _(' with litigation id ') + f'[L0{litigation_current_app.litigation_code}]',
                from_email=os.environ.get("EMAIL_HOST_USER"),
                fail_silently=False,
                auth_user=None,
                recipient_list=[os.environ.get("ADMIN_EMAIL")]
            )

            messages.success(request, _("Your application has been received"))
            return HttpResponseRedirect(request.path_info)
    else:
        form = LitigationRegisterForm()
    return render(request, "litigation_app/index.html", {'form': form})
