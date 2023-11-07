from django.shortcuts import render
from django.shortcuts import redirect
from .models import sam
from .models import avf
from .models import mockinterview
from django.contrib.auth import get_user_model
User=get_user_model()
from django.views.generic import CreateView 
# Create your views here.
def home(request):
     context={ "sam":sam.objects.all()}
     return render(request,'sam/sam.html',context)

def avfhome(request):
     context={ "sam":avf.objects.all()}
     return render(request,'sam/avf.html',context)


def avfform(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        courses = request.POST.get('course')
        alum_email = request.POST.get('alum_id')  # Assuming 'alum_id' is the primary key of the Alumni model

        # Check if the 'alum_id_pk' is a valid primary key
        try:
            alum_id = User.objects.get(email=alum_email)
        except User.DoesNotExist:
            # Handle the case where the Alumni instance does not exist
            # You can return an error message or redirect as needed
            return HttpResponse("Invalid Alumni ID")

        # Create a new 'avf' instance with a valid 'alum_id'
        new_avf = avf(branch=branch, courses=courses, alum_id=alum_id)
        new_avf.save()

        # Redirect to a success page or perform further actions
        return redirect('avf-home')

    # Handle GET request and render the form
    
        # Render your form or return an empty form
        # You can also include Alumni data in the form if needed

    return render(request, 'sam/avf_form.html')
 

def mockhome(request):
     context={ "sam":mockinterview.objects.all()}
     return render(request,'sam/mockinterview.html',context)

 