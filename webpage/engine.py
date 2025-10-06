from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/enviar-denuncia', methods=['POST'])
def enviar_denuncia():
    data = request.json
    report = data.get("report")
    email = data.get("email")
    nome = data.get("nome")
    serie = data.get("serie")

    if not report:
        return jsonify({"error": "O campo 'report' é obrigatório"}), 400

    doc_ref = db.collection("denuncias").add({
        "report": report,
        "email": email,
        "nome": nome,
        "serie": serie,
        "timestamp": datetime.datetime.now()
    })

    return jsonify({"success": True, "id": doc_ref[1].id})

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('/webpage/index.html')
if __name__ == '__main__':
    app.run()