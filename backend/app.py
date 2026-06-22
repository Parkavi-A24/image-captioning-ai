from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from caption_generator import generate_caption

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/caption', methods=['POST'])
def caption():

    if 'image' not in request.files:
        return jsonify({"error":"No image uploaded"})

    file = request.files['image']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = generate_caption(filepath)

    return jsonify({"caption": result})

if __name__ == "__main__":
    app.run(debug=True)
