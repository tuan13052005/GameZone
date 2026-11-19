
document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const result = await response.json();

        if (result.success) {
            // Lưu thông tin người dùng đang đăng nhập
            localStorage.setItem("currentUser", JSON.stringify(result.user));

            alert(result.message);

            window.location.href = "../TrangChu/index.html";
        } else {
            alert(result.message);
        }

    } catch (error) {
        alert("Không thể kết nối đến máy chủ!");
    }
});
