def Main():
    print('Introduce la ruta en la que se generara el archivo resultado: ')
    f_salida= input()
    CreaClases(f_salida)
    print("Introduce la ruta del fichero a traducir: ")
    f_entrada= input()
    TraduceInstancias(f_salida,f_entrada)
    TraduceReglas(f_salida,f_entrada)
    print('El fichero se ha generado en la ruta '+f_salida)

def CreaClases(f_salida):
    f = open(f_salida+"\\resultado.clp", "w")
    f.write("""(defclass jugador
	    (is-a USER)
	    (slot Nombre (type SYMBOL))
    )

(defclass tablero
	    (is-a USER)
        (slot Nombre (type SYMBOL))
	    (slot x (type INTEGER))
	    (slot y (type INTEGER))
	    (slot estado (type SYMBOL))
    )

(defclass turno
	    (is-a USER)
	    (slot Nombre (type SYMBOL))
    )


    """)
    f.close

def TraduceInstancias(f_salida,f_entrada):
    with open( f_entrada, 'r') as file:
        f = open(f_salida+"\\resultado.clp", "a")
        line = file.readline()
        f.write("(definstances estado-inicial \n");
        while line:
            
            word=str(line).split()
            if ('(init' in word and '(control' in word):
                {
                    f.write("   (of turno (Nombre " + word[2].replace(')','')+"))\n")
                }
            elif ('(init' in word and '(control' not in word and len(word)>=5):
                {
                f.write("   (of tablero (Nombre "+word[1].replace('(','') +")"+ "(x "+word[2]+")"+"(y "+word[3]+")"+"(estado "+word[4].replace(')','')+"))"+"\n")
                }
            if ('(role' in word ):
                {
                    f.write("   (of jugador (Nombre " + word[1].replace(')','')+"))\n")
                }     
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
        while line:
            does=0
            word=str(line).split()
            if ('(<=' in word and '(next' in word):
                array.insert(0,line)
                line = file.readline();
                word=str(line).split()
                if('(control' not in word):
                    condicion=2
                    while(line!="\n"):
                        if('(does' in word):
                            array.insert(1,word[1])
                            does=1
                        elif('(true' in word):
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
                                f.write(" ?ag <- (object (is-a tablero) (Nombre "+word[1].replace('(','')+")(x "+word[2]+")(y "+word[3]+")(estado "+word[4].replace(')','')+"))\n")
                                contador=contador-1
                    else:
                        while(contador>=1):
                                word=str(array[contador]).split()
                                f.write(" ?ag <- (object (is-a tablero) (Nombre "+word[1].replace('(','')+")(x "+word[2]+")(y "+word[3]+")(estado "+word[4].replace(')','')+"))\n")
                                contador=contador-1
                    word=str(array[0]).split()
                    f.write("=>\n(modify ?ag (Nombre "+word[2].replace('(','')+")(x "+word[3]+")(y "+word[4]+")(estado "+word[len(word)-1].replace(')','')+")))\n")
                    acciones+=1
                    array.clear()
                else:
                    print("hola")
            else:
                line = file.readline();
        f.close



Main()




#f.write("\n(defrule inicio\n ?d <- (object (is-a jugador) (Nombre "+word[2]+"))\n")
                    #line = file.readline();
                    #word2=str(line).split()
                    #f.write(" ?ag <- (object (is-a tablero) (Nombre "+word2[1].replace('(','')+")(x ?x)(y ?y)(estado "+word2[len(word2)-1].replace(')','')+"))\n=>\n(modify ?ag (estado "+word[2]+")))\n")
              #line = file.readline();    