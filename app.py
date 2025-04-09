# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from OpenShift!"

@app.route('/healthz')
def health():
    # In a real app, you'd check database connections, etc.
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
