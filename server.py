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
            
            metodo, ruta, protocolo = data.decode('utf-8').split('\r\n')[0].split(' ')
            
            if ruta == '/':
            
                if metodo == 'GET':
                    with open('login.html', 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        
                    contenido = mf.cabecera(len(contenido), True) + contenido
                    conn.sendall(contenido.encode('utf-8'))
                
                elif metodo == "POST":
                    pass
                
                else:
                    pass  
                
            elif ruta == 'login':
                
                if metodo =='GET':
                    pass 
                
                elif metodo =='POST':
                    pass
                
                else:
                    pass  
                   
            else:
                
                extension = ruta.split('/')[-1].split('.')[-1]
                
                if extension in ['css','js']:
                    with open('.'+ruta,'r') as f:
                        archivo = f.read()
                        
                    archivo = mf.cabecera(len(archivo),extension) + archivo
                    conn.sendall(archivo.encode('utf-8'))  
                
        
        
        