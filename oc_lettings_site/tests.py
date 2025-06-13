import pytest
from django.urls import reverse, resolve
from lettings.models import Address, Letting


@pytest.fixture
def address():
    return Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="Test State",
        zip_code=12345,
        country_iso_code="Test ISO Code",
    )


@pytest.fixture
def letting(address):
    return Letting.objects.create(
        title="Test Letting",
        address=address
    )


def test_index_url():
    url = reverse('index')
    assert url == '/'

    view = resolve(url)
    assert view.func.__name__ == 'index'


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Welcome to Holiday Homes' in str(response.content)
    assert 'oc_lettings_site/index.html' in [t.name for t in response.templates]


def test_error_404_view(client):
    url = '/url-non-existante/'
    response = client.get(url)
    assert response.status_code == 404
    assert 'Erreur 404 - Page non trouvée' in response.content.decode('utf-8')
    assert 'errors/404.html' in [t.name for t in response.templates]
