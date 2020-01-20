from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

import logging

from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm
from .models import Book

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('book_manag:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class BookmListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'bookm_list.html'

    def get_queryset(self):
        diaries = Book.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries