from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RiskAssessmentForm
from base_app.models import Entity
from .models import RiskAssessment

# Create your views here.


@login_required
def home(request):
    return render(request, 'risk_assessment/home.html')


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

    return render(request, 'risk_assessment/risk_assessment_template.html', {**context, **form})
