from django.http import HttpResponse
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
            mail_subject = _('Activation link has been sent to your email id')
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
            response = _('Please confirm your email address to complete the registration')
            return HttpResponse(response)
    else:
        form = RegisterForm()
    return render(request, 'clients/index.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(code=uid)
    except(TypeError, ValueError, OverflowError, Customer.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, _('Your email has been confirmed! You can now make a litigation application.'))
        return redirect('litigation')
        # response = _('Your email has been confirmed! You can now make a litigation application.')
        # return HttpResponse(response)
    else:
        response = _('Activation link is invalid!')
        return HttpResponse(response)







    # def registration(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#
#             form.save()
#             messages.success(request, f"You have been registered")
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = RegisterForm()
#     return render(request, 'clients/index.html', {'form': form})
