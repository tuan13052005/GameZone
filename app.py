from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

app = Flask(__name__)
CORS(app)  # Cho phép trang web ở port 5500 gọi tới Flask ở port 5000

# Luôn lưu users.json cùng thư mục với app.py
THU_MUC = os.path.dirname(os.path.abspath(__file__))
FILE_JSON = os.path.join(THU_MUC, "users.json")


# Đọc danh sách tài khoản
def doc_tai_khoan():
    if not os.path.exists(FILE_JSON):
        with open(FILE_JSON, "w", encoding="utf-8") as f:
            json.dump({"users": []}, f, ensure_ascii=False, indent=4)

    with open(FILE_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


# Ghi danh sách tài khoản
def ghi_tai_khoan(data):
    with open(FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Đăng ký
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "Vui lòng nhập đầy đủ thông tin!"
        })

    if len(password) < 6:
        return jsonify({
            "success": False,
            "message": "Mật khẩu phải có ít nhất 6 ký tự!"
        })

    database = doc_tai_khoan()

    # Kiểm tra email đã tồn tại
    for user in database["users"]:
        if user["email"].lower() == email:
            return jsonify({
                "success": False,
                "message": "Email đã được đăng ký!"
            })

    # Tạo id mới (không bị trùng kể cả khi xóa user)
    new_id = max((u["id"] for u in database["users"]), default=0) + 1

    new_user = {
        "id": new_id,
        "name": name,
        "email": email,
        "password": generate_password_hash(password),  # lưu dạng mã hóa
        "role": "user"
    }

    database["users"].append(new_user)
    ghi_tai_khoan(database)

    return jsonify({
        "success": True,
        "message": "Đăng ký thành công!"
    })


# Đăng nhập
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    database = doc_tai_khoan()

    for user in database["users"]:
        if user["email"].lower() == email and check_password_hash(user["password"], password):
            return jsonify({
                "success": True,
                "message": "Đăng nhập thành công!",
                "user": {
                    "id": user["id"],
                    "name": user["name"],
                    "email": user["email"],
                    "role": user["role"]
                }
            })

    return jsonify({
        "success": False,
        "message": "Email hoặc mật khẩu không chính xác!"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)