from django.shortcuts import render


def index(request):
    return render(request, 'oc_lettings_site/index.html')


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    return render(request, 'errors/500.html', status=500)
