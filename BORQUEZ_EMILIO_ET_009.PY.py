def menu():
    
    planes = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
                #...puede seguir habiendo mas registros
    }
    inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15],
            #...puede seguir habiendo mas registros
    }
    while True:
        print('========== MENÚ PRINCIPAL ==========')
        print('1. Cupos por tipo de plan')
        print('2. Búsqueda de planes por rango de precio')
        print('3. Actualizar precio de plan')
        print('4. Agregar plan')
        print('5. Eliminar plan')
        print('6. Salir')
        print('=====================================')
        try:
            opcion = input('ingrese opcion del 1 al 6: ')
            if opcion =="":
                print('error: opcion no debe quedar vacia')
            elif opcion.strip()=="":
                print('error: no debe contener solo espacios')
            else:
                opcion = int(opcion.strip())
                if opcion not in(1,2,3,4,5,6):
                    print(f'error: la opcion {opcion} no es válida escoga opcion del 1 al 6')
                else:
                    if opcion == 1:
                        cupos_plan(planes, inscripciones)
                    elif opcion == 2:
                        busca_rango_precio_plan(planes, inscripciones)
                        #elif opcion == 3:
                            #actualiza_precio_plan(planes, inscripciones)
                    elif opcion == 4:
                        agrega_nuevo_plan(planes, inscripciones)
                        #elif opcion == 5:
                            #eliminar_plan(planes, inscripciones)
                    elif opcion == 6:
                        print('gracias por usar nuestro software!')
                        exit(0)
        except ValueError as e:
            print('opcion ingresada inválida ingrese un numero del 1 al 6')
            print('error codigo: ', e)
def cupos_plan(planes, inscripciones):
    PLAN_SOLICITADO = input('desea plan trimestral semestral o anual?: ')
    for codigo,datazos in planes
    if PLAN_SOLICITADO == "":
        print('error la opcion no debe estar vacia')
    elif PLAN_SOLICITADO.strip() == "":
        print('error, el plan solicitado no debe contener solo espacios en blanco')
    elif PLAN_SOLICITADO.strip().upper() not in planes.items(codigo[datazos][1]).strip().upper: #estoy intentando enganchar la duracion del plan pero hay un error no se cual es
        print(f'no se encuentran planes {PLAN_SOLICITADO} disponibles en el sistema')
    else:
        detalle_PLAN_SOLICITADO(PLAN_SOLICITADO, planes, inscripciones)

def detalle_PLAN_SOLICITADO(PLAN_SOLICITADO, planes, inscripciones):
    cupos_en_plan = []
    for codigo, datazos, in planes.items():
        if datazos[1].strip().upper() == PLAN_SOLICITADO:
            cupos_en_plan.append(inscripciones[codigo][1], inscripciones[codigo], planes[codigo][0])
    if cupos_en_plan:
        for cupos, precio, nombre in cupos_en_plan:
            print(f'el plan {nombre} de codigo {codigo} tiene un stock de {cupos} con un precio de {precio}')
    else:
        print(f"no se encontraron planes {PLAN_SOLICITADO} disponibles")

def busca_rango_precio_plan(planes, inscripciones):
    precio_min, precio_max = filtro_planes_rango_precio()
    planes_en_rango = []
    for codigo, datazos in inscripciones.items():
        if precio_min <= datazos[0] <= precio_max and (datazos[1]>0):  #igual intento enganchar la duracion del plan pero no puedo
            planes_en_rango.append(inscripciones[codigo][1], inscripciones[codigo], planes[codigo][0])
    if planes_en_rango:
        print(f'planes disponibles entre {precio_min} y {precio_max}:\n')
        print(planes_en_rango)
    for cupos, precio, nombre in planes_en_rango:
        print(f'el plan {nombre} de codigo {codigo} tiene un stock de {cupos} con un precio de {precio}')

def filtro_planes_rango_precio():
    while True:
        precio_min = input('ingrese precio minimo')
        precio_max = input('ingrese precio maximo')
        if precio_min == "" or precio_max == "":
            print('error no debe quedar espacios vacios')
        elif precio_min.strip() =="" or precio_max == "":
            print('no debe tener solo espacios en blanco')
        else:
            try:
                precio_min = float(precio_min)
                precio_max = float(precio_max)
                if precio_min > precio_max:
                    print('error no debe el precio minimo ser mayor que el maximo')
                if precio_min < 0 or precio_max < 0:
                    print('error el precio minimo y maximo no deben ser menores a cero')
                return precio_min, precio_max
            except ValueError as e:
                print('datos ingresados invalidos')
                print('error serie: ', e)

