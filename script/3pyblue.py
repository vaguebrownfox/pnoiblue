import bluetooth
import os

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "93fd0c34-5cf0-4c07-8b12-06fcc82e17f0"

bluetooth.advertise_service(server_sock, "Lno", service_id=uuid)

print("Waiting for connection on RFCOMM channel", port)


client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            print("not data")
            break
        if data == b'record' :
            os.system("echo Record start")
        elif data == b'stop' :
            os.system("echo Record stop")

        print(data)
except OSError:
    print("OSError!!")
    pass
