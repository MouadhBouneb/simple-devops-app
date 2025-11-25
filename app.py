"""
Simple Flask Application - Sample DevOps Project
"""
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configuration
app.config['VERSION'] = os.getenv('APP_VERSION', '1.0.0')
app.config['ENVIRONMENT'] = os.getenv('ENVIRONMENT', 'development')


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Sample DevOps App',
        'version': app.config['VERSION'],
        'environment': app.config['ENVIRONMENT']
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': app.config['VERSION']
    }), 200


@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
    ]
    return jsonify(users), 200


@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    
    user = {
        'id': 3,
        'name': data['name'],
        'email': data['email']
    }
    return jsonify(user), 201


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    if user_id == 1:
        return jsonify({'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}), 200
    elif user_id == 2:
        return jsonify({'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

