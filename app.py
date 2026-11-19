
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE_JSON = "users.json"


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
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    database = doc_tai_khoan()

    # Kiểm tra email đã tồn tại
    for user in database["users"]:
        if user["email"] == email:
            return jsonify({
                "success": False,
                "message": "Email đã được đăng ký!"
            })

    # Tạo tài khoản mới
    new_user = {
        "id": len(database["users"]) + 1,
        "name": name,
        "email": email,
        "password": password,
        "role": "user"
    }

    database["users"].append(new_user)

    # Lưu vào JSON
    ghi_tai_khoan(database)

    return jsonify({
        "success": True,
        "message": "Đăng ký thành công!"
    })


# Đăng nhập
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    database = doc_tai_khoan()

    for user in database["users"]:
        if user["email"] == email and user["password"] == password:

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
    app.run(debug=True)
