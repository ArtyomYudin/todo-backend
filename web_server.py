from flask import Flask, request
from entry_manager import EntryManager
from resources import Entry

app = Flask(__name__)

FOLDER = '/tmp/'


@app.route('/')
def hello_world():
    return 'Test'


@app.route('/api/entries/')
def get_entries():
    new_list = []
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    for entry in entry_manager.entries:
        new_list.append(entry.json())
    return new_list


@app.route('/api/save_entries/', methods=['POST'])
def save_entries():
    if request.method == 'POST':
        entry_manager = EntryManager(FOLDER)
        req = request.get_json()
        for item in req:
            entry_manager.entries.append(Entry.from_json(item))
        entry_manager.save()
        return {'status': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

    