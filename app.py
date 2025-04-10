from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    return jsonify({"answer": f"You asked: '{question}' — great question!"})

if __name__ == "__main__":
    app.run()
