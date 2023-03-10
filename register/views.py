from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm


# Create your views here.
def login_view(req):
    if req.method == 'POST':
        form = UserLoginForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('')
    else:
        form = UserLoginForm()

    return render(req, 'login.html', {'form': form})


class LoginView(View):
    template_name = 'login.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('Home')
        message = 'Неверный логин или пароль!'
        return render(request, self.template_name, context={'form': form, 'message': message})


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('Login')


def user_logout(req):
    logout(req)
    return redirect('Login')


"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__html__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__',
  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
   '__weakref__', '_bound_fields_cache', '_bound_items', '_clean_fields', '_clean_form', '_errors', '_html_output', '_post_clean',
    '_widget_data_value', 'add_error', 'add_initial_prefix', 'add_prefix', 'as_div', 'as_p', 'as_table', 'as_ul', 'auto_id', 'base_fields',
     'changed_data', 'clean', 'confirm_login_allowed', 'data', 'declared_fields', 'default_renderer', 'empty_permitted', 'error_class',
      'error_messages', 'errors', 'field_order', 'fields', 'files', 'full_clean', 'get_context', 'get_initial_for_field', 'get_invalid_login_error',
       'get_user', 'has_changed', 'has_error', 'hidden_fields', 'initial', 'is_bound', 'is_multipart', 'is_valid', 'label_suffix', 'media',
        'non_field_errors', 'order_fields', 'prefix', 'render', 'renderer', 'request', 'template_name', 'template_name_div', 'template_name_label',
         'template_name_p', 'template_name_table', 'template_name_ul', 'use_required_attribute', 'user_cache', 'username_field', 'visible_fields']

"""
