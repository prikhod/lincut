from flask import Flask, jsonify
from flask import request
from config import parse_config
from linkmaker import Storage

app = Flask(__name__)
conf = parse_config('config/config.yaml')
storage = Storage(conf)


@app.route('/make_link', methods=['POST'])
def make_link():
    result, short_link = storage.add(request.data.decode('utf-8'))
    print(request.data.decode('utf-8'))
    return jsonify({'result': short_link if result else result})


@app.route('/get_links', methods=['GET'])
def get_links():
    return jsonify({'result': storage.get_all()})


@app.route('/get_link/<path:short_link>', methods=['GET'])
def get_full_link(short_link):
    result = storage.get(short_link)
    return jsonify({'result': result.decode('utf-8') if result else None})


@app.route('/delete_link/<path:short_link>', methods=['DELETE'])
def delete_link(short_link):
    return jsonify({'result': storage.remove(short_link)})


if __name__ == '__main__':
    app.run()


