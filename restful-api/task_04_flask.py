from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}

@app.route("/")
def home():
    """Ana səhifə müraciəti"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Bütün username-ləri siyahı şəklində qaytarır"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """API-ın statusunu yoxlayır"""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Dinamik route: username-ə görə istifadəçi tapır"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadəçi əlavə edir (POST müraciəti)"""
    # 1. Body-nin JSON olub-olmadığını yoxla
    if not request.is_json:
        # Tapşırıq tələbi: Invalid JSON üçün 400
        return jsonify({"error": "Invalid JSON"}), 400
    
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # 2. Username yoxdursa
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 3. Username artıq mövcuddursa
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # 4. İstifadəçini əlavə et və 201 qaytar
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)