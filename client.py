import socket
import time
import sync_messages

def handle_connection(client_socket):
  # ----------------------------------------------
  # CODIGO PRINCIPAL
  # ----------------------------------------------
  request = "20230005"
  sync_messages.send_message(client_socket,request)
  response = sync_messages.recv_message(client_socket)
  print(f"Final grade: {response}")
  # ----------------------------------------------

def main():
  server_address = ("localhost",5000)
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)
    start = time.time() * 1000
    handle_connection(client_socket)
    end = time.time() * 1000

  print(f"Transaction time: {end - start} ms")

if __name__ == "__main__":
  main()