import pytest
from django.urls import reverse, resolve
from .models import Profile


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser',
        password='testpassword'
    )


@pytest.fixture
def profile(user):
    return Profile.objects.create(
        user=user,
        favorite_city='Test City'
    )


def test_index_url():
    url = reverse('profiles_index')
    assert url == '/profiles/'

    view = resolve(url)
    assert view.func.__name__ == 'index'


def test_profile_url(profile):
    url = reverse('profile', args=[profile.user.username])
    assert url == f'/profiles/{profile.user.username}/'

    view = resolve(url)
    assert view.func.__name__ == 'profile'


@pytest.mark.django_db(transaction=True)
def test_index_view(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Profiles' in str(response.content)
    assert 'profiles/index.html' in [t.name for t in response.templates]


@pytest.mark.django_db(transaction=True)
def test_profile_view(client, profile):
    url = reverse('profile', args=[profile.user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert 'TestUser' in str(response.content)
    assert 'profiles/profile.html' in [t.name for t in response.templates]
