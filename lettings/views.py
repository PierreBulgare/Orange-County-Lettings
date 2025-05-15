from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Affiche la liste des locations.
    Args:
        request: L'objet de requête HTTP.
    Returns:
        HttpResponse: La réponse HTTP contenant la liste des locations.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.
    Args:
        request: L'objet de requête HTTP.
        letting_id: L'ID de la location à afficher.
    Returns:
        HttpResponse: La réponse HTTP contenant les détails de la location.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
