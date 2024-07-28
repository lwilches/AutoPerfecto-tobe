from flask import Flask, request, jsonify
import requests
from  src.config.manager_env import manager_env 

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({'error': 'Token is missing or invalid'}), 401

        token = token.split(" ")[1]  
        auth_url = manager_env.url_users

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(auth_url, headers=headers)
        
        if response.status_code != 200:
            return jsonify({'error': 'Token is invalid or expired'}), 401
        
        return f(*args, **kwargs)
    return decorator