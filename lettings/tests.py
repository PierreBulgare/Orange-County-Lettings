import pytest
from django.urls import reverse, resolve
from .models import Letting, Address


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
    url = reverse('lettings_index')
    assert url == '/lettings/'

    view = resolve(url)
    assert view.func.__name__ == 'index'


def test_letting_url():
    url = reverse('letting', args=[1])
    assert url == '/lettings/1/'

    view = resolve(url)
    assert view.func.__name__ == 'letting'


@pytest.mark.django_db(transaction=True)
def test_index_view(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Lettings' in str(response.content)
    assert 'lettings/index.html' in [t.name for t in response.templates]


@pytest.mark.django_db(transaction=True)
def test_letting_view(client, letting):
    url = reverse('letting', args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Test Letting' in str(response.content)
    assert 'lettings/letting.html' in [t.name for t in response.templates]
