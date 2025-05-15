from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    Affiche la liste des profils.
    Args:
        request: L'objet de requête HTTP.
    Returns:
        HttpResponse: La réponse HTTP contenant la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche le profil d'un utilisateur spécifique.
    Args:
        request: L'objet de requête HTTP.
        username: Le nom d'utilisateur du profil à afficher.
    Returns:
        HttpResponse: La réponse HTTP contenant le profil de l'utilisateur.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
