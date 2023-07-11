f = open("ejem.clp", "w")
f.write("""(defclass jugador
	(is-a USER)
	(slot Paciente (type SYMBOL))
)

(defclass tablero
	(is-a USER)
	(slot x (type INTEGER))
	(slot y (type INTEGER))
	(slot estado (type SYMBOL))
)

(defclass turno
	(is-a USER)
	(slot Nombre (type SYMBOL))
)


""")

with open('tic-tac-toe.gdl', 'r') as file:
    line = file.readline()
    to_search = "role(x)"
    f.write("(definstances estado-inicial \n");
    while line:
        line = file.readline();

        if ("init(control(" in line):
            {
                f.write("   (of turno (Nombre " + str(line[line.find("(") + 8:line.find(")")]) + "))\n")
            }
        else:
            if ("init" in line): {
                f.write("   (of tablero (x "+str(line[line.find("(") + 1:line.find(",")]) +") (y "+ str(line[line.find(",") + 1:line.rfind(",")])+") (estado "+str(line[line.rfind(",")+1:line.rfind(")")])+ "))\n")

            }
    f.write(")");
