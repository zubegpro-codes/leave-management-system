from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from base.models import  Location, Leaves, CustomUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'address', 'email', 'password1', 'password2', 'nin']

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        
        # Add Bootstrap classes to specific fields
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['nin'].widget.attrs.update({'class': 'form-control'})



class LeaveForm(ModelForm):
    class Meta:
        model = Leaves
        fields = ['user', 'employee_ID', 'email', 'phoneNo', 'position', 'manager', 'manager_email', 'title', 'leave_start', 'leave_end', 'leave_type', 'description']

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)  # Use LeaveForm here
        
        # Add Bootstrap classes to specific fields
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee_ID'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phoneNo'].widget.attrs.update({'class': 'form-control'})
        self.fields['position'].widget.attrs.update({'class': 'form-control'})
        self.fields['manager'].widget.attrs.update({'class': 'form-control'})
        self.fields['manager_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['leave_start'].widget.attrs.update({'class': 'form-control'})
        self.fields['leave_end'].widget.attrs.update({'class': 'form-control'})
        self.fields['leave_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

# class ReportForm(ModelForm):
#     class Meta:
#         model = Report
#         fields= ['user','topic', 'title', 'Rimg', 'description', 'locate']

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio','nin','avatar','phoneNo','address']

