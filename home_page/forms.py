from .models import About
from bootstrap_modal_forms.forms import BSModalForm


class AboutForm(BSModalForm):
    class Meta:
        model = About
        fields = ['about_me']