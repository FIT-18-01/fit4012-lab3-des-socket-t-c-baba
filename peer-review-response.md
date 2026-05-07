# Peer Review Response

## Thông tin nhóm

- Thành viên 1: Nguyễn Xuân Quang
- Thành viên 2: Nguyễn Anh Tuấn

## Thành viên 1 góp ý cho thành viên 2

Code của bạn chạy ổn, cấu trúc `receiver.py` rõ ràng và xử lý log tốt. Tuy nhiên cần đảm bảo thông báo lỗi dễ đọc khi socket timeout hoặc dữ liệu nhận không hợp lệ.

## Thành viên 2 góp ý cho thành viên 1

Phần `sender.py` nên tách rõ phần build packet và mã hoá để dễ kiểm thử. Nên ghi log sender và receiver riêng để thuận tiện đối chiếu khi debug.

## Nhóm đã sửa gì sau góp ý

Chúng tôi đã cập nhật `sender.py` để dùng hàm `encrypt_des_cbc` và `build_packet` từ `des_socket_utils.py`, đồng thời thêm log gửi/nhận. Cả hai cũng cùng hoàn thiện test local và tạo file log minh chứng `logs/demo_run.log`.
