import os
from datetime import datetime, timezone
from flask import Flask, jsonify, request, send_from_directory
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# --- MongoDB Connect ---
client = MongoClient(os.getenv("MONGO_URI"))
db = client["portfolio"]
messages_collection = db["messages"]

# Un HTML file ah kaatradhu
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

# Contact form data vaanguradhu
@app.post("/api/contact")
def contact():
    data = request.get_json(silent=True) or request.form
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    subject = str(data.get("subject", "")).strip()
    message = str(data.get("message", "")).strip()

    if not all([name, email, subject, message]):
        return jsonify({"ok": False, "message": "Please complete every field."}), 400

    messages_collection.insert_one({
        "name": name,
        "email": email,
        "subject": subject,
        "message": message,
        "created_at": datetime.now(timezone.utc).isoformat()
    })
    return jsonify({"ok": True, "message": "Thanks! Your message has been received."}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))