def agrega_nuevo_plan(planes, inscripciones):
    CODIGO_NUEVO = input('ingrese el codigo del nuevo plan')
    NOMBREPLAN_NUEVO = input('ingrese el nombre del plan')
    TIPOPLAN_NUEVO = input('ingrese el tipo de plan nuevo')
    DURACION_NUEVO = input('ingrese la duración del nuevo plan')
    ACCESOPISCINASINO_NUEVO = input('ingrese [si/no] incluye acceso a piscina el nuevo plan')
    SINOCLASES_NUEVO = input('ingrese [si/no] incluye clases el nuevo plan')
    HORARIO_NUEVO = input('ingrese franja horaria nuevo plan')
    PRECIO_INSCRIPCIONES_NUEVO = input('ingrese precio de este plan nuevo')
    STOCK_INSCRIPCIONES_NUEVO = input('ingrese stock de este plan nuevo')
    bool_nombreplan = validar_el_nombreplan(NOMBREPLAN_NUEVO)
    bool_codigoplan = validar_el_codigoplan(CODIGO_NUEVO)
    bool_tipoplan = validar_el_tipoplan(TIPOPLAN_NUEVO)
    bool_duracionplan = validar_la_duracion(DURACION_NUEVO)
    bool_poolsino = validar_la_piscina(ACCESOPISCINASINO_NUEVO)
    bool_clasessino = validar_la_clase(SINOCLASES_NUEVO)
    bool_horario = validar_el_horario(HORARIO_NUEVO)
    bool_stock = validar_el_stock(STOCK_INSCRIPCIONES_NUEVO)
    bool_precio = validar_el_precio(PRECIO_INSCRIPCIONES_NUEVO)

    if  bool_codigoplan and bool_nombreplan and bool_tipoplan and bool_duracionplan and bool_poolsino and bool_clasessino and bool_horario and bool_stock and bool_precio:
        if CODIGO_NUEVO in planes:
            print('error: el codigo de plan ya está registrado en el sistema')
        else:
            ACCESOPISCINASINO_NUEVO = bool(ACCESOPISCINASINO_NUEVO)
            PRECIO_INSCRIPCIONES_NUEVO = int(PRECIO_INSCRIPCIONES_NUEVO)
            STOCK_INSCRIPCIONES_NUEVO = int(STOCK_INSCRIPCIONES_NUEVO)
            planes[CODIGO_NUEVO] = [NOMBREPLAN_NUEVO, TIPOPLAN_NUEVO, DURACION_NUEVO, ACCESOPISCINASINO_NUEVO, SINOCLASES_NUEVO, HORARIO_NUEVO]
            inscripciones[CODIGO_NUEVO] = [PRECIO_INSCRIPCIONES_NUEVO, STOCK_INSCRIPCIONES_NUEVO]
            print(planes[CODIGO_NUEVO], inscripciones[CODIGO_NUEVO])
            print('se ha agregado el nuevo plan exitosamente!')
def validar_el_nombreplan(NOMBREPLAN_NUEVO):
    if NOMBREPLAN_NUEVO == "":
        print('no debe estar vacio el nombre del plan nuevo')
    elif NOMBREPLAN_NUEVO.strip() == "":
        print('no debe contener solo espacios en blanco')
    else:
        return True
def validar_el_codigoplan(CODIGO_NUEVO):
    if CODIGO_NUEVO == "":
        print('no debe estr vacio el codigo nuevo del plan')
    elif CODIGO_NUEVO.strip() == "":
        print('no debe tener solo espacios en blanco el codigo del nuevo plan')
    else:
        return True
def validar_el_tipoplan(TIPOPLAN_NUEVO):
    TIPOPLAN_NUEVO = input('ingrese opcion TRIMESTRAL MENSUAL O ANUAL: ')
    if TIPOPLAN_NUEVO == "":
        print('no debe estr vacio el codigo nuevo del plan')
    elif TIPOPLAN_NUEVO.strip() == "":
        print('no debe tener solo espacios en blanco el codigo del nuevo plan')
    else:
        try:
            TIPOPLAN_NUEVO = int(TIPOPLAN_NUEVO.strip())
            if TIPOPLAN_NUEVO.upper() == "TRIMESTRAL" or "MENSUAL" or "ANUAL":
                print(f'error: la opcion {TIPOPLAN_NUEVO} no es válida escoga opcion del 1 al 6')
            else:
                print(f'error: la opcion {TIPOPLAN_NUEVO} no es válida escoga opcion TRIMESTRAL, MENSUAL O ANUAL')
        except ValueError as e:
            print('opcion ingresada inválida escoga una opcion TRIMESTRAL, MENSUAL O ANUAL')
            print('error codigo: ', e)
