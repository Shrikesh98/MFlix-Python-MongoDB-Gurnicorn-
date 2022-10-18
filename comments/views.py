"""A view function is the code you write to respond to requests to your application.
Flask uses patterns to match the incoming request
URL to the view that should handle it. The view returns data that Flask turns into an outgoing response."""
from flask import request

from get_database import get_database
from main import app
from models import Comments

dbname = get_database()


@app.route("/", methods=['GET', 'POST'])
def do_nothing():
    pass


@app.route("/create", methods=['POST'])
def createComment(comment):
    collection_name = dbname["comments"]
    comment = Comments(request.args.get("_id"), request.args.get("name"))
    item_details = collection_name.find()
    for item in item_details:
        print(item)




@app.route("/list", methods=['POST'])
def listComments():
    db_comments = dbname["comments"]
    item_details = db_comments.find()
