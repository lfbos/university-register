# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView

from app.forms import LoginForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        professor = getattr(self.request.user, 'professor')
        context.update({
            'professor': professor
        })

        return context


class LoginView(FormView):
    template_name = 'app/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        if form.has_valid_credentials():
            user = authenticate(**data)

            if user is not None:

                if getattr(user, 'professor', None) is None:
                    return render(self.request, self.template_name, context={
                        'form': form,
                        'error': 'El usuario no es un profesor'
                    })

                login(self.request, user)
                return super(LoginView, self).form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={
            'form': form,
            'error': 'Credenciales inválidas, chequee su correo/contraseña'
        })


def sign_out(request):
    logout(request)

    return redirect('login')
