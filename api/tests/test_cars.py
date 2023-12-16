from ..db import crud, schemas
from .seed import seeded_cars, seeded_games
from .test_config import client, session


def test_create_car(client, session):
    car_make = "Honda"
    car_model = "NSX Evo"
    car_class = "GT3"

    response = client.post(
        f"/games/{seeded_games[0]['id']}/car",
        json={"make": car_make, "model": car_model, "car_class": car_class},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["make"] == car_make
    assert data["model"] == car_model
    assert data["car_class"] == car_class
    assert "id" in data
    car_id = data["id"]

    car = crud.get_car(session, car_id)
    assert car_id == str(car.id)

    deleted = crud.delete_car(session, car_id)
    assert deleted == 1


def test_get_car(client):
    car = seeded_cars[0]

    response = client.get(f"/cars/{car['id']}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["make"] == car["make"]
    assert data["model"] == car["model"]
    assert data["car_class"] == car["car_class"]
    assert data["id"] == str(car["id"])


def test_get_cars(client):
    n_cars = len(seeded_cars)

    response = client.get("/cars")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == n_cars


def test_delete_car(client, session):
    car = crud.create_car(
        session,
        schemas.CarCreate(make="Audi", model="RS3", car_class="TCR"),
        game_id=seeded_games[0]["id"],
    )

    n_cars_before = len(crud.get_cars(session))

    response = client.delete(f"/cars/{car.id}")
    assert response.status_code == 200
    assert response.json() == 1

    n_cars_after = len(crud.get_cars(session))

    assert n_cars_before == n_cars_after + 1


def test_update_car(client, session):
    new_model = "Brooklands"
    car = crud.create_car(
        session,
        schemas.CarCreate(make="Bentley", model="Continental", car_class="GT3"),
        game_id=seeded_games[0]["id"],
    )

    response = client.patch(f"/cars/{car.id}", json={"model": new_model})
    assert response.status_code == 200, response.text
    data = response.json()

    car = crud.get_car(session, car.id)

    assert data["model"] == new_model
    assert data["make"] == "Bentley"
    assert data["car_class"] == "GT3"
    assert data["id"] == str(car.id)
    assert car.model == new_model
