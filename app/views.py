from django.shortcuts import render
from io import BytesIO
import time
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def home(request):
    return render(request, 'app/home.html')


def generate_helloWorld(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello.pdf"'
    p = canvas.Canvas(response)
    p.drawString(30, 750, "Hello World!")
    p.showPage()
    p.save()

    return response


def generate_form(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="form.pdf"'
    p = canvas.Canvas(response)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
    p.drawString(30,750,'OFFICIAL COMMUNIQUE')
    p.drawString(30,735,'OF XYZ INDUSTRIES')
    p.drawString(500,750,"12/12/2010")
    p.line(480,747,580,747)
    p.drawString(275,725,'AMOUNT OWED:')
    p.drawString(500,725,"BDT 5000.00")
    p.line(378,723,580,723)
    p.drawString(30,703,'RECEIVED BY:')
    p.line(120,700,580,700)
    p.drawString(120,703,"Ms. Z")

    p.showPage()
    p.save()

    return response



def generate_letter(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="letter.pdf"'

    doc = SimpleDocTemplate(response,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]
    logo = "static/pylogo.jpg"
    magName = "TOTO"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2023"
    freeGift = "tin foil hat"

    formatted_time = time.ctime()
    full_name = "chottola chotto"
    address_parts = ["chotto St.", "chotto town, chottogram"]

    im = Image(logo, 1*inch, 1*inch)
    Story.append(im)

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '%s' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '%s' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))       
    for part in address_parts:
        ptext = '%s' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))   

    Story.append(Spacer(1, 12))
    ptext = 'Dear %s:' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = 'We would like to welcome you to our subscriber base for %s Magazine! \
            You will receive %s issues at the excellent introductory price of $%s. Please respond by\
            %s to start receiving your subscription and get the following free gift: %s.' % (magName,issueNum,subPrice, limitedDate,freeGift)
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))


    ptext = 'Thank you very much and we look forward to serving you.'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ptext = 'Sincerely,'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))
    ptext = 'Ms. Z'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)

    return response

