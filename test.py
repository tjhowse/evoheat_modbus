#!/usr/bin/env python3

import socket
from hexdump import hexdump
from datetime import datetime

host = "hws.local"
port = 6638

def main():
    # Connect to the raw TCP socket server at host:port and print the bytes to stdout

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            while True:
                data = s.recv(1024)
                if not data:
                    break
                # Convert the bytes to a string in hex format
                hex = data.hex(':')
                print(hex)

                with open("log.raw", "ab") as f:
                    f.write(data)
                if hex == "fe":
                     continue
                date = datetime.now().isoformat()
                with open("log.log", "a") as f:
                    f.write(date+"\n")
                    f.write(hex)
                    f.write("\n")

                with open("hexdump.log", "a") as f:
                    f.write(date+"\n")
                    f.write(hexdump(data, result='return'))
                    f.write("\n")

if __name__ == "__main__":
    main()
