from pathlib import Path
from urllib.parse import quote

from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename


BASE_URL = "http://127.0.0.1:8080"
UPLOAD_FOLDER = Path(__file__).resolve().parent / "uploads"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_image_url(filename):
    return f"{BASE_URL}/uploads/{quote(filename)}"


@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "Image file is required"}), 400

    image = request.files["image"]
    if image.filename == "":
        return jsonify({"error": "Image filename is required"}), 400

    if not is_allowed_file(image.filename):
        return jsonify({"error": "Unsupported image type"}), 400

    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    filename = secure_filename(image.filename)
    image.save(UPLOAD_FOLDER / filename)

    return jsonify({"image_url": get_image_url(filename)}), 201


@app.route("/image/<path:filename>", methods=["GET"])
def get_image(filename):
    filename = secure_filename(filename)
    content_type = request.headers.get("Content-Type", "")
    accept = request.headers.get("Accept", "")

    if content_type == "image" or accept.startswith("image"):
        return send_from_directory(UPLOAD_FOLDER, filename)

    return jsonify({"image_url": get_image_url(filename)}), 200


@app.route("/delete/<path:filename>", methods=["DELETE"])
def delete_image(filename):
    filename = secure_filename(filename)
    image_path = UPLOAD_FOLDER / filename

    if not image_path.exists():
        return jsonify({"error": "Image not found"}), 404

    image_path.unlink()
    return jsonify({"message": f"Image {filename} deleted"}), 200


@app.route("/uploads/<path:filename>", methods=["GET"])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, secure_filename(filename))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
