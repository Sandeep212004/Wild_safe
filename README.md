from flask import Flask, redirect, request, jsonify
from config import Config
from utils import (
    get_staff_details,
    get_verification_key,
    decode_and_verify_token,
    generate_app_jwt
)

app = Flask(__name__)
app.config.from_object(Config)


# 🔹 Home
@app.route("/")
def home():
    return "SSO Demo Running"


# 🔹 Step 1: Redirect to SSO login
@app.route("/login")
def login():
    sso_url = f"{app.config['SSO_BASE_URL']}/login?redirect_uri={app.config['SSO_REDIRECT_URI']}"
    return redirect(sso_url)


# 🔹 Step 2: Callback
@app.route("/sso/callback")
def callback():
    token = request.args.get("token")

    if not token:
        return jsonify({"error": "Token not found in callback"}), 400

    # 🔹 Step 3: Get verification key
    public_key = get_verification_key()
    if not public_key:
        return jsonify({"error": "Failed to fetch verification key"}), 500

    # 🔹 Step 4: Decode token
    decoded = decode_and_verify_token(token, public_key)
    if not decoded:
        return jsonify({"error": "Invalid token"}), 401

    # 🔹 Step 5: Extract staffId
    staff_id = (
        decoded.get("employeeId")
        or decoded.get("staffId")
        or decoded.get("sub")
    )

    if not staff_id:
        return jsonify({"error": "staffId not found in token"}), 400

    # 🔹 Step 6: Fetch user details
    user = get_staff_details(token, staff_id)
    if not user:
        return jsonify({"error": "Failed to fetch user details"}), 401

    # 🔹 Step 7: Generate app JWT
    app_token = generate_app_jwt(user)

    return jsonify({
        "message": "Login successful",
        "staff_id": staff_id,
        "user": user,
        "app_token": app_token
    })


# 🔒 Protected route
@app.route("/dashboard")
def dashboard():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"error": "Missing Authorization header"}), 401

    try:
        token = auth_header.split(" ")[1]

        import jwt
        decoded = jwt.decode(
            token,
            app.config["JWT_SECRET"],
            algorithms=[app.config["JWT_ALGORITHM"]]
        )

        return jsonify({
            "message": "Welcome to dashboard",
            "user": decoded
        })

    except Exception:
        return jsonify({"error": "Invalid token"}), 401


if __name__ == "__main__":
    app.run(debug=True)
