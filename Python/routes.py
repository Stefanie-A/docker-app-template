from models.task import TODO
from flask import request, jsonify, Blueprin
from database import db
from app import *


#Flask To-Do-List

#Create task
@todo_bp.route('/create-task', methods="POST")
def Create_task():
    data = request.get_json()
    task = data.get('Task')
    note = data.get('Note')
    date = data.get('Date')

    if task is None and note is None and date is None:
        return jsonify({"Message": "Please enter a task"}), 401
        
    task = TODO (
        Task = task,
        Note = note,
        Date = date
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"Message": "Task successfully created"}), 201

@todo_bp.route('/search-task', methods="GET")
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

@todo_bp.route('/update-task/<int: task_id>', methods="UPDATE")
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

@todo_bp.route('/delete-task/<int: task_id>', methods="DELETE")
def delete_task(task_id):
    task = TODO.query.get(task_id)
    if not task:
        return jsonify({"Error": "Task not found"}), 404
    
    try:
        db.session.delete(task)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({"Error": str(e)}), 400
    
    return True