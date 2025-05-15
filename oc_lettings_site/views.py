from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site.
    Args:
        request: L'objet de requête HTTP.
    Returns:
        HttpResponse: La réponse HTTP contenant la page d'accueil.
    """
    return render(request, 'oc_lettings_site/index.html')


def error_404(request, exception):
    """
    Gère les erreurs 404 (page non trouvée).
    Args:
        request: L'objet de requête HTTP.
        exception: L'exception levée lors de la tentative d'accès à une page non trouvée.
    Returns:
        HttpResponse: La réponse HTTP contenant la page d'erreur 404.
    """
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    """
    Gère les erreurs 500 (erreur interne du serveur).
    Args:
        request: L'objet de requête HTTP.
    Returns:
        HttpResponse: La réponse HTTP contenant la page d'erreur 500.
    """
    return render(request, 'errors/500.html', status=500)
