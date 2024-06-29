from django import forms

from .models import Litigation

from clients.models import Customer


class LitigationRegisterForm(forms.ModelForm):
    class Meta:
        model = Litigation

        fields = '__all__'

        widgets = {
            'fruit_pendants': forms.RadioSelect(),
            'batch_disfiguration': forms.RadioSelect(),
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'reception_act': forms.RadioSelect(),
            'purchase_contract': forms.RadioSelect(),
            'social_economic_reform': forms.RadioSelect(),
            'building_titles': forms.Textarea(
                attrs={'class': 'materialize-textarea'}),
            'total_demolition': forms.RadioSelect(),
            'residual_airspace': forms.RadioSelect(),
            'storage_state': forms.RadioSelect(),
            'lease_agreement': forms.RadioSelect(),
            'productive_activities': forms.RadioSelect(),
            'need_transfer_user': forms.RadioSelect(),
            'reclamation_activities': forms.RadioSelect(),
        }

    def clean_origin(self):
        origin = 'web'
        return origin

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            database_email = Customer.objects.get(email__iexact=email)
            if database_email:
                if database_email.is_active:
                    return email
                raise forms.ValidationError("You must confirm your email")
            raise forms.ValidationError("You must register before sending an application")
        raise forms.ValidationError("You must enter your registration email")

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
