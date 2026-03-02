"""
Simple Flask API demonstrating maintainable design.
Each function is self-contained and clearly documented.
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    """Health check endpoint for system monitoring."""
    return jsonify(status="OK", message="Service running smoothly")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


