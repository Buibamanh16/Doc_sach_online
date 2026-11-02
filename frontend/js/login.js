document
  .getElementById("loginForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;
    const msgDiv = document.getElementById("message");

    msgDiv.style.color = "blue";
    msgDiv.textContent = "Đang xử lý...";

    try {
      // Cập nhật đường dẫn chuẩn trỏ tới auth router tại đây
      const response = await fetch("http://127.0.0.1:8000/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: user,
          password: pass,
        }),
      });

      const result = await response.json();

      if (response.ok) {
        msgDiv.style.color = "green";
        msgDiv.textContent = `Xin chào ${result.data.username}! Đăng nhập thành công.`;
      } else {
        msgDiv.style.color = "red";
        msgDiv.textContent = result.detail || "Đăng nhập thất bại!";
      }
    } catch (error) {
      msgDiv.style.color = "red";
      msgDiv.textContent = "Không thể kết nối tới máy chủ Backend!";
    }
  });
