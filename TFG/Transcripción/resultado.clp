(defclass jugador
	    (is-a USER)
	    (slot Nombre (type SYMBOL))
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


    (definstances estado-inicial 
   (of jugador (Nombre x))
   (of jugador (Nombre o))
   (of tablero (x 1) (y 1) (estado b))
   (of tablero (x 1) (y 2) (estado b))
   (of tablero (x 1) (y 3) (estado b))
   (of tablero (x 2) (y 1) (estado b))
   (of tablero (x 2) (y 2) (estado b))
   (of tablero (x 2) (y 3) (estado b))
   (of tablero (x 3) (y 1) (estado b))
   (of tablero (x 3) (y 2) (estado b))
   (of tablero (x 3) (y 3) (estado b))
   (of turno (Nombre x))
)