import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"
tasks = []

def testCreateTask():
  data = {
    "title": "Estudar Python",
    "description": "APIs com Flask"
  }

  response = requests.post(f"{BASE_URL}/tasks", json=data)
  responseJson = response.json()

  tasks.append(responseJson["id"])

  assert response.status_code == 201
  assert "message" in responseJson
  assert "id" in responseJson
