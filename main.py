import json

from bson import json_util
from flask import Flask, request
from bson.objectid import ObjectId
from get_database import get_database
from models import Comments

app = Flask(__name__)
dbname = get_database()


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/create", methods=['POST'])
def createComment():
    collection_name = dbname["comments"]
    comment = convert_dict_to_comment(request.json)
    print(comment)
    dumps = json.dumps(comment.__dict__)
    item_details = collection_name.insert_one(dumps)
    for item in item_details:
        print(item)


def convert_dict_to_comment(comment_json):
    return Comments(comment_json.get("_id"), comment_json.get("name"),
                    comment_json.get("email"),
                    ObjectId(comment_json.get("movie_id")),
                    comment_json.get("text"))


def parse_json(data):
    return json.loads(json_util.dumps(data))


if __name__ == '__main__':
    app.run()
