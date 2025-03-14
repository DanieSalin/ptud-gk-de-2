# Quản Lý Công Việc - Task Management System

## Thông tin sinh viên
- **Họ và tên:** Đỗ Tấn Đạt
- **MSSV:** 22648601
- **Lớp:** DHKHDL18A
- **Môn học:** Phát triển ứng dụng
- **Giảng viên:** ThS. Trương Vĩnh Linh

## Giới thiệu project
Hệ thống Quản lý Công việc là một ứng dụng web được xây dựng bằng Django Framework, cho phép người dùng quản lý và theo dõi các công việc của mình một cách hiệu quả.

## Tính năng chính
### Quản lý người dùng
- Đăng ký tài khoản mới
- Đăng nhập/Đăng xuất
- Quản lý thông tin cá nhân
- Tùy chỉnh avatar người dùng

### Quản lý công việc
- Tạo công việc mới
- Chỉnh sửa thông tin công việc
- Xóa công việc
- Theo dõi trạng thái công việc
- Thông báo công việc quá hạn

### Giao diện
- Thiết kế responsive
- Giao diện thân thiện, dễ sử dụng
- Hỗ trợ dark/light mode
- Hiệu ứng và animation đẹp mắt

## Công nghệ sử dụng
### Backend
- Python 3.12.7
- Django 5.1.7
- SQLite Database

### Frontend
- HTML5/CSS3
- Bootstrap 5
- JavaScript
- Font Awesome 5

## Hướng dẫn cài đặt
### Yêu cầu hệ thống
- Python 3.12 trở lên
- pip (Python package installer)
- Git

### Các bước cài đặt
1. **Clone repository**
   ```bash
   git clone https://github.com/DanieSalin/ptud-gk-de-2.git
   cd ptud-gk-de-2
   ```
2. **Tạo môi trường ảo**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Cài đặt các thư viện**
   ```bash
   pip install -r requirements.txt
   ```
4. **Thực hiện migrate database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Tạo tài khoản admin (không bắt buộc)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Khởi động server**
   ```bash
   python manage.py runserver
   ```
7. **Truy cập ứng dụng**
   - Mở trình duyệt và truy cập: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Trang admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Hướng dẫn sử dụng
1. Đăng ký tài khoản mới hoặc đăng nhập nếu đã có tài khoản
2. Tại trang chủ, bạn có thể:
   - Xem danh sách công việc
   - Tạo công việc mới
   - Cập nhật thông tin công việc
   - Xóa công việc
3. Vào trang cá nhân để:
   - Cập nhật thông tin
   - Thay đổi avatar
   - Xem thống kê công việc

## Liên hệ
- Email: [dodat2004py@gmail.com](mailto:dodat2004py@gmail.com)
- GitHub: [DanieSalin](https://github.com/DanieSalin)
- LinkedIn: [Đạt Đỗ](https://www.linkedin.com/in/dotandatdaniel)