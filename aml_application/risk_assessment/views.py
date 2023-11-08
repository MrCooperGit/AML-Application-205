from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RiskAssessmentForm

# Create your views here.


@login_required
def home(request):
    return render(request, 'risk_assessment/home.html')


@login_required
def risk_assessment_view(request):
    print(request.user.userprofile.entity)

    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            risk_assessment = form.save(commit=False)
            risk_assessment.entity = request.user.userprofile.entity
            risk_assessment.save()
            messages.success(request, "Risk assessment submitted successfully")
            return redirect('landing_app:index')
        else:
            messages.error(request, "Form is invalid. Check errors")
            return render(request, 'risk_assessment/risk_assessment_template.html', {'form': form})
    else:
        form = RiskAssessmentForm()

    return render(request, 'risk_assessment/risk_assessment_template.html', {'form': form})
