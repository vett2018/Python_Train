import socket

# class Socket:
#     def __init__(self, sock_familty, sock_type, proto):
#         self._fd = system_socket(sock_family, sock_type, proto)
#
#     def write(self, data):
#             # на самом деле вместо write используется send, но об этом ниже
#         system_write(self._fd, data)
#
#     def fileno(self):
#         return self._fd

if __name__ == '__main__':
    serv_sock = socket.socket(socket.AF_INET,  # задамем семейство протоколов 'Интернет' (INET)
                              socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
                              proto=0)  # выбираем протокол 'по умолчанию' для TCP, т.е. IP
    serv_sock.bind(('', 53210))  # чтобы привязать сразу ко всем, можно использовать ''
    serv_sock.listen(10)

    while True:
        # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()
        print('Connected by', client_addr)

        while True:
            # Пока клиент не отключился, читаем передаваемые
            # им данные и отправляем их обратно
            data = client_sock.recv(1024)
            if not data:
                # Клиент отключился
                break
            client_sock.sendall(data)

        client_sock.close()

