import socket


# 该工具为服务端,用来发送客户端需要下载的文件
def send_file_2_client(new_client_socket, client_addr):
    # 1.接收客户端需要下载的文件名
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端%s需要下载的文件是:%s' % (str(client_addr), file_name))

    file_content = None

    # 2.打开这个文件,读取数据
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有需要下载的文件%s' % file_name)

    # 3.回送数据
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    localaddr = ('192.168.0.103', 26886)
    tcp_server_socket.bind(localaddr)

    # 3.被动监听
    tcp_server_socket.listen(128)

    while True:
        # 4.等待链接
        print('监听等待链接')
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5.调用函数
        send_file_2_client(new_client_socket, client_addr)

        # 6.关闭套接字
        new_client_socket.close()

        goon = input('是否继续?  1继续  2关闭')
        if goon == '2':
            break

    tcp_server_socket.close()


if __name__ == '__main__':
    main()
