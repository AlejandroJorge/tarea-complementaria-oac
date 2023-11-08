import socket
import time
import sync_messages
import grades

def get_student_final_grade(searching_id: int):
  with open("grades.csv","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
      line = line[:-1]
      line = line.split(",")
      student_id, Pa, Pb, Ex = grades.parse_register(line)
      student_id = int(student_id)
      if(student_id == searching_id):
        return grades.get_final_grade(Pa,Pb,Ex)
  return -1


def handle_client(client_socket,client_address):
  start = time.time() * 1000

  print("========================================================")
  print(f"Connection accepted from {client_address[0]}:{client_address[1]}")
  # ----------------------------------------------------
  # CODIGO PRINCIPAL
  # ----------------------------------------------------
  request = sync_messages.recv_message(client_socket)

  final_grade = get_student_final_grade(int(request))
  if (final_grade == -1):
    response = f"Id {request} not found"
    sync_messages.send_message(client_socket,response)
  else:
    response = str(final_grade)
    sync_messages.send_message(client_socket,response)
  # ----------------------------------------------------

  end = time.time() * 1000
  client_socket.close()

  print(f"Transaction time: {end - start} ms")

def main():
  server_address = ("localhost",5000)
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    try:
      server_socket.bind(server_address)
      server_socket.listen(4)
      
      print(f"Listening at {server_address[0]}:{server_address[1]}")
      while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket,client_address)

    except KeyboardInterrupt:
      print("\nExiting")

    except Exception as err:
      print(f"Aborting: {err}")

if __name__ == "__main__":
  main()
  