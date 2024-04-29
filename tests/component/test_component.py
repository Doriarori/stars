import requests

base_url = 'http://localhost:8000'
add_star_url = f'{base_url}/add_star'
list_stars_url = f'{base_url}/stars'
get_star_by_id_url = f'{base_url}/get_star_by_id'
delete_star_url = f'{base_url}/delete_star'

nasa_service_url = 'http://localhost:8001'
apod_url = f'{nasa_service_url}/apod'
neo_url = f'{nasa_service_url}/neo'

new_star = {
    "id": 99,
    "name": "Sun",
    "temperature": 5778,
    "size": 1.0,
    "distance": 0
}


def test_add_star():
    response = requests.post(add_star_url, json=new_star)
    assert response.status_code == 200
    assert response.json()['name'] == "Sun"


def test_get_stars():
    response = requests.get(list_stars_url)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_star_by_id():
    response = requests.get(f"{get_star_by_id_url}/99")
    assert response.status_code == 200
    assert response.json()['id'] == 99


def test_delete_star():

    delete_response = requests.delete(f"{delete_star_url}/99")
    assert delete_response.status_code == 200

    response = requests.get(f"{get_star_by_id_url}/99")
    assert response.status_code == 404

def test_get_astronomy_picture_of_the_day():

    response = requests.get(apod_url)
    assert response.status_code == 200
    data = response.json()
    assert 'url' in data
    assert 'explanation' in data

def test_get_near_earth_objects():

    start_date = "2023-04-01"
    end_date = "2023-04-07"
    response = requests.get(f"{neo_url}?start_date={start_date}&end_date={end_date}")
    assert response.status_code == 200
    data = response.json()
    assert 'near_earth_objects' in data
    assert start_date in data['near_earth_objects']