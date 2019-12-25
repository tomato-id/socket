import socket


# 该工具为客户端,用来从服务端下载文件
def main():
    # 1.创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.获取服务器ip port
    dest_ip = '192.168.1.2'
    dest_port = 26886

    # 3.链接服务器
    tcp_client_socket.connect((dest_ip, dest_port))

    # 4.获取下载的文件名
    download_file_name = input('filename:')

    # 5.将文件名发送到服务器
    tcp_client_socket.send(download_file_name.encode('utf-8'))

    # 6.接收文件中的数据
    recv_data = tcp_client_socket.recv(1024*1024)

    # 7.保存接收到的数据到一个文件中
    with open(download_file_name, 'wb') as f:
        f.write(recv_data)

    # 8.关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
