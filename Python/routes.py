from models.user import User
from database import db

#Flask To-Do-List
List = []

#Create task
@app.route('/create-task', method="POST")
def Create_task():
    return True

@app.route('/search-task', method="GET")
def search_task():
    return True

@app.route('/update-task', method="UPDATE")
def update_task():
    return True

@app.route('/delete-task', method="DELETE")
def delete_task():
    return True