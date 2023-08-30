import string
import os
def Main():
   try:
      print('Introduce la ruta en la que se generara el archivo resultado: ')
      f_salida= input()
      ejem=os.path.isdir(f_salida)
      ejem2= os.path.exists(f_salida)
      if(not os.path.exists(f_salida) or not os.path.isdir(f_salida)):
          print('La ruta introducida no es valida. Vuelve a intentarlo')
          return
   except:
       print('No se ha podido acceder a la ruta debido a un error comprueba la ruta y vuelve a intentarlo.')
       return
   try:
       print("Introduce la ruta del fichero a traducir: ")
       f_entrada= input()
       if(not os.path.exists(f_entrada) or not os.path.isfile(f_entrada)):
          print('La ruta introducida no es valida. Vuelve a intentarlo.')
          return
   except:
       print('No se ha podido acceder a la ruta debido a un error comprueba la ruta y vuelve a intentarlo.')
       return
   CreaClases(f_salida)
   TraduceInstancias(f_salida,f_entrada)
   TraduceHechos(f_salida,f_entrada)
   TraduceReglas(f_salida,f_entrada)
   print('El fichero se ha generado en la ruta '+f_salida)

def CreaClases(f_salida):
    f = open(f_salida+"\\resultado.clp", "w")
    f.write("""(defclass jugador
	    (is-a USER)
	    (slot Nombre (type SYMBOL))
    )

(defclass turno
	    (is-a USER)
	    (slot Nombre (type SYMBOL))
    )\n""")
    f.close

def TraduceInstancias(f_salida,f_entrada):
    with open( f_entrada, 'r') as file:
        f = open(f_salida+"\\resultado.clp", "a")
        line = file.readline()
        f.write("\n(definstances estado-inicial \n");
        while line:
            
            word=str(line).split()
            if ('(init' in word and '(control' in word):
                {
                    f.write("   (of turno (Nombre " + word[2].replace(')','')+"))\n")
                }
            if ('(role' in word and '?' not in line):
                {
                    f.write("   (of jugador (Nombre " + word[1].replace(')','')+"))\n")
                }     
            line = file.readline();
        f.write(")");
        f.close

def TraduceHechos(f_salida,f_entrada):
    with open( f_entrada, 'r') as file:
        f = open(f_salida+"\\resultado.clp", "a")
        line = file.readline()
        f.write("\n(deffacts hechos-iniciales \n");
        while line:
            
            word=str(line).split()
            if ('(init' in word and '(control' not in word ):
                f.write(line.replace('(init ','').replace(')','').replace('\n','')+")\n")
            line = file.readline();
        f.write(")");
        f.close


def TraduceReglas(f_salida,f_entrada):
    with open( f_entrada, 'r') as file:
        f = open(f_salida+"\\resultado.clp", "a")
        line = file.readline()
        word=str(line).split()
        array=list()
        acciones=1
        goal=1
        abecedario_minusculas = list(string.ascii_lowercase)
        while line:
            does=0
            word=str(line).split()
            if ('(<=' in word and '(next' in word):
                array.insert(0,line)
                line = file.readline();
                word=str(line).split()
                condiciones=""
                if('(control' not in word):
                    condicion=2
                    while(line!="\n"):
                        if('(does' in word):
                            array.insert(1,word[1])
                            does=1
                        else:
                            array.insert(condicion,line)
                            condicion+=1
                        line = file.readline();
                        word=str(line).split()
                    contador=len(array)-1
                    f.write("\n(defrule accion"+str(acciones)+"\n")
                    if(does==1):
                        f.write("?d <- (object (is-a jugador) (Nombre "+array[1]+"))\n")
                        while(contador>1):
                            word=str(array[contador]).split()
                            if('(not' not in word):
                                word='?'+abecedario_minusculas[contador]+' <- '+str(array[contador])+''
                                condiciones=condiciones+word.replace('(true ','').replace(')','').replace('\n','')+")\n"
                                f.write(condiciones.replace('(or',''))
                                contador=contador-1
                                line = file.readline();
                            else:
                                word=str(array[contador])
                                condiciones=condiciones+word.replace('(true ','').replace(')','').replace('\n','')+"))\n"
                                f.write(condiciones.replace('(or',''))
                                contador=contador-1
                                line = file.readline();
                    else:
                        while(contador>=1):
                            word=str(array[contador]).split()
                            if('(not' not in word):
                                word='?'+abecedario_minusculas[contador]+' <- '+str(array[contador])+''
                                condiciones=condiciones+word.replace('(true ','').replace(')','').replace('\n','')+")\n"
                                f.write(condiciones.replace('(or',''))
                                contador=contador-1
                                line = file.readline();
                            else:
                                word=str(array[contador])
                                condiciones=condiciones+word.replace('(true ','').replace(')','').replace('\n','')+"))\n"
                                f.write(condiciones.replace('(or',''))
                                contador=contador-1
                                line = file.readline();
                    word=str(array[0])
                    f.write("=>\n(assert "+word.replace('(<= (next','').replace(')','').replace('\n','')+")))\n")
                    acciones+=1
                    array.clear()
                

            elif('(<=' in word and '(goal' not in word and 'terminal' not in word and '(legal' not in word):
                fact=line
                line = file.readline();
                contador=0
                condiciones=""
                while(line!="\n" and line!=")\n" and len(line) != 0):
                    contador+=1
                    word=str(line).split()
                    if('(true' in word):
                        line='?'+abecedario_minusculas[contador]+' <- '+line+''
                        condiciones=condiciones+line.replace('(true ','').replace(')','').replace('\n','')+")\n"
                    elif('(not' not in word):
                        line='?'+abecedario_minusculas[contador]+' <- '+line+''
                        condiciones=condiciones+line.replace(')','').replace('\n','')+")\n"
                    else:
                       condiciones=condiciones+line.replace(')','').replace('\n','')+"))\n"
                    line = file.readline();
                if(condiciones!=""):
                    condiciones=condiciones.replace('(or','')
                    f.write("\n(defrule accion"+str(acciones)+"\n")
                    f.write(condiciones)
                    f.write("=>\n(assert "+fact.replace('(<= ','')+"))\n")
                    acciones+=1
            elif ('(<=' in word and '(goal' in word):
                fact=line
                line = file.readline();
                
                f.write("\n(defrule goal"+str(goal)+"\n")
                goal+=1
                while(line!="\n" and line!=")\n" and len(line) != 0):
                    contador+=1
                    word=str(line).split()
                    if('(not' not in word):
                        line='?a <- '+line+''
                        f.write(line.replace(')','').replace('\n','')+")\n")
                    else:
                        f.write(line.replace(')','').replace('\n','')+"))\n")
                    line = file.readline();
                f.write("=>\n(assert "+fact.replace('(<= ','')+"))\n")
            
            else:
                line = file.readline();
        f.close



Main()

