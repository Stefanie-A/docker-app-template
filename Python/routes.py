from models.task import TODO
from flask import request, jsonify, Blueprint
from database import db

todo_bp =Blueprint('task', '__name__')
#Flask To-Do-List

@todo_bp.route("/create-task/", methods=["POST"])
def create_task():
    data = request.get_json()
    task = data.get('Task')
    note = data.get('Note')
    date = data.get('Date')

    if task is None or note is None or date is None:
        return jsonify({"error": "Please provide values for 'Task', 'Note', and 'Date'."}), 400
        
    todo = TODO(
        Task=task,
        Note=note,
        Date=date
    )

    db.session.add(todo)
    db.session.commit()

    return jsonify({"message": "Task created successfully."}), 201

@todo_bp.route('/search-task/', methods=["GET"])
def search_task():
    task = TODO.query.all()
    task_search = [ ]

    for tasks in task:
        task_search.append({
            'id': tasks.id,
            'username': tasks.Task,
            'email': tasks.Note,
            'password': tasks.Date
        })
    return jsonify(task_search)

@todo_bp.route("/update-task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task = TODO.query.get(task_id)

    if not task:
        return jsonify({"Error": "Task not found"}), 404
    
    task.task = data.get('Task', task.task)
    task.note = data.get('Note', task.note)
    task.date = data.get('Date', task.date)

    db.session.commit()
    return jsonify({"Messges": "Task updated!"}), 202

@todo_bp.route('/delete-task/<int:task_id>', methods=["DELETE"])
def delete_task(task_id):
    # Query the task by its ID
    task = TODO.query.get(task_id)
    
    # If the task doesn't exist, return a 404 error
    if not task:
        return jsonify({"Error": "Task not found"}), 404
    
    try:
        # Delete the task from the database
        db.session.delete(task)
        db.session.commit()
        
        # Return a success message
        return jsonify({"Message": "Task deleted successfully"}), 200

    except Exception as e:
        # If an error occurs during deletion, rollback the session
        db.session.rollback()
        
        # Return an error message with the details of the exception
        return jsonify({"Error": str(e)}), 500
