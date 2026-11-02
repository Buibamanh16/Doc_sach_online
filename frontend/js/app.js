const API_URL = "http://127.0.0.1:8000/api/books";
let currentPage = 1;
const limit = 12;

async function fetchBooks(page = 1) {
  const grid = document.getElementById("bookGrid");
  grid.innerHTML = "<p>Đang tải dữ liệu...</p>";

  try {
    const response = await fetch(`${API_URL}?page=${page}&limit=${limit}`);
    const data = await response.json();

    renderBooks(data.books);
    renderPagination(data.total, page, limit);
  } catch (error) {
    console.error("Lỗi khi gọi API:", error);
    grid.innerHTML =
      '<p style="color:red">Không thể kết nối tới máy chủ API!</p>';
  }
}

function renderBooks(books) {
  const grid = document.getElementById("bookGrid");
  if (!books || books.length === 0) {
    grid.innerHTML = "<p>Chưa có sách nào.</p>";
    return;
  }

  grid.innerHTML = books
    .map(
      (book) => `
        <div class="book-card">
            <img class="book-cover" src="${book.cover_url || "https://via.placeholder.com/220x280?text=No+Cover"}" alt="${book.title}">
            <div class="book-info">
                <div class="book-title" title="${book.title}">${book.title}</div>
                <div class="book-meta">
                    <span class="book-rating">★ ${book.avg_rating || "0.0"}</span>
                    <span>${book.published_year || ""}</span>
                </div>
            </div>
        </div>
    `,
    )
    .join("");
}

function renderPagination(total, page, limit) {
  const totalPages = Math.ceil(total / limit);
  const pagination = document.getElementById("pagination");

  let html = "";
  if (page > 1) {
    html += `<button onclick="changePage(${page - 1})">Trước</button>`;
  }

  html += `<button class="active">${page} / ${totalPages}</button>`;

  if (page < totalPages) {
    html += `<button onclick="changePage(${page + 1})">Sau</button>`;
  }

  pagination.innerHTML = html;
}

function changePage(newPage) {
  currentPage = newPage;
  fetchBooks(currentPage);
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Khởi chạy khi load trang
document.addEventListener("DOMContentLoaded", () => {
  fetchBooks(currentPage);
});
