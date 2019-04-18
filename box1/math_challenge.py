#!/usr/bin/env python3
import random
import socket
import argparse
import textwrap
import time


class ChallengeServer:
    BUFSIZE = 4096
    INSTRUCTIONS = """
    This challenge requires you write a python program to process simple math equations sent from this server.  Your
    program should receive messages from this server, process the equation, and send the evaluated equation to the 
    server.  

    Examples: 
        If the server sends 
            4 + 4
        You should respond with 
            8
    
        If the server sends 
            8 * 8
        You should respond with
            64
            
        If the server sends
            17 / 6
        You should respond with
            2.83

    The server will only send equations consisting of two positive whole numbers between 1 and 100 separated by a 
    mathematical operator representing addition, subtraction, division or multiplication (i.e. + - / *).  The server 
    will never send negative numbers, however, your responses are allowed to be negative.  In the event of division, 
    the answer should be rounded to two decimal places.  

    The server will issue {iterations} equations before responding with the flag.  The server is impatient and won't 
    wait very long for a response.  If you don't respond quickly enough, the server will sever the connection and you 
    will need to start over.

    No questions?  Good.  Here we go.
    =========== Challenge Starting ===========
    """

    def __init__(self, port):
        self.port = port
        self.conn = None

    def _accept_connection(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', int(self.port)))
        sock.listen(1)
        client, _ = sock.accept()
        return client

    def send_message(self, message):
        message = message.encode() if isinstance(message, str) else message
        self.conn.sendall(message)

    def receive_message(self):
        msg = b''

        while True:
            chunk = self.conn.recv(ChallengeServer.BUFSIZE)
            if len(chunk) < ChallengeServer.BUFSIZE:
                return msg + chunk
            msg += chunk

    def close_socket(self):
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()

    def listen(self):
        self.conn = self._accept_connection()

        num_loops = 10
        flag = "4fb83aac261ee19ab8dd744f451f7ae9d5790392"

        self.send_message(textwrap.dedent(ChallengeServer.INSTRUCTIONS.format(iterations=num_loops)))

        time.sleep(.5)
        self.conn.settimeout(0.5)

        operators = ['+', '-', '*', '/']

        try:
            while num_loops != 0:
                left_operand = random.randrange(1, 100)
                right_operand = random.randrange(1, 100)
                operator = random.choice(operators)
                msg = f"{left_operand} {operator} {right_operand}"

                self.send_message(f"{msg}\n")

                data = self.receive_message()

                if data.decode().strip() != str(round(eval(msg), 2)):
                    break

                num_loops -= 1

            if num_loops == 0:
                self.send_message(f"The flag is: {flag}\n")
            else:
                self.send_message(f"I sent {msg}.  You should have sent {round(eval(msg), 2)}.  "
                                  f"I received {data.decode().strip()}.  "
                                  f"Please try again, or don't, I'm not the challenge police.\n")
        except socket.timeout as e:
            self.send_message("Too slow...\n")
        finally:
            self.close_socket()


def main(arguments):
    ChallengeServer(arguments.port).listen()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help='port on which to listen', default=12345)

    args = parser.parse_args()
    main(args)

