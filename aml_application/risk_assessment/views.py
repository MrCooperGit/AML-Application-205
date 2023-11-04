from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RiskAssessmentForm
from .models import RiskAssessment

# Create your views here.


@login_required
def home(request):
    return render(request, 'risk_assessment/home.html')


@login_required
def risk_assessment_view(request):
    print(request.user.userprofile)

    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            risk_assessment = form.save(commit=False)
            risk_assessment.entity = request.user.userprofile.entity
            risk_assessment.save()
    else:
        form = RiskAssessmentForm()

    return render(request, 'risk_assessment/risk_assessment_template.html', {'form': form})
