from flask import request, jsonify, Blueprint
from Python.models.task import Task
from database import db


task_bp =Blueprint('task', '__name__')
#Flask To-Do-List

#Create task
@task_bp.route('/create-task', method="POST")
def Create_task():
    return True

@task_bp.route('/search-task', method="GET")
def search_task():
    return True

@task_bp.route('/update-task', method="UPDATE")
def update_task():
    return True

@task_bp.route('/delete-task', method="DELETE")
def delete_task():
    return True