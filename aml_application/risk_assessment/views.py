from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import RiskAssessmentForm
from base_app.models import Entity, UserProfile
from .models import RiskAssessment
from xhtml2pdf import pisa

# Create your views here.


@login_required
def home(request):
    return render(request, 'risk_assessment/home.html')


@login_required
def risk_assessment(request):
    entity = Entity.objects.get(id=request.user.userprofile.entity.id)
    entity_name = entity.name
    last_risk_assessment = RiskAssessment.objects.filter(
        entity=entity).latest('date_created')
    user_type1 = UserProfile.objects.get(
        user_type=request.user.userprofile.user_type)

    context = {
        'last_risk_assessment': last_risk_assessment,
        'user_type': user_type1,
        'entity_name': entity_name,
    }

    return render(request, 'risk_assessment/view_risk_assessment.html', {**context})


@login_required
def risk_assessment_view(request):
    entity = Entity.objects.get(id=request.user.userprofile.entity.id)
    last_risk_assessment = RiskAssessment.objects.filter(
        entity=entity).latest('date_created')
    print(last_risk_assessment)
    context = {
        'last_risk_assessment': last_risk_assessment,
    }

    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            risk_assessment = form.save(commit=False)
            risk_assessment.entity = request.user.userprofile.entity
            risk_assessment.save()
            return render(request, 'risk_assessment/form_success.html')
    else:
        form = RiskAssessmentForm()

    return render(request, 'risk_assessment/risk_assessment_template.html', {'context': context, 'form': form})


def render_to_pdf(template_path, context_dict):
    template = get_template(template_path)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="output.pdf"'

    # Create a PDF file
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def pdf_view(request):
    entity = Entity.objects.get(id=request.user.userprofile.entity.id)
    entity_name = entity.name
    last_risk_assessment = RiskAssessment.objects.filter(
        entity=entity).latest('date_created')
    user_type1 = UserProfile.objects.get(
        user_type=request.user.userprofile.user_type)

    context = {
        'last_risk_assessment': last_risk_assessment,
        'user_type': user_type1,
        'entity_name': entity_name,

    }

    # Specify the path to your template
    template_path = 'risk_assessment/view_risk_assessment.html'

    # Render the PDF and return the response
    return render_to_pdf(template_path, context)
