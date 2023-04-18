from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import pyftpdlib.handlers

# Настройки FTP-сервера
FTP_HOST = "192.168.1.101" 
FTP_PORT = 21
FTP_USER = "user"
FTP_PASSWORD = "password"
FTP_DIRECTORY = "C:/Users/User/Shared" # замените на свой путь

#авторизация пользователя
authorizer = DummyAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm="elradfmwMT")

handler = FTPHandler
pyftpdlib.handlers.PassiveDTP.timeout = None
handler.authorizer = authorizer

handler.masquerade_address = FTP_HOST

# запуск сервера
with FTPServer((FTP_HOST, FTP_PORT), handler) as server:
    server.serve_forever()

