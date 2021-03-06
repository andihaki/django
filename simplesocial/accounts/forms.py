from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        # isi fields, dateng dari auth
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nama Pengguna'
        self.fields['email'].label = 'Alamat Email'
        self.fields['password1'].label = 'Kata Kunci'
        self.fields['password2'].label = 'Ulangi Kata Kunci'