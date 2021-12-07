from django.contrib.auth.forms import AuthenticationForm


class MyLoginForm(AuthenticationForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)

       for fieldname in ['username', 'password']:
           self.fields[fieldname].widget.attrs = {'class': 'form-control'}