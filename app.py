from flask import Flask, render_template, request
from database import init_db, add_user, get_all_users

app = Flask(__name__)

# Khởi tạo database
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        # Lấy dữ liệu từ form
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        message_input = request.form.get("message", "").strip()

        # Kiểm tra đầy đủ thông tin
        if not (name and phone and message_input):
            return render_template("index.html", error="Vui lòng điền đủ thông tin.", form=request.form)

        # Lưu vào database
        add_user(name, phone, message_input)

        message = f"Cảm ơn {name}! Thông tin của bạn đã được lưu."

        # Trả về trang index kèm thông báo
        return render_template("index.html", message=message)

    return render_template("index.html")

@app.route("/admin")
def admin():
    # Lấy tất cả user từ database
    users = get_all_users()
    return render_template("admin.html", users=users)

if __name__ == "__main__":
    # Chạy web trên localhost:5000
    app.run(debug=True, host="127.0.0.1", port=5000)
    from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


