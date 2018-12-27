
def main():
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas

    canvas = canvas.Canvas('env.pdf')
    canvas.setFont("Helvetica", 10)
    canvas.setPageSize((220 * mm, 110 * mm))
    canvas.drawString(10 * mm, 100 * mm, "Samuel MEYNARD")
    canvas.drawString(10 * mm, 95 * mm, "12E rue MARAT")
    canvas.drawString(10 * mm, 90 * mm, "78210 Saint Cyr L'école")

    canvas.setFont("Helvetica", 12)
    canvas.drawString(130 * mm, 40 * mm, "OVH - Service prélèvement bancaire")
    canvas.drawString(130 * mm, 35 * mm, "2 rue Kellermann")
    canvas.drawString(130 * mm, 30 * mm, "BP 80157")
    canvas.drawString(130 * mm, 25 * mm, "59053 ROUBAIX")

    canvas.save()


if __name__ == "__main__":
    main()
