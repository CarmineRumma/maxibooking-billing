import pytest
from django.core.urlresolvers import reverse

from billing.lib.test import json_contains
from clients.models import Client
from hotels.models import Country

from ..models import Service


@pytest.mark.django_db
def test_service_period_days():
    service = Service.objects.get(pk=1)
    assert service.period_days == 93
    service.period = 5
    service.save()
    assert service.period_days == 155


@pytest.mark.django_db
def test_service_get_price():
    service = Service.objects.get(pk=1)
    assert service.get_price() == 12332.00
    assert service.get_price(client=1) == 2300.00
    assert service.get_price(client=9999) == 12332.00
    assert service.get_price(country=2) == 234234.00
    assert service.get_price(country=93434) == 12332.00
    assert service.get_price(country='ad') == 2300.00
    assert service.get_price(country=Country.objects.get(pk=1)) == 2300.00
    assert service.get_price(client=Client.objects.get(pk=1)) == 2300.00


def test_services_list_by_user(client):
    response = client.get(reverse('service-list'))
    assert response.status_code == 401


def test_service_list_by_admin(admin_client):
    response = admin_client.get(reverse('service-list'))
    assert response.status_code == 200
    assert len(response.json()['results']) == 3
    json_contains(response, 'Test service three')


def test_service_list_by_admin_ru(admin_client, settings):
    settings.LANGUAGE_CODE = 'ru'
    response = admin_client.get(reverse('service-list'))
    assert response.status_code == 200
    assert len(response.json()['results']) == 3
    json_contains(response, 'Описание тестового сервиса 2')


def test_service_display_by_admin(admin_client):
    response = admin_client.get(reverse('service-detail', args=[1]))
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['title'] == 'Test service one'
    assert response_json['price'] == 12332.00


def test_service_display_by_user(client):
    response = client.get(reverse('service-detail', args=[2]))
    assert response.status_code == 401


def test_service_price_by_admin(admin_client):
    response = admin_client.get(
        reverse('service-price', args=[1]) + '?country=ad')
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['price'] == 2300.00


def test_service_price_by_client(client):
    response = client.get(reverse('service-price', args=[1]) + '?country=ad')
    assert response.status_code == 401
