<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quản Lý Công Việc - Task Management System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            color: #ffeb3b;
        }
    </style>
</head>
<body>
    <h1>Quản Lý Công Việc - Task Management System</h1>
    
    <h2>Thông tin sinh viên</h2>
    <ul>
        <li><strong>Họ và tên:</strong> Đỗ Tấn Đạt</li>
        <li><strong>MSSV:</strong> 22648601</li>
        <li><strong>Lớp:</strong> DHKHDL18A</li>
        <li><strong>Môn học:</strong> Phát triển ứng dụng</li>
        <li><strong>Giảng viên:</strong> ThS. Trương Vĩnh Linh</li>
    </ul>
    
    <h2>Giới thiệu project</h2>
    <p>Hệ thống Quản lý Công việc là một ứng dụng web được xây dựng bằng Django Framework, cho phép người dùng quản lý và theo dõi các công việc của mình một cách hiệu quả.</p>
    
    <h2>Tính năng chính</h2>
    <h3>Quản lý người dùng</h3>
    <ul>
        <li>Đăng ký tài khoản mới</li>
        <li>Đăng nhập/Đăng xuất</li>
        <li>Quản lý thông tin cá nhân</li>
        <li>Tùy chỉnh avatar người dùng</li>
    </ul>
    
    <h3>Quản lý công việc</h3>
    <ul>
        <li>Tạo công việc mới</li>
        <li>Chỉnh sửa thông tin công việc</li>
        <li>Xóa công việc</li>
        <li>Theo dõi trạng thái công việc</li>
        <li>Thông báo công việc quá hạn</li>
    </ul>
    
    <h3>Giao diện</h3>
    <ul>
        <li>Thiết kế responsive</li>
        <li>Giao diện thân thiện, dễ sử dụng</li>
        <li>Hỗ trợ dark/light mode</li>
        <li>Hiệu ứng và animation đẹp mắt</li>
    </ul>
    
    <h2>Công nghệ sử dụng</h2>
    <h3>Backend</h3>
    <ul>
        <li>Python 3.12.7</li>
        <li>Django 5.1.7</li>
        <li>SQLite Database</li>
    </ul>
    
    <h3>Frontend</h3>
    <ul>
        <li>HTML5/CSS3</li>
        <li>Bootstrap 5</li>
        <li>JavaScript</li>
        <li>Font Awesome 5</li>
    </ul>
    
    <h2>Hướng dẫn cài đặt</h2>
    <h3>Yêu cầu hệ thống</h3>
    <ul>
        <li>Python 3.12 trở lên</li>
        <li>pip (Python package installer)</li>
        <li>Git</li>
    </ul>
    
    <h3>Các bước cài đặt</h3>
    <ol>
        <li><strong>Clone repository</strong>
            <pre><code>git clone https://github.com/DanieSalin/ptud-gk-de-2.git
cd ptud-gk-de-2</code></pre>
        </li>
        <li><strong>Tạo môi trường ảo</strong>
            <pre><code># Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate</code></pre>
        </li>
        <li><strong>Cài đặt các thư viện</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Thực hiện migrate database</strong>
            <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
        </li>
        <li><strong>Tạo tài khoản admin (không bắt buộc)</strong>
            <pre><code>python manage.py createsuperuser</code></pre>
        </li>
        <li><strong>Khởi động server</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Truy cập ứng dụng</strong>
            <ul>
                <li>Mở trình duyệt và truy cập: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></li>
                <li>Trang admin: <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a></li>
            </ul>
        </li>
    </ol>
    
    <h2>Hướng dẫn sử dụng</h2>
    <ol>
        <li>Đăng ký tài khoản mới hoặc đăng nhập nếu đã có tài khoản</li>
        <li>Tại trang chủ, bạn có thể:
            <ul>
                <li>Xem danh sách công việc</li>
                <li>Tạo công việc mới</li>
                <li>Cập nhật thông tin công việc</li>
                <li>Xóa công việc</li>
            </ul>
        </li>
        <li>Vào trang cá nhân để:
            <ul>
                <li>Cập nhật thông tin</li>
                <li>Thay đổi avatar</li>
                <li>Xem thống kê công việc</li>
            </ul>
        </li>
    </ol>
    
    <h2>Liên hệ</h2>
    <ul>
        <li>Email: <a href="mailto:dodat2004py@gmail.com">dodat2004py@gmail.com</a></li>
        <li>GitHub: <a href="https://github.com/DanieSalin" target="_blank">DanieSalin</a></li>
    </ul>
</body>
</html>
