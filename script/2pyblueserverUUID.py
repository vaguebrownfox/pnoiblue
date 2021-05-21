import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]
print("port!!", port)

uuid = "93fd0c34-5cf0-4c07-8b12-06fcc82e17f0"

bluetooth.advertise_service(server_sock, "Lno", service_id=uuid
                            # protocols=[bluetooth.OBEX_UUID]
                            )
print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)


with open('./rec.WAV', mode='rb') as f:
    dataB = f.read(1024)
    while dataB != "":
        client_sock.send(dataB)
        dataB = f.read(1024)


try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            print("not data")
            break
        print("Received", str(data))
        with open('filename.txt', mode='a') as f:
            f.write(str(data) + '\n')
except OSError:
    print("OSError!!")
    pass



print("Disconnected.")


client_sock.close()
server_sock.close()
print("All done.")