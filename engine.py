from flask import Flask, jsonify, request, render_template
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/enviar_denuncia', methods=['POST', 'GET'])
def enviar_denuncia():
    print("Form submitted!")

    data = request.get_data
    report = data.get("report-ocorrido")
    email = data.get("report-email")
    nome = data.get("report-nome")
    serie = data.get("report-serie")

    if not report:
        return jsonify({"error": "O campo 'report' é obrigatório"}), 400

    doc_ref = db.collection("denuncias").add({
        "report": report,
        "email": email,
        "nome": nome,
        "serie": serie,
        "timestamp": datetime.datetime.utcnow()
    })

    return jsonify({"success": True, "id": doc_ref[1].id})

@app.route('/enviar_contato', methods=['POST', 'GET'])
def enviar_contato():
    print("Form submitted!")

    data = request.get_data
    nome = data.get("nome")
    email = data.get("email")
    mensagem = data.get("mensagem")
    
    if not nome or not email or not mensagem:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400
    
    try:
        doc_ref = db.collection("contatos").add({
            "nome": nome,
            "email": email,
            "mensagem": mensagem,
            "timestamp": datetime.datetime.utcnow()
    })
        return jsonify({"success": True, "id": doc_ref[1].id})
    except Exception as e:
        return jsonify({"error": f"Erro ao enviar: {str(e)}"}), 500