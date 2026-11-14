from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Task Management API"
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or not data.get('title'):
        return jsonify({"error": "Task title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": False
    }

    tasks.append(task)

    return jsonify(task), 201

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
