from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
import time
import logging
import ssl
from time import mktime
from django.views.decorators.csrf import csrf_exempt

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger('smeadmin')


@hooks.register('register_admin_menu_item')
def register_menu_item():
  return MenuItem('SME - Enveloppe', reverse("view_env"), classnames='icon icon-mail', order=10000)


class EnveloppeView(TemplateView):

    template_name = "env.html"

    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="env.pdf"'
        from reportlab.lib.units import mm
        from reportlab.pdfgen import canvas
        if 'dest' in request.POST:
            dest = request.POST['dest']
        if 'exp' in request.POST:
            exp = request.POST['exp']
        canvas = canvas.Canvas(response)
        canvas.setFont("Helvetica", 10)
        canvas.setPageSize((220 * mm, 110 * mm))

        index = 100
        for l in exp.splitlines():
            canvas.drawString(10 * mm, index * mm, l)
            index -= 5

        canvas.setFont("Helvetica", 12)
        index = 40
        for l in dest.splitlines():
            canvas.drawString(130 * mm, index * mm, l)
            index -= 5

        canvas.save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestion des enveloppes"
        return context


@hooks.register('register_admin_urls')
def urlconf():
    return [
        url(r'^smeadmin/$', EnveloppeView.as_view(), name='view_env'),
    ]