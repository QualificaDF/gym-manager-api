import os
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv # type: ignore

load_dotenv()

def internal_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_recebido = request.headers.get('x-internal-token')
        token_esperado = os.getenv('INTERNAL_API_TOKEN')
        if not token_recebido:
            return jsonify({'error': 'Token não informado'}), 401
        
        if token_recebido != token_esperado:
            return jsonify({'error': 'Token inválido'}), 401
        
        return f(*args, **kwargs)
    
    return decorated