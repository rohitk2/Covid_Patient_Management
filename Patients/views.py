from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Patient_Management.models import Patient_Data

def home(request) :
    return render(request, 'Patients/home.html')

def register(request) :
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Patients/register.html', {'form': form})


@login_required
def user_page(request) :
    #get the patient who is logged in
    patient = str(request.user)

    #pull up the user data and data from the sensors
    Patient_user_info = User.objects.values()
    Patient_data = Patient_Data.objects.values()
    #print(Patient_data)
    #print(Patient_user_info)

    #Get the corresponding id for the username
    Patient = [(dict['username'], dict['id']) for dict in Patient_user_info if dict['username'] == patient][0]
    full_data = [data for data in Patient_data if data['patient_id'] == Patient[1]]
    # print(full_data)
    json_full_data = json.dumps(full_data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    # print(json_full_data)
    #input the data in to the html page
    context = {
        'user': Patient[0],
        'full_data': json_full_data
    }
    return render(request, 'Patients/user_page.html', context)
