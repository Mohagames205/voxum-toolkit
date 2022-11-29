import socket
import json

simulated_users = {}

def connect_socket():
    HOST = "127.0.0.1"
    PORT = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

s = connect_socket()
while True:
    command, *args = input("Enter command: ").split()

    if command.lower() == "sim-user":
        main_user = args[0]
        other_users = args[1:]

        print(main_user, other_users)

        user_dict = {}

        for i in range(len(other_users)):
            if i % 2 == 0:
                user_dict[other_users[i]] = int(other_users[i + 1])

        simulated_users[main_user] = user_dict


    if command.lower() == "push":
        print(simulated_users)
        s.sendall(json.dumps(simulated_users).encode())
        print("Pushed users to voxum")

    if command.lower() == "rest":
        simulated_users = {}
        print("Simulated users reset")

    if command.lower() == "stop":
        break




















