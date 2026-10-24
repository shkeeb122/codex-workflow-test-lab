from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'ok': True, 'service': 'codex-workflow-test-lab'})


@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello from the test lab'})


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
