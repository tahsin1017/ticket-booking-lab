from fastapi.testclient import TestClient
from main import api, Ticket

client = TestClient(api)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}

def test_add_ticket():
    test_ticket = {
        "id": 1,
        "flight_name": "TK123",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "New York"
    }
    response = client.post("/ticket", json=test_ticket)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["flight_name"] == "TK123"

def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_ticket():
    updated_ticket = {
        "id": 1,
        "flight_name": "TK124",
        "flight_date": "2025-10-15",
        "flight_time": "15:30",
        "destination": "New York"
    }
    response = client.put("/ticket/1", json=updated_ticket)
    assert response.status_code == 200
    assert response.json()["flight_name"] == "TK124"

def test_delete_ticket():
    test_ticket = {
        "id": 2,
        "flight_name": "TK125",
        "flight_date": "2025-10-16",
        "flight_time": "16:30",
        "destination": "London"
    }
    client.post("/ticket", json=test_ticket)
    
    response = client.delete("/ticket/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2
    
    response = client.get("/ticket")
    assert all(ticket["id"] != 2 for ticket in response.json())