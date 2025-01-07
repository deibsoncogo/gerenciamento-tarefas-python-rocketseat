from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
taskIdControl = 1

@app.route("/tasks", methods=["POST"])
def createTask():
  global taskIdControl

  data = request.get_json()

  newTask = Task(
    id=taskIdControl, title=data["title"], description=data.get("description", "")
  )

  taskIdControl += 1

  tasks.append(newTask)

  return jsonify({ "message": "Nova tarefa criada com sucesso" })

@app.route("/tasks", methods=["GET"])
def getTasks():
  taskList = [task.toDict() for task in tasks]

  output = {
    "tasks": taskList,
    "totalTasks": len(taskList)
  }

  return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def getTask(id):
  for task in tasks:
    if task.id == id:
      return jsonify(task.toDict()), 200

  return jsonify({ "message": "Não foi possível encontrar a tarefa"}), 404

if __name__ == "__main__":
  app.run(debug=True)
