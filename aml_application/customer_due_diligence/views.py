from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.contrib import messages
from django.views import View
from reportlab.lib.pagesizes import letter, A4
from django.conf import settings
import os
from django.templatetags.static import static
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile

from .forms import CustomerDueDiligenceForm, CustomerVerificationForm
from base_app.models import Customer

from reportlab.pdfgen import canvas


class GeneratePDF(View):
    def get(self, request):
        form = MyForm()  # Initialize your form here
        return render(request, 'pdf_form.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data
            # Generate PDF using ReportLab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'

            # Create a PDF canvas and populate it with content
            p = canvas.Canvas(response)
            p.drawString(100, 750, form.cleaned_data['text_field'])
            # Add more content as needed

            p.showPage()
            p.save()
            return response

        return render(request, 'pdf_form.html', {'form': form})


def view_pdf(request):
    # Create a response object for viewing
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="sample.pdf"'

    # Generate the PDF content and add it to the response
    generate_pdf_content(response)

    return response


def download_pdf(request):
    # Create a response object for downloading
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sample.pdf"'

    # Generate the PDF content and add it to the response
    generate_pdf_content(response)

    return response


def generate_pdf_content(response):
    # Create a PDF canvas
    p = canvas.Canvas(response, pagesize=letter)

    # Add content to the PDF
    p.drawString(100, 750, "Hello, World!")
    image_url = 'static/corner.jpg'
    p.drawInlineImage(image_url, 25, 725, 50, 50)

    # Save the PDF
    p.showPage()
    p.save()

    return response


def customer_due_diligence_view(request):
    if request.method == 'POST':
        form = CustomerDueDiligenceForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            if Customer.objects.filter(full_name=full_name, date_of_birth=date_of_birth).exists():
                messages.error(
                    request, 'A customer with that full name and date of birth already exists')
            else:
                form.save()
                messages.success(request, 'Customer added successfully')
                return redirect('/cdd/register')

    else:
        form = CustomerDueDiligenceForm()

    return render(request, 'cddform.html', {'form': form})


def customer_verification_view(request):
    if request.method == 'POST':
        form = CustomerVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            existing_customer = form.cleaned_data['existing_customer']

            if existing_customer:
                # print(existing_customer)
                for field_name, uploaded_file in request.FILES.items():
                    # print("field name:", field_name,
                    #       "uploaded file", uploaded_file)
                    if uploaded_file:
                        # Save the uploaded files to the corresponding fields
                        setattr(existing_customer, field_name, uploaded_file)
                # print('prior to save')
                existing_customer.identity_verified = True
                existing_customer.address_verified = True
                existing_customer.save()
                messages.success(request, 'Customer verified')
                return redirect('/cdd/verify')
            else:
                messages.error(request, 'Please select an existing customer')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = CustomerVerificationForm()

    return render(request, 'cddverification.html', {'form': form})
