from django.shortcuts import render
from .forms import RiskAssessmentForm

# Create your views here.


def home(request):
    return render(request, 'risk_assessment/home.html')


def risk_assessment_view(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            # Process the form data as needed
            form.save()  # This will save the user's responses to the database
    else:
        form = RiskAssessmentForm()

    return render(request, 'risk_assessment/risk_assessment_template.html', {'form': form})
