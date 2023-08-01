def Main():
    print('Introduce la ruta en la que se generara el archivo resultado: ')
    f_salida= input()
    CreaClases(f_salida)
    print("Introduce la ruta del fichero a traducir: ")
    f_entrada= input()
    TraduceInstancias(f_salida,f_entrada)
    #TraduceReglas(f_salida,f_entrada)
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
        to_search = "role(x)"
        f.write("(definstances estado-inicial \n");
        while line:
            line = file.readline();
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
                    

                
            #(x "+ str(line[line.find(" ") + 1:line.rfind(" ")])+") (y "+ str(line[line.find(" ") + 1:line.rfind(" ")])+") (estado "+str(line[line.rfind(" ")+1:line.rfind(")")])+ "))
            #elif("role" in line):{f.write("   (of jugador (Nombre " + str(line[line.find("(")+1  :line.find(")")]) + "))\n")}
        f.write(")");
        f.close



Main()