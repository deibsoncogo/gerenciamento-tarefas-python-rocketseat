import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

def testCreateTask():
  data = {
    "title": "Title",
    "description": "Description"
  }

  response = requests.post(f"{BASE_URL}/tasks", json=data)
  responseJson = response.json()

  tasks.append(responseJson["id"])

  assert response.status_code == 201
  assert "message" in responseJson
  assert "id" in responseJson

def testGetTasks():
  response = requests.get(f"{BASE_URL}/tasks")
  responseJson = response.json()

  assert response.status_code == 200
  assert "tasks" in responseJson
  assert "totalTasks" in responseJson

def testGetTask():
  response = requests.get(f"{BASE_URL}/tasks/{tasks[0]}")
  responseJson = response.json()

  assert response.status_code == 200
  assert tasks[0] == responseJson["id"]

def testUpdateTask():
  data = {
    "title": "Title Test Update",
    "description": "Description Test Update",
    "completed": True
  }

  response = requests.put(f"{BASE_URL}/tasks/{tasks[0]}", json=data)

  assert response.status_code == 204

def testDeleteTask():
  response = requests.delete(f"{BASE_URL}/tasks/{tasks[0]}")
  responseJson = response.json()

  assert response.status_code == 205
  assert "message" in responseJson
