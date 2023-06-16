# 클라이언트 프로그램
import socket
import os
server_ip = '163.152.233.18' 
server_port = 30473

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((server_ip, server_port))

except ConnectionRefusedError:
    print('서버에 연결할 수 없습니다.')
    print('1. 서버의 ip주소와 포트번호가 올바른지 확인하십시오.')
    print('2. 서버 실행 여부를 확인하십시오.')
    os._exit(1)

while True:
    msg = input('msg:')
    if msg == 'quit':
        break
    socket.sendall(msg.encode(encoding='utf-8'))

    data = socket.recv(1024)
    msg = data.decode()
    print('echo msg:', msg)

socket.close()
