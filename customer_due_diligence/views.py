from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomerDueDiligenceForm, CustomerVerificationForm, CompanyForm
from base_app.models import Customer, Company, Shareholder, Director


@login_required
def customer_due_diligence_view(request):
    # set the companies to only those in the current entity
    companies = Company.objects.filter(entity=request.user.userprofile.entity)

    if request.method == 'POST':
        form = CustomerDueDiligenceForm(
            request.POST, company_choices=companies)
        print(form)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.entity = request.user.userprofile.entity
            if form.cleaned_data['is_director'] == 'Yes' or form.cleaned_data['is_shareholder'] == 'Yes':
                # Set customer.company if condition is met
                customer.company = form.cleaned_data['company']
            else:
                # Clear customer.company if condition is not met
                customer.company = None

            full_name = form.cleaned_data['full_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']

            if Customer.objects.filter(full_name=full_name, date_of_birth=date_of_birth).exists():
                data = {'success': False,
                        'message': "A customer with matching name and date of birth already exists."}
                return JsonResponse(data, status=400)
            elif Customer.objects.filter(email=email,).exists():
                data = {'success': False,
                        'message': "A customer with that email already exists."}
                return JsonResponse(data, status=400)
            else:
                customer.save(update_verification_times=True)
                data = {
                    'success': True,
                    'message': "Customer created successfully",
                }
                # Check if the customer is a director or shareholder
                if form.cleaned_data['is_director'] == 'Yes' or form.cleaned_data['is_shareholder'] == 'Yes':
                    company = customer.company

                    if form.cleaned_data['is_director'] == 'Yes':
                        director = Director(
                            entity=request.user.userprofile.entity,
                            customer=customer,
                            company=company
                        )
                        director.save()

                    if form.cleaned_data['is_shareholder'] == 'Yes':
                        shareholder = Shareholder(
                            entity=request.user.userprofile.entity,
                            customer=customer,
                            company=company
                        )
                        shareholder.save()
                data = {
                    'success': True,
                    'message': "Company created successfully",
                }
                return JsonResponse(data)
        else:
            errors_html = {field: '\n'.join(errors)
                           for field, errors in form.errors.items()}
            data = {'success': False, 'errors_html': errors_html,
                    }
            return JsonResponse(data, status=400)
    else:
        form = CustomerDueDiligenceForm()
        return render(request, 'cddform.html', {'form': form, 'companies': companies, })


@login_required
def customer_verification_view(request):
    existing_customers = Customer.objects.filter(
        entity=request.user.userprofile.entity)
    # for customer in existing_customers:
    #     print(f"Customer ID: {customer.id}, Full Name: {customer.full_name}")

    if request.method == 'POST':
        form = CustomerVerificationForm(
            request.POST, request.FILES, existing_customers=existing_customers)
        # print(request.FILES)

        if form.is_valid():
            existing_customer = form.cleaned_data['existing_customers']
            # print(existing_customer)
            if existing_customer:
                identity_document = request.FILES.get('proof_of_identity')
                address_proof = request.FILES.get('proof_of_address')
                # print(f"Identity: {identity_document}")
                # print(f"Address: {address_proof}")

                if identity_document and address_proof:
                    existing_customer.proof_of_identity = identity_document
                    existing_customer.identity_verified = True
                    existing_customer.proof_of_address = address_proof
                    existing_customer.address_verified = True

                    existing_customer.save(update_verification_times=True)
                    return render(request, 'cdd_form_submitted.html')
                else:
                    messages.error(request, 'Both files must be uploaded.')
            else:
                messages.error(request, 'Please select an existing customer')
        else:
            messages.error(request, 'Check form errors below')
    else:
        form = CustomerVerificationForm()

    return render(request, 'cddverification.html', {'form': form, 'existing_customers': existing_customers})


@login_required
def customer_list_view(request):
    # Retrieve the current entity's customers
    customers = Customer.objects.filter(entity=request.user.userprofile.entity)

    return render(request, 'customer_list.html', {'customers': customers})


@login_required
def update_customer_view(request, customer_id):
    # Retrieve the customer object using the customer_id
    customer = get_object_or_404(Customer, id=customer_id)
    # set the companies to only those in the current entity
    companies = Company.objects.filter(entity=request.user.userprofile.entity)

    if request.method == 'POST':
        # Create a form instance with the POST data and the instance of the customer to be updated
        form = CustomerDueDiligenceForm(request.POST, instance=customer)
        # print(form)

        if form.is_valid():
            updated_customer = form.save(commit=False)
            # Ensure that the entity remains the same
            updated_customer.entity = request.user.userprofile.entity
            if form.cleaned_data['is_director'] == 'Yes' or form.cleaned_data['is_shareholder'] == 'Yes':
                # Set customer.company if condition is met
                updated_customer.company = form.cleaned_data['company']
            else:
                # Clear customer.company if condition is not met
                updated_customer.company = None

            updated_customer.save(update_verification_times=False)

            # Check if the customer is a director or shareholder
            if form.cleaned_data['is_director'] == 'Yes' or form.cleaned_data['is_shareholder'] == 'Yes':
                company = customer.company

                if form.cleaned_data['is_director'] == 'Yes':
                    director = Director(
                        entity=request.user.userprofile.entity,
                        customer=customer,
                        company=company
                    )
                    director.save()

                if form.cleaned_data['is_shareholder'] == 'Yes':
                    shareholder = Shareholder(
                        entity=request.user.userprofile.entity,
                        customer=customer,
                        company=company
                    )
                    shareholder.save()

            # Return JSON response indicating successful update
            data = {
                'success': True,
                'message': "Customer updated",
            }
            return JsonResponse(data)
        else:
            # Return JSON response with form errors
            errors_html = {field: '\n'.join(errors)
                           for field, errors in form.errors.items()}
            data = {'success': False, 'errors_html': errors_html,
                    }
            return JsonResponse(data, status=400)
    else:
        # Create a form instance with the data from the existing customer
        form = CustomerDueDiligenceForm(instance=customer)
        return render(request, 'update_customer.html', {'form': form, 'customer': customer, 'companies': companies})


@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.entity = request.user.userprofile.entity
            company.save()
            data = {
                'success': True,
                'message': "Company created successfully",
            }
            return JsonResponse(data)
        else:
            errors_html = {field: '\n'.join(errors)
                           for field, errors in form.errors.items()}
            data = {'success': False, 'errors_html': errors_html,
                    'message': "Error submitting company"}
            return JsonResponse(data, status=400)
    else:
        form = CompanyForm()
        return render(request, 'company_create_form.html', {'form': form})
