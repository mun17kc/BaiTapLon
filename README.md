# Web Scraping Dữ Liệu Bất Động Sản

Đoạn mã Python này thu thập dữ liệu bất động sản từ trang web [alonhadat.com.vn](https://alonhadat.com.vn), đặc biệt là các tin đăng về bất động sản tại Đà Nẵng. Mục tiêu của script là thu thập thông tin về tiêu đề, giá, địa chỉ, diện tích và mô tả cho mỗi tin đăng và lưu vào một file Excel để người dùng có thể dễ dàng tham khảo và phân tích.

## Tính Năng
- Thu thập thông tin chi tiết các tin đăng bất động sản bao gồm:
  - Tiêu đề tin đăng.
  - Giá của bất động sản.
  - Địa chỉ của bất động sản.
  - Diện tích của bất động sản.
  - Mô tả chi tiết của bất động sản.
- Thu thập dữ liệu từ nhiều trang trong danh sách tin đăng.
- Lưu kết quả vào file Excel (`BTL.xlsx`).
- Chạy tự động mỗi ngày vào lúc 6:00 sáng thông qua thư viện `schedule`.


## Yêu Cầu

Để chạy được script này, bạn cần cài đặt các phần mềm và thư viện sau:

### 1. **Cài Đặt Python và Thư Viện**
- **Python**: Phiên bản Python 3.x trở lên.
- Các thư viện yêu cầu:
  - `selenium`: Dùng để tự động hóa trình duyệt web và thu thập dữ liệu.
  - `pandas`: Dùng để lưu trữ và xử lý dữ liệu thu thập được vào file Excel.
  - `schedule`: Dùng để lên lịch chạy tự động script vào thời gian chỉ định.

### 2. **Tải Chrome WebDriver**
- Bạn cần tải [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) tương thích với phiên bản Google Chrome mà bạn đang sử dụng. Đảm bảo rằng bạn đã thêm đường dẫn của `ChromeDriver` vào biến môi trường hoặc chỉ rõ đường dẫn khi khởi tạo trình duyệt.

## Cài Đặt và Chạy Script

 ## Cài đặt các thư viện Python:
   Trước khi chạy script, bạn cần cài đặt các thư viện yêu cầu. Chạy lệnh sau trong terminal hoặc command prompt để cài đặt:

   pip install -r requirements.txt

## Tải và cài đặt ChromeDriver:

Tải phiên bản ChromeDriver tương thích với trình duyệt Chrome của bạn.

Đảm bảo rằng ChromeDriver có thể được truy cập từ bất kỳ thư mục nào trong hệ thống của bạn (có thể thêm đường dẫn vào biến môi trường PATH).

## Chạy Script:

Sau khi cài đặt các thư viện và thiết lập ChromeDriver, bạn có thể chạy script bằng cách sử dụng lệnh sau:
python script_name.py ( ví dụ như bài tôi python main.py)

## Lên Lịch Tự Động:

Script này đã được lên lịch tự động chạy vào lúc 6:00 sáng mỗi ngày nhờ vào thư viện schedule.

Nếu bạn muốn thay đổi thời gian chạy, bạn chỉ cần chỉnh sửa dòng sau trong script:

schedule.every().day.at("06:00").do(thu_thap_va_luu)

Cấu Trúc File Kết Quả

Khi chạy thành công, dữ liệu thu thập được sẽ được lưu vào một file Excel với tên BTL.xlsx. File Excel này chứa các cột sau:

tiêu đề: Tiêu đề của tin đăng.

giá: Giá của bất động sản.

địa chỉ: Địa chỉ của bất động sản.

diện tích: Diện tích của bất động sản.

mô tả: Mô tả chi tiết về bất động sản.

## Ví Dụ Kết Quả
Sau khi script chạy thành công, một file Excel (BTL.xlsx) sẽ được tạo. File này sẽ chứa dữ liệu về các tin đăng bất động sản đã thu thập từ website.

## Các Lỗi Thường Gặp
Lỗi khi truy cập trang web: Nếu trang web không tải được hoặc có sự cố khi truy xuất thông tin, hãy kiểm tra kết nối internet hoặc thay đổi thời gian chờ.

Lỗi WebDriver: Đảm bảo rằng ChromeDriver đã được cài đặt đúng phiên bản và có thể truy cập từ bất kỳ thư mục nào trong hệ thống của bạn.

Lỗi khi thu thập dữ liệu: Nếu không tìm thấy các phần tử trên trang, có thể cấu trúc của trang web đã thay đổi. Bạn cần kiểm tra và cập nhật lại các selectors trong script.

