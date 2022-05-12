from django import forms


from iletisim.models import Contact


class contactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields='__all__'
"""
class kariyerForm(forms.ModelForm):
    class Meta:
        model = kariyer
        fields='__all__'
        
        """