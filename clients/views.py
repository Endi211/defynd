from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegisterForm
from clients.token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Customer
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = _('Defynd: Activation link has been sent to your email id')
            message = render_to_string('acc_active_email.html', context={
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            response = _('A link has been sent to your email address to complete your registration')
            return HttpResponse(response)
    else:
        form = RegisterForm()
    return render(request, 'clients/index.html', {'form': form})


def activate(request, uidb64, token):
    # Check if activation has already been processed in this session
    if request.session.get('activation_processed', False):
        messages.info(request, _('Your account has been activated. You can now make a litigation application.'))
        logger.info("Activation already processed in this session.")
        return HttpResponseRedirect(reverse('litigation'))

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(code=uid)
    except (TypeError, ValueError, OverflowError, Customer.DoesNotExist) as e:
        user = None
        logger.error(f"Error decoding UID or retrieving user: {e}")

    if user is not None:
        if account_activation_token.check_token(user, token):
            if not user.is_active:
                user.is_active = True
                user.save()
                request.session['activation_processed'] = True
                messages.success(request, _('Your email has been confirmed! You can now make a litigation application.'))
                logger.info(f"User {user.email} activated successfully.")
                return HttpResponseRedirect(reverse('litigation'))
            else:
                messages.info(request, _('Your account is already activated.'))
                logger.info(f"User {user.email} already activated.")
                return HttpResponseRedirect(reverse('litigation'))
        else:
            logger.warning(f"Invalid token for user {user.email}.")
            return HttpResponse(_('Activation link is invalid!'), status=400)
    else:
        logger.warning("User not found.")
        return HttpResponse(_('Activation link is invalid!'), status=400)


