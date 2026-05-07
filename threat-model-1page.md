# Threat Model - Lab 3

## Thông tin nhóm

- Thành viên 1: Nguyễn Xuân Quang
- Thành viên 2: Nguyễn Anh Tuấn

## Assets

- Bản tin gốc (plaintext) truyền qua socket.
- Khóa DES 8 byte và IV 8 byte được gửi cùng với ciphertext.
- Tính toàn vẹn và tính bảo mật của gói dữ liệu.

## Attacker model

- Kẻ tấn công có thể nghe lén lưu lượng TCP (passive eavesdropper).
- Kẻ tấn công có thể chặn và sửa đổi gói tin (active MITM) trên cùng kết nối mạng nội bộ.
- Kẻ tấn công không có quyền truy cập trực tiếp vào máy gửi hoặc máy nhận nhưng có thể tác động lên kênh truyền.

## Threats

- Thực thể nghe lén có thể thu thập key và IV plaintext cùng ciphertext, dẫn tới giải mã toàn bộ thông điệp.
- Kẻ tấn công có thể thay đổi ciphertext trước khi truyền đến receiver, gây ra sai lệch hoặc lỗi khi giải mã.
- Kẻ tấn công có thể phát lại gói tin cũ để gây nhầm lẫn hoặc tấn công replay.

## Mitigations

- Không gửi key và IV bằng plaintext trên cùng kênh; sử dụng key exchange an toàn hoặc TLS để bảo vệ kênh truyền.
- Thêm xác thực integrity như HMAC hoặc MAC trên toàn bộ packet để phát hiện tampering.
- Thêm cơ chế chống replay, ví dụ số nhảy (nonce) hoặc timestamp trong packet.

## Residual risks

- DES có khóa 56-bit yếu và không đủ an toàn với attacker hiện đại.
- Nếu channel bị xâm nhập, attacker vẫn có thể phá hoại hoặc tái phát gói tin, vì hệ thống chưa có bảo vệ chống replay và xác thực mạnh.
