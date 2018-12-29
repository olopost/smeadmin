#! /bin/env python

# Utilisation de trois fichiers :
# entete.txt pour le nom de l émetteur
# dest.txt le destinataire
# base.txt contenu

def main():
    from reportlab.lib.units import mm
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT

    doc = SimpleDocTemplate("letter.pdf", pagesize=A4)

    Env = []

    with open("entete.txt") as entete:
        mystyle = getSampleStyleSheet()
        right = ParagraphStyle(name='Justify', alignment=TA_LEFT, leftIndent=300, parent=mystyle['Normal'])
        Env.append(Paragraph(entete.read().replace('\n', '<br/>'), right))
        Env.append(Spacer(1, 3 * mm))
        mystyle = getSampleStyleSheet()
        right = ParagraphStyle(name='Justify', alignment=TA_LEFT, leftIndent=300, parent=mystyle['Normal'])
        from datetime import datetime
        t = datetime.now()
        import locale
        locale.setlocale(locale.LC_ALL, "fr_FR")
        Env.append(Paragraph("À Saint-Cyr-L'École, le " + t.strftime("%a %d %b %Y"), right))
        Env.append(Spacer(1, 12 * mm))
    with open("dest.txt") as entete:
        mystyle = getSampleStyleSheet()
        dest = ParagraphStyle(name='Justify', alignment=TA_LEFT, leftIndent=20 * mm, parent=mystyle['Normal'])
        Env.append(Paragraph("À l'attention de : " + entete.read().replace('\n', '<br/>'), dest))
        Env.append(Spacer(1, 12 * mm))


    with open("base.txt") as entete:
        mystyle = getSampleStyleSheet()
        base = ParagraphStyle(name='Base', alignment=TA_JUSTIFY, leftIndent=0, parent=mystyle['Normal'])
        Env.append(Paragraph(entete.read().replace('\n', '<br/>'), base))
    doc.build(Env)


if __name__ == "__main__":
    main()
