from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Topic, NewsText

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout



app_url="/news/"
def index(request):
    topics = Topic.objects.all()
    return render(request, "index.html", {'topics': topics})

def newstext(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    news_texts = topic.newstext_set.all()  # Получаем все связанные тексты новостей
    return render(request, "newstext.html", {'topic': topic, 'news_texts': news_texts})
def contacts(request):
    return render(request, "contacts.html")

# авторизация и регистрация пользователей
class RegisterFormView(FormView):

    form_class = UserCreationForm

    success_url = app_url + "login/"

    template_name = "reg/register.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

# вход - логирование

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"

    success_url = app_url
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

# для выхода - миниатюрное представление без шаблона -
# после выхода перенаправим на главную
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)

# изменение пароля
class PasswordChangeView(FormView):

    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'

    success_url = app_url + 'login/'
    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)