def validar_la_duracion(DURACION_NUEVO):
    if DURACION_NUEVO == "":
        print('no debe estr vacio el codigo nuevo del plan')
    elif DURACION_NUEVO.strip() == "":
        print('no debe tener solo espacios en blanco el codigo del nuevo plan')
    else:
        try:
            DURACION_NUEVO = int(DURACION_NUEVO)
            if DURACION_NUEVO > 0:
                return True
        except ValueError as e:
            print('error: duración invalida, debes escoger una duracion mayor a cero')
            print('detalle del error: ', e)
def validar_la_piscina(ACCESOPISCINASINO_NUEVO):
    if ACCESOPISCINASINO_NUEVO == "":
        print('no debe estar en blanco esta opcion, porfavor eliga: [s/n]: ')
    elif ACCESOPISCINASINO_NUEVO.strip()=="":
        print('esta opcion no debe tener solo espacios en blanco, porfavor eliga: [s/n]: ')
    else:
        try:
            if ACCESOPISCINASINO_NUEVO.strip().upper() == "S":
                return True
            elif ACCESOPISCINASINO_NUEVO.strip().upper() == "N":
                return False
        except ValueError as e:
            print('opcion invalida, porfavor ingresa [s/n]')
            print('codigo de error: ', e)
def validar_la_clase(SINOCLASES_NUEVO):
    if SINOCLASES_NUEVO == "":
        print('no debe estar en blanco esta opcion, porfavor eliga: [s/n]: ')
    elif SINOCLASES_NUEVO.strip()=="":
        print('esta opcion no debe tener solo espacios en blanco, porfavor eliga: [s/n]: ')
    else:
        try:
            if SINOCLASES_NUEVO.strip().upper() == "S":
                return True
            elif SINOCLASES_NUEVO.strip().upper() == "N":
                return False
        except ValueError as e:
            print('opcion invalida, porfavor ingresa [s/n]')
            print('codigo de error: ', e)
def validar_el_horario(HORARIO_NUEVO):
    if HORARIO_NUEVO == "":
        print('no debe estr vacio el codigo nuevo del plan')
    elif HORARIO_NUEVO.strip() == "":
        print('no debe tener solo espacios en blanco el codigo del nuevo plan')
    else:
        try:
            HORARIO_NUEVO = int(HORARIO_NUEVO)
            if HORARIO_NUEVO > 0:
                return True
        except ValueError as e:
            print('error: duración invalida, debes escoger una duracion mayor a cero')
            print('detalle del error: ', e)
def validar_el_precio(PRECIO_INSCRIPCIONES_NUEVO):
    if PRECIO_INSCRIPCIONES_NUEVO == "":
        print('no debe estr vacio el codigo nuevo del plan')
    elif PRECIO_INSCRIPCIONES_NUEVO.strip() == "":
        print('no debe tener solo espacios en blanco el codigo del nuevo plan')
    else:
        try:
            PRECIO_INSCRIPCIONES_NUEVO = int(PRECIO_INSCRIPCIONES_NUEVO)
            if PRECIO_INSCRIPCIONES_NUEVO > 0:
                return True
        except ValueError as e:
            print('error: duración invalida, debes escoger una duracion mayor a cero')
            print('detalle del error: ', e)
def validar_el_stock(STOCK_INSCRIPCIONES_NUEVO):
    if STOCK_INSCRIPCIONES_NUEVO == "":
        print('no debe estr vacio el codigo nuevo del plan')
    elif STOCK_INSCRIPCIONES_NUEVO.strip() == "":
        print('no debe tener solo espacios en blanco el codigo del nuevo plan')
    else:
        try:
            STOCK_INSCRIPCIONES_NUEVO = int(STOCK_INSCRIPCIONES_NUEVO)
            if STOCK_INSCRIPCIONES_NUEVO > 0:
                return True
        except ValueError as e:
            print('error: duración invalida, debes escoger una duracion mayor a cero')
            print('detalle del error: ', e)

menu()



