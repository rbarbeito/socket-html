import socket, os

import misfunciones as mf

HOST="0.0.0.0"
PORT=65432

pid = os.getpid()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST,PORT))
    s.listen()
    
    print("{}> Esperando conexión....".format(pid))
    
    while True:
        
        conn, addr= s.accept()

        with conn: 
            print("{}> Cliente conectado desde... {}".format(pid,addr))
            
            data = conn.recv(1024)

            print(data.decode().split('\r\n'))

            
            metodo, ruta, protocolo = data.decode('utf-8').split('\r\n')[0].split(' ')
            
            if ruta == '/':
            
                if metodo == 'GET':
                    with open('login.html', 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        
                    contenido = mf.cabecera(len(contenido), False, 'html') + contenido
                    conn.sendall(contenido.encode('utf-8'))
                
                elif metodo == "POST":
                    pass
                
                else:
                    pass  
                
            elif ruta == '/login':
                
                if metodo =='GET':
                    pass 
                
                elif metodo =='POST':
                    campos = data.decode('utf-8').split('\r\n')[-1].split('&')
                     
                    email = mf.convertir_ascii(campos[0].split('=')[-1])
                    passwd = mf.convertir_ascii(campos[1].split('=')[-1])

                    datos_user=dict()
                     
                    for campo in campos:
                        forma = mf.convertir_ascii(campo).split('=')
                        datos_user[forma[0]]=forma[1]

                    if datos_user["email"]=='xx@xx.com':

                        if datos_user['password'] == '123456':
                            content="<html ><head><meta charset='UTF-8'></head><body><h1>OK, makey</h1></body></html>"
                            contenido = mf.cabecera(len(content),True,'html') + content
                            conn.sendall(contenido.encode('utf-8'))
                        else:
                            content="<html ><head><meta charset='UTF-8'></head><body><h1>Error de usuario y/o contraseña</h1></body></html>"
                            contenido = mf.cabecera(len(content),False,'html') + content
                            conn.sendall(contenido.encode('utf-8'))
                    else:
                            content="<html ><head><meta charset='UTF-8'></head><body><h1>Error de usuario y/o contraseña</h1></body></html>"
                            contenido = mf.cabecera(len(content),False,'html') + content
                            conn.sendall(contenido.encode('utf-8'))
                            

                    
                else:
                    pass  
                   
            else:
                
                extension = ruta.split('/')[-1].split('.')[-1]

                                
                if extension in ['css','js']:
                    with open('.'+ruta,'r') as f:
                        archivo = f.read()
                        
                    archivo = mf.cabecera(len(archivo), False ,extension) + archivo
                    conn.sendall(archivo.encode('utf-8'))  
                
        
        
        
