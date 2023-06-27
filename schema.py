def coneccion(host, user, password):
    import telnetlib
    tn = telnetlib.Telnet(host)
    tn.read_until(b"name:")
    tn.write(user.encode('ascii') + b"\r")
    tn.read_until(b"word:")
    tn.write(password.encode('ascii') + b"\r")
    a = tn.read_until(b">").decode("utf-8")
    tn.write(b"enable\r")
    a = tn.read_until(b"#").decode("utf-8")
    return tn


def leercomandos(comandos):
    lista = []
    if (".txt" not in comandos):
        comandos = comandos+".txt"
    with open(comandos, 'r') as file:
        for linea in file:
            linea = linea.strip()
            lista.append(linea)
    return lista


def guardarcomandos(data, archivoguardar, c, modoacceso='a',):
    if (".txt" not in archivoguardar):
        archivoguardar = archivoguardar+".txt"
    with open(archivoguardar, modoacceso) as file:
        file.write(data)
        # file.write('\n----------\n')
        file.write('\n------------'+c+'------------\n')


def traerarchivo():
    from ftplib import FTP
    servidor = '10.115.72.128'
    usuario = 'tellabs'
    contrasena = 'umts2008'
    # Crear una instancia de la clase FTP y conectarse al servidor
    ftp = FTP(servidor)
    ftp.login(usuario, contrasena)
    # Cambiar al directorio deseado en el servidor FTP
    directorio = '/flash/debug/log'
    ftp.cwd(directorio)
    # Nombre del archivo a extraer
    nombre_archivo = 'PerfEvent_u1_1718.txt'
    # Crear un archivo local para guardar los datos del archivo extraído
    archivo_local = open(nombre_archivo, 'wb')
    # Extraer el archivo desde el servidor FTP y guardarlo en el archivo local
    ftp.retrbinary('RETR ' + nombre_archivo, archivo_local.write)
    # Cerrar la conexión FTP y el archivo local
    ftp.quit()
    archivo_local.close()
    print('El archivo', nombre_archivo,
          'ha sido extraído correctamente desde el servidor FTP.')
    
#/flash/appl-sw
# se guarda el software
#/flash/snapshot-config
#se guarda el backup
def subirarchivo():
    #!/usr/bin/env python
    import ftplib
    import os
    # Datos FTP
    servidor = '10.115.72.128'
    usuario = 'tellabs'
    contrasena = 'umts2008'
    ftp_raiz = '/flash/debug/log'  # donde queremos subir el fichero

    # Datos del fichero a subir
    #fichero_origen = '/home/gorka/mifichero.zip'
    fichero_origen = 'comandos.txt'
    fichero_destino = 'comandos.txt'
    # Conectamos con el servidor
    try:
        s = ftplib.FTP(servidor, usuario, contrasena)
        try:
            f = open(fichero_origen, 'rb')
            s.cwd(ftp_raiz)
            s.storbinary('STOR ' + fichero_destino, f)
            f.close()
            s.quit()
            print("se subió correctamente el archivo al servidor "+servidor)
        except:
            print("No se ha podido encontrar el fichero " + fichero_origen)
    except:
        print("No se ha podido conectar al servidor " + servidor)
 