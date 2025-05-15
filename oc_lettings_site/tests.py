import pytest
from django.urls import reverse, resolve


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
