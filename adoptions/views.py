from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pets.models import Pet
from .models import AdoptionRequest


@login_required
def adoption_form(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if pet.status != 'Available':
        messages.error(request, 'This pet has already been adopted and is no longer available.')
        return redirect('pet_detail', pk=pk)

    existing = AdoptionRequest.objects.filter(user=request.user, pet=pet, status='Pending').exists()
    if existing:
        messages.warning(request, 'You already have a pending adoption request for this pet.')
        return redirect('pet_detail', pk=pk)

    if request.method == 'POST':
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        reason = request.POST.get('reason', '').strip()
        previous_pet_experience = request.POST.get('previous_pet_experience') == 'yes'
        message = request.POST.get('message', '').strip()

        if not phone or not address or not reason:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'adoptions/adoption_form.html', {'pet': pet})

        AdoptionRequest.objects.create(
            user=request.user,
            pet=pet,
            phone=phone,
            address=address,
            reason=reason,
            previous_pet_experience=previous_pet_experience,
            message=message,
        )
        messages.success(request, f'Your adoption request for {pet.name} has been submitted!')
        return redirect('my_requests')

    return render(request, 'adoptions/adoption_form.html', {'pet': pet})


@login_required
def my_requests(request):
    requests_list = AdoptionRequest.objects.filter(user=request.user).select_related('pet')
    return render(request, 'adoptions/my_requests.html', {'requests_list': requests_list})
