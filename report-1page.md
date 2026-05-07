# Report 1 page - Lab 3

## Thông tin nhóm

- Thành viên 1: Nguyễn Xuân Quang
- Thành viên 2: Nguyễn Anh Tuấn

## Mục tiêu

Xây dựng một hệ thống gửi/nhận dữ liệu qua TCP socket, mã hoá bản tin bằng DES-CBC với PKCS#7 padding và header độ dài, đồng thời kiểm thử luồng truyền tin và nhận diện hạn chế bảo mật của thiết kế hiện tại.

## Phân công thực hiện

- Nguyễn Xuân Quang phụ trách chính `sender.py`, phần mã hoá DES và cấu trúc packet.
- Nguyễn Anh Tuấn phụ trách chính `receiver.py`, các kiểm thử tự động và ghi log.
- Cả hai cùng thực hiện threat model, báo cáo và debug hệ thống.

## Cách làm

Sender tạo key và IV dài 8 byte, mã hoá plaintext bằng DES-CBC và để padding PKCS#7, rồi gửi tuần tự key + IV + header độ dài 4 byte + ciphertext. Receiver lắng nghe socket, nhận header và ciphertext, giải mã bằng DES-CBC, bỏ padding và in ra bản rõ. Các hàm pad/unpad, encrypt/decrypt, build/parse packet được tổ chức trong `des_socket_utils.py`.

## Kết quả

Hệ thống chạy được bằng `python receiver.py` và `python sender.py`, hoặc qua biến môi trường `SERVER_IP`, `SERVER_PORT`, `MESSAGE`. Đã chạy thành công 6 test trong `tests/`, gồm test roundtrip local, negative test cho tamper và test wrong key. Log minh chứng được lưu tại `logs/demo_run.log`.

## Kết luận

Lab giúp làm rõ luồng mã hoá/lưỡng mã qua socket và vai trò của key, IV, padding và header. Thiết kế hiện tại không an toàn trong thực tế vì truyền key và IV plaintext trên cùng kết nối TCP; để triển khai thật cần thêm key agreement, xác thực và integrity protection.
