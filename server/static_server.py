from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from multiprocessing import Process

listen_socket= socket(AF_INET,SOCK_STREAM)
listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
server_addr = ('', 10000)
listen_socket.bind(server_addr)

listen_socket.listen(10)
print('listening...')


def handle_client(connet_socket):
	'handling request'
	request_data = connect_socket.recv(1024)
	pass
	request_data.decode()


while True:
	connect_socket, peer_addr = listen_socket.accept()

	process_do_service = Process(target= handle_client, args= (connect_socket,))
	process_do_service.start()

	process_do_service.close()