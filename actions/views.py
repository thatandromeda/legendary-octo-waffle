import random

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Action

class HomePage(TemplateView):
    model = Action
    template_name = 'actions/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.random_action()
        context['title'] = 'Home'
        return context

    def random_action(self):
        max_id = Action.objects.last().id
        action = None

        while not action:
            pk = random.randint(1, max_id)
            action = Action.objects.filter(pk=pk).first()

        return action