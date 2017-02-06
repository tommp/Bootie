from django.shortcuts import render
from django.views.generic import ListView
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta

from paddleusers.models import Position


class BoardView(ListView):
    template_name = 'board_page.html'
    queryset = Position.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['board_positions'] = Position.objects.all().order_by('priority')
        return context
