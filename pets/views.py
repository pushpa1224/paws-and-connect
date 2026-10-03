from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Pet, Favorite


def pet_list(request):
    pets = Pet.objects.all()

    search = request.GET.get('search', '')
    animal_type = request.GET.get('animal_type', '')
    gender = request.GET.get('gender', '')
    location = request.GET.get('location', '')
    status = request.GET.get('status', '')

    if search:
        pets = pets.filter(name__icontains=search) | pets.filter(breed__icontains=search) | pets.filter(location__icontains=search)
    if animal_type:
        pets = pets.filter(animal_type=animal_type)
    if gender:
        pets = pets.filter(gender=gender)
    if location:
        pets = pets.filter(location__icontains=location)
    if status:
        pets = pets.filter(status=status)

    paginator = Paginator(pets, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    favorite_pet_ids = []
    if request.user.is_authenticated:
        favorite_pet_ids = list(Favorite.objects.filter(user=request.user).values_list('pet_id', flat=True))

    context = {
        'page_obj': page_obj,
        'search': search,
        'animal_type': animal_type,
        'gender': gender,
        'location': location,
        'status': status,
        'animal_type_choices': Pet.ANIMAL_TYPE_CHOICES,
        'favorite_pet_ids': favorite_pet_ids,
    }
    return render(request, 'pets/pet_list.html', context)


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, pet=pet).exists()
    context = {'pet': pet, 'is_favorite': is_favorite}
    return render(request, 'pets/pet_detail.html', context)


@login_required
def toggle_favorite(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    fav, created = Favorite.objects.get_or_create(user=request.user, pet=pet)
    if not created:
        fav.delete()
        messages.success(request, f'Removed {pet.name} from favorites.')
    else:
        messages.success(request, f'Added {pet.name} to favorites.')
    return redirect(request.META.get('HTTP_REFERER', 'pet_list'))


@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('pet')
    return render(request, 'pets/my_favorites.html', {'favorites': favorites})
