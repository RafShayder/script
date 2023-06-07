from schema import *
comandos=leercomandos("comandos.txt")
host = "10.115.72.128"
user = "tellabs"
password = 'umts2008'
tn=coneccion(host,user,password)
i =1;
for c in comandos:
    lu="{comand}\r".format(comand=c)
    tn.write(bytes(lu,"utf-8"))
    pro=str(tn.read_until(b"#").decode("utf-8")) 
    guardarcomandos(pro,"prueba.txt",c,)
    print(c)
traerarchivo()
subirarchivo()
tn.write(b"exit\r")
tn.close()


