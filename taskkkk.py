
import os


class Environment:
    env_var = os.environ

    def env_print(self):
        return "Переменные окружения пользователя:\n%s" % self.env_var

    def env_elem_get(self, name_var):
        return os.getenv(name_var)

    def env_elem_modify(self, name_var, new_value):
        os.environ[name_var] = new_value
        return os.environ[name_var]

    def new_elem(self, name_elem, value_elem):
        os.environ[name_elem] = value_elem
        return '%s = %s' % (name_elem, os.getenv(name_elem))


# Environment test
e1 = Environment()
print(e1.env_print())
print(e1.env_elem_get('APPDATA'))
print(e1.env_elem_modify('USERNAME', 'Homes'))
print(e1.new_elem('EXAMPLE', 'Example'))


class Server:
    SERVER_NAME = 'Server'
    SERVER_PORT = 8000
    SERVER_PROTOCOL = 'protocol'
    SERVER_SOFTWARE = 'soft'


class RemoteUser:
    REMOTE_ADDR = 'address'
    REMOTE_HOST = 'hostname'
    REMOTE_USER = 'user'


class CGIConnection:

    def __init__(self):
        self.address = RemoteUser.REMOTE_ADDR
        self.host = RemoteUser.REMOTE_HOST
        self.user = RemoteUser.REMOTE_USER
        self.server_name = Server.SERVER_NAME
        self.port = Server.SERVER_PORT
        self.protocol = Server.SERVER_PROTOCOL
        self.software = Server.SERVER_SOFTWARE


# CGIConnection test
cgi = CGIConnection()
print('Адрес пользователя:' + cgi.address)
print('Хост пользователя:' + cgi.host)
print('Имя пользователя:' + cgi.user)
print('Имя сервера:' + cgi.server_name)
print('Порт:' + str(cgi.port))
print('Протокол сервера:' + cgi.protocol)
print('Софт сервера:' + cgi.software)


class Response:

    def __init__(self, REQUEST_METHOD):
        self.REQUEST_METHOD = REQUEST_METHOD

    def doc_response(self):
        return 'Returning Document'

    def local_redirect_response(self):
        return 'Returning Local Redirect'

    def client_redirect_response(self):
        return 'Returning Client Redirect'

    def client_redirect_doc_response(self):
        return 'Returning Client Redirect with Document'

    def response(self):
        if self.REQUEST_METHOD == 1:
            return self.doc_response()
        elif self.REQUEST_METHOD == 2:
            return self.local_redirect_response()
        elif self.REQUEST_METHOD == 3:
            return self.client_redirect_response()
        elif self.REQUEST_METHOD == 4:
            return self.client_redirect_doc_response()


r1 = Response(1)
r2 = Response(2)
r3 = Response(3)
r4 = Response(4)

print(r1.response())
print(r2.response())
print(r3.response())
print(r4.response())