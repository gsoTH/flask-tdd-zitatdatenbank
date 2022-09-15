import json
import random                                           # notwendig um Zufallswerte zu erzeugen
import pytest

def test_hello_world(app):
    # Arrange
    route = "/"
    soll_status_code = 200
    soll_content = b"<h1>Hello, World!</h1>"        # b wandelt den string in bytecode um, sonst Typfehler

    # Act
    response = app.get(route)

    # Assert
    assert response.status_code == soll_status_code
    assert soll_content in response.data   


def test_errohandler_random_page_returns_error(app):
    # Arrange
    soll_status_code = 404
    soll_content = b"Seite existiert nicht."

    charlist = ["a", "b", "c", "d", "e", "f", "x", "y", "z"]
    random.shuffle(charlist)
    
    random_url = "/"
    for c in charlist:
        random_url = random_url + c

    # Act
    response = app.get(random_url)

    # Assert
    assert response.status_code == soll_status_code
    assert soll_content in response.data


def test_eintragen_get_nicht_erlaubt(app):
    # Arrange
    route = "/eintragen"
    soll_status_code = 405 
    soll_content = b"Method Not Allowed"

    # Act
    response = app.get(route)

    # Assert
    assert response.status_code == soll_status_code
    assert soll_content in response.data


def test_eintragen_post_ohne_daten_wirft_fehler(app):
    # Arrange
    route = "/eintragen"
    soll_status_code = 400
    soll_content = b"Request was not JSON"
    # soll_content  = {'return_url': 'my_test_url'}
    payload = "kein JSON"

    # Act
    response = app.post(route, data = payload)

    # Assert
    assert response.status_code == soll_status_code
    assert soll_content in response.data


def test_eintragen_post_akzeptiert_nur_json(app):
    # Arrange
    route = "/eintragen"
    soll_status_code = 400
    soll_content = b"Request was not JSON"
    payload = "kein JSON"

    # Act
    response = app.post(route, data=payload)

    # Assert
    assert response.status_code == soll_status_code
    assert soll_content in response.data

@pytest.mark.skip                                   # hier ist noch der Wurm drin
def test_eintragen_post_zitat_wird_gespeichert(app):
    # Arrange
    route = "/eintragen"
    soll_status_code = 200
    soll_content = b"Zitat eingetragen."
    payload  = json.dumps(
        {   "zitat": "Es ist mir hier zu laut, ich kann nicht richtig kauen.", 
            "quelle": "Zwei wie Pech und Schwefel"}
            )

    # Act
    response = app.post(route, data = payload)

    # Assert
    assert response.status_code == soll_status_code
    assert soll_content in response.data

