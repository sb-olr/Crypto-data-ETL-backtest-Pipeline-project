from flask import Flask, request, abort
import os
import git
import hmac
import hashlib
from icecream import ic
import my_db_utils
import json

app = Flask(__name__)

try:
    w_secret = os.environ['SECRET_TOKEN']
except:
    ic("ignore on dev server:")
    ic("SECRET_TOKEN for github actions not found in environment")

@app.route('/')
def hello():
    return 'hello world'


@app.route('/api/view/<string:table_name>')
def view_table(table_name):
    db_name='data/TEST-crypto-db.sqlite3'
    data = my_db_utils.get_all_records(db_name, table_name)
    return json.dumps(data)
























### for auto update of code from Github; webhook
def is_valid_signature(x_hub_signature, data, private_key):
    # x_hub_signature and data are from the webhook payload
    # private key is your webhook secret
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)


@app.route('/git_pull', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return '<h1>Method not supported</h1><p>use POST! </p>', 403

    # First check credentials
    x_hub_signature = request.headers.get('X-Hub-Signature')
    if not is_valid_signature(x_hub_signature, request.data, w_secret):
        print('Deploy signature failed: {sig}'.format(sig=x_hub_signature))
        abort(418)

    if request.method == 'POST':
        repo = git.Repo('/home/mailsuj/Crypto')
        origin = repo.remotes.origin
        origin.pull()
        return 'Done', 200
    else:
        return '<h1>Method not supported</h1><p>use POST! </p>', 403


if __name__ == '__main__':
    app.run(debug=True)
