
def cabecera(contentlength, cookie=False, archivo='html'):
    
    cabecera = '''HTTP/1.1 200 OK
                        Server: Apache
                        Content-Length: {}
                        Content-Type: {}; chartset=utf-8
                        Set-Cookie: id=a3fWa; Max-Age=2592000\r\n\r\n'''.format(contentlength, tipos_mime(archivo))

    return cabecera

def tipos_mime(archivo):
    
    tiposmime={
        "html":"text/html",
        "js":"text/javascript",
        'css':'text/css'
    }
    
    return tiposmime[archivo]

def addcookie(cookie):
    print(cookie)
    if cookie == True:
        return "Set-Cookie: id=a3fWa; Max-Age=2592000"
    
    return ''