import random
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/inventory/<item_id>', methods=['GET'])
def get_inventory(item_id):
    qty = random.randint(0, 1000)
    print("GET <id: {}> Returns qty={}".format(item_id, qty))
    return jsonify(itemId=item_id, qty=qty)
