import socket
import asyncio

async def send_message(socket: socket.socket, message = "Mensaje default"):
  raw_message = message.encode("utf-8")
  await asyncio.sleep(0)
  
  socket.sendall(raw_message)
  await asyncio.sleep(0)
  
  print("========================================================")
  print(f"Sent: {message}")

async def recv_message(socket: socket.socket, BUFFSIZE = 1024) -> str:
  raw_message = socket.recv(BUFFSIZE)
  await asyncio.sleep(0)
  
  message = raw_message.decode("utf-8")
  await asyncio.sleep(0)

  print("========================================================")
  print(f"Received: {message}")
  return message