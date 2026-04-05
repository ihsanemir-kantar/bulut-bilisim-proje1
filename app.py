from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sunucu belleğinde tutulan notlar
notes = [
    {"id": 1, "content": "Bulut Bilisim ders notlarını oku"},
    {"id": 2, "content": "AWS sunucusu başarıyla kuruldu"},
    {"id": 3, "content": "Frontend ve Backend AWS üzerinden haberleşiyor"}
]

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)