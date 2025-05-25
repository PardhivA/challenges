# import socket

# def start_lb(host='0.0.0.0', port=80):
#     # Create a TCP socket
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         server_socket.bind((host, port))
#         server_socket.listen(5)

#         print(f"[INFO] Load balancer started on port {port}")

#         while True:
#             client_socket, client_address = server_socket.accept()
#             print(f"\n[INFO] Received request from {client_address[0]}")

#             request_data = client_socket.recv(1024).decode('utf-8')
#             print(request_data)

#             # Send a basic HTTP response back
#             response = (
#                 "HTTP/1.1 200 OK\r\n"
#                 "Content-Type: text/plain\r\n"
#                 "Content-Length: 17\r\n"
#                 "\r\n"
#                 "Request received\n"
#             )
#             client_socket.sendall(response.encode('utf-8'))
#             client_socket.close()

# if __name__ == "__main__":
#     try:
#         start_lb()
#     except PermissionError:
#         print("Permission denied: try running with sudo if using port 80.")



import socket


def lb(host = "0.0.0.0", port = 80):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server_socket.bind((host,port))
        server_socket.listen(5)
        
        print(f"[INFO] Load balancer started on port {port}")
        
        while True:
            client_socket, client_address = server_socket.accept()
            
            print(f"\n[INFO] Received request from {client_address[0]}")
            
            
            request_data = client_socket.recv(1024).decode('utf-8')
            
            print(request_data)
            
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                "Content-Length: 17\r\n"
                "\r\n"
                "Request received\n" 
            )
            
            client_socket.sendall(response.encode('utf-8'))
            
            client_socket.close()
            
            
if __name__ == "__main__":
    try:
        lb()
    except PermissionError:
        print("Permission denied: try running with sudo if using port 80.")
        