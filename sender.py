import os
import socket

from des_socket_utils import encrypt_des_cbc, build_packet

HOST = os.getenv('SERVER_IP', '127.0.0.1')
PORT = int(os.getenv('SERVER_PORT', '5000'))
MESSAGE = os.getenv('MESSAGE', '')
LOG_FILE = os.getenv('SENDER_LOG_FILE', '')


def main() -> None:
    message = os.getenv('MESSAGE', '')
    if not message:
        message = input("Enter message: ")

    plain = message.encode('utf-8')

    key, iv, cipher_bytes = encrypt_des_cbc(plain)

    packet = build_packet(key, iv, cipher_bytes)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(packet)

        print("[Sender] Sent successfully")

        lines = [
            f"[Sender] Key: {key.hex()}",
            f"[Sender] IV: {iv.hex()}",
            f"[Sender] Ciphertext: {cipher_bytes.hex()}",
            f"[Sender] Plaintext: {message}"
        ]

        for line in lines:
            print(line)

        if LOG_FILE:
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()