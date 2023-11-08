import socket
import asyncio
import time
import grades
import async_messages

async def get_student_final_grade(searching_id: int):
  with open("grades.csv","r",encoding="utf-8") as f:
    await asyncio.sleep(0)
    
    lines = f.readlines()
    await asyncio.sleep(0)

    for line in lines:
      line = line[:-1]
      line = line.split(",")
      student_id, Pa, Pb, Ex = grades.parse_register(line)
      student_id = int(student_id)
      if(student_id == searching_id):
        return grades.get_final_grade(Pa,Pb,Ex)
    await asyncio.sleep(0)

  return -1

async def handle_client(client_socket,client_address):
  start = time.time() * 1000

  print("========================================================")
  print(f"Connection accepted from {client_address[0]}:{client_address[1]}")
  # ----------------------------------------------------
  # CODIGO PRINCIPAL
  # ----------------------------------------------------
  request = await async_messages.recv_message(client_socket)

  final_grade = await get_student_final_grade(int(request))

  if (final_grade == -1):
    response = f"Id {request} not found"
    await async_messages.send_message(client_socket,response)
  else:
    response = str(final_grade)
    await async_messages.send_message(client_socket,response)
  # ----------------------------------------------------
  
  end = time.time() * 1000
  client_socket.close()

  print(f"Transaction time: {end - start} ms")


async def main():
  loop = asyncio.get_event_loop()
  server_address = ("localhost",5000)
  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    try:
      server_socket.bind(server_address)
      server_socket.listen(4)
      server_socket.setblocking(False)

      print(f"Listening at {server_address[0]}:{server_address[1]}")
      while True:
        client_socket, client_address = await loop.sock_accept(server_socket)
        asyncio.create_task(handle_client(client_socket,client_address))

    except KeyboardInterrupt:
      print("\nExiting")

if __name__ == "__main__":
  asyncio.run(main())
  