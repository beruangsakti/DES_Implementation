import socket

def send_shutdown_command():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))
    client_socket.send("shutdown".encode())
    client_socket.close()

# Send shutdown command to the server
send_shutdown_command()