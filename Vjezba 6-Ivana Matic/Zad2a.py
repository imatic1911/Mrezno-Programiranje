from smtpd import SMTPServer

class CustomSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"Received message from: {mailfrom}")
        print(f"Message addressed to: {rcpttos}")
        print(f"Message data:\n{data}")

if __name__ == "__main__":
    server = CustomSMTPServer(('127.0.0.1', 1025), None)

    try:
        print("SMTP server started.")
        server.serve_forever()
    except KeyboardInterrupt:
        print("SMTP server stopped.")
