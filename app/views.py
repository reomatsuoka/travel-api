from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms import SearchForm

class IndexView(LoginRequiredMixin, View):
    # template_name = "app/index.html"
    login_url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'app/index.html', {
            'form': form,
        })
