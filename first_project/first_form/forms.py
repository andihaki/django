from django import forms
from django.core import validators

# bikin sendiri validator
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('ooops')

class FormName(forms.Form):
    name = forms.CharField()
    # name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="retype email")
    text = forms.CharField(widget=forms.Textarea)

    # hidden field
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)])

    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']

    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("BOT DETECTED!")
        
    #     return bot_catcher


    # buat ngecek, email dan verify_email apa sama?
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("emailnya ga sama")