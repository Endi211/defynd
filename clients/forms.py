from django import forms

from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = [
            'customer_type', 'name', 'email', 'phone', 'mobile', 'vat_number', 'fiscal_code', 'company_name',
            'role', 'street', 'city', 'post_number', 'birthday', 'birth_place', 'gender', 'last_name', 'origin',
            'phone_prefix', 'mobile_prefix'
        ]
        widgets = {
            'gender': forms.RadioSelect(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if models.Customer.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError("User with this email already exists !")
            return email
        raise forms.ValidationError("You need to enter an email !")

    def clean_origin(self):
        origin = 'web'
        return origin

    def MonkeyPatchDjangoFormsBoundField(self):
        def prepare_widget_render(self, widget=None, attrs=None, only_initial=False):
            """
            Prepare the data needed for the widget rendering.
            """
            if not widget:
                widget = self.field.widget

            attrs = attrs or {}
            auto_id = self.auto_id
            if auto_id and 'id' not in attrs and 'id' not in widget.attrs:
                if not only_initial:
                    attrs['id'] = auto_id
                else:
                    attrs['id'] = self.html_initial_id

            if not only_initial:
                name = self.html_name
            else:
                name = self.html_initial_name

            return widget, name, attrs

        def as_widget(self, widget=None, attrs=None, only_initial=False):
            """
            Renders the field by rendering the passed widget, adding any HTML
            attributes passed as attrs.  If no widget is specified, then the
            field's default widget will be used.
            """
            widget, name, attrs = self.prepare_widget_render(widget, attrs, only_initial)
            return widget.render(name, self.field(), attrs=attrs)

        def __getitem__(self, idx):
            """
            Tries to use current widget's renderer, and then check attribute.
            """
            widget, name, attrs = self.prepare_widget_render()
            try:
                renderer = widget.get_renderer(name, self.field(), attrs=attrs)
                return renderer[idx]
            except Exception:
                return getattr(self, idx)

        forms.forms.BoundField.prepare_widget_render = prepare_widget_render
        forms.forms.BoundField.as_widget = as_widget
        forms.forms.BoundField.__getitem__ = __getitem__
