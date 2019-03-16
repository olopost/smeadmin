from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.conf.urls import url
from django.http import HttpResponse
import logging
import ssl
from .models import CarnetDAdresse
from wagtail.admin.menu import MenuItem

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger('smeadmin')




class CarnetDAdresseAdmin(ModelAdmin):
    """
    Carnet d'adresse - pour la gestion de l'envoi de lettre et de courrier
    """
    model = CarnetDAdresse
    menu_label = "SME - Carnet d'adresse"
    menu_icon = "mail"



class EnveloppeView(TemplateView):
    """
    Letter DL format pdf generation
    """

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
        context['carnet'] = CarnetDAdresse.objects.all()
        return context

    def will_modify_explorer_page_queryset(self):
        return False

    def get_admin_urls_for_registration(self):
        urls = (url(r'^smeadmin/$', EnveloppeView.as_view(), name='view_env'),)
        return urls

    def get_menu_item(self, order=None):
        return MenuItem('SME - Enveloppe', reverse("view_env"), classnames='icon icon-mail', order=10000)





class LettreView(TemplateView):
    """
    Autogenerate letter - French format
    """

    template_name = "letter.html"

    def post(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="letter.pdf"'
        from reportlab.lib.units import mm
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT

        doc = SimpleDocTemplate(response, pagesize=A4)

        Env = []

        entete = request.POST['exp']
        mystyle = getSampleStyleSheet()
        right = ParagraphStyle(name='Justify', alignment=TA_LEFT, leftIndent=300, parent=mystyle['Normal'])
        Env.append(Paragraph(entete.replace('\n', '<br/>'), right))
        Env.append(Spacer(1, 3 * mm))
        right = ParagraphStyle(name='Justify', alignment=TA_LEFT, leftIndent=300, parent=mystyle['Normal'])
        from datetime import datetime
        t = datetime.now()
        import locale
        locale.setlocale(locale.LC_ALL, "fr_FR")
        Env.append(Paragraph("À " + request.POST['loc'] + ", le " + t.strftime("%a %d %b %Y"), right))
        Env.append(Spacer(1, 12 * mm))

        entete = request.POST['dest']
        mystyle = getSampleStyleSheet()
        dest = ParagraphStyle(name='Justify', alignment=TA_LEFT, leftIndent=20 * mm, parent=mystyle['Normal'])
        Env.append(Paragraph("À l'attention de : " + entete.replace('\n', '<br/>'), dest))
        Env.append(Spacer(1, 12 * mm))

        entete = request.POST['base']
        entete = entete.replace('$DEST$', request.POST['dest'])
        mystyle = getSampleStyleSheet()
        base = ParagraphStyle(name='Base', alignment=TA_JUSTIFY, leftIndent=0, parent=mystyle['Normal'])
        Env.append(Paragraph(entete.replace('\n', '<br/>'), base))
        doc.build(Env)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gestion des lettres"
        context['carnet'] = CarnetDAdresse.objects.all()
        return context

    def will_modify_explorer_page_queryset(self):
        return False

    def get_admin_urls_for_registration(self):
        urls = (url(r'^smeadmin-letter/$', LettreView.as_view(), name='view_lettre'),)
        return urls

    def get_menu_item(self, order=None):
        return MenuItem('SME - Lettre', reverse("view_lettre"), classnames='icon icon-edit', order=10000)

class SMEAdminGroup(ModelAdminGroup):
    """
    SME Admin menu
    """
    menu_label = "SMEAdmin"
    items = (CarnetDAdresseAdmin,EnveloppeView, LettreView)

# Register button
modeladmin_register(SMEAdminGroup)

