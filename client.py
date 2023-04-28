import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    # server_address = ('172.20.0.5', 10000)
    server_address = ('172.20.0.5', 32444) # diganti ke 32444 sesuai soal
    
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data plain message
    # message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    # logging.info(f"sending {message}")
    # sock.sendall(message.encode())
    
    # Send file data
    file = open('contoh.txt', 'rb')
    logging.info(f"sending file")
    line = file.read(1024)
    while(line):
        sock.sendall(line)
        line = file.read(1024)
    file.close()
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logging.info(f"{data}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()
