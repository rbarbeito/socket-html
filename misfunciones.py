from datetime import datetime, timedelta, time
from urllib.parse import unquote

def cabecera(contentlength, cookie, archivo):
    cabecera = 'HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Length: {}\r\nContent-Type: {}; chartset=utf-8\r\n{}\r\n\r\n'''.format(contentlength, tipos_mime(archivo),addcookie(cookie))
    return cabecera



def tipos_mime(archivo):
    
    tiposmime={
        "html":"text/html",
        "js":"text/javascript",
        'css':'text/css'
    }
    
    return tiposmime[archivo]



def addcookie(cookie):

    if cookie == True:
        return "Set-Cookie: id=a3fWa; Expires={};".format(tiempo_cookie())
    
    return ''



def tiempo_cookie():
    dt = datetime.now() + timedelta(minutes=10)

    return dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

def convertir_ascii(texto):
    return unquote(texto).replace('+', " ")



    
