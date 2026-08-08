ids = []
nombres = []
categorias = []
descripciones = []
cantidades = []
estados = []
fechas = []
responsables = []
observaciones = []
historial_ids = []
historial_tipos = []
historial_fechas = []
#----------------------------------------------#
#--|menu_principal_autogenerador_de_reportes|--#
#----------------------------------------------#
while True:
    print("menu principal autogenerador de reportes")
    print("1) registrar información")
    print("2) editar información")
    print("3) eliminar información")
    print("4) buscar información")
    print("5) generar reporte general")
    print("6) generar reporte por estado")
    print("7) generar reporte por categoría")
    print("8) historial de reportes")
    print("9) lista de datos")
    print("10) salir")
    opcion = input("seleccione una opción: ")
    #---------------------------#
    #--|registrar_informacion|--#
    #---------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_registro = 1
        else:
            id_registro = ids[-1] + 1
        nombre = input("nombre: ")
        categoria = input("categoría: ")
        descripcion = input("descripción: ")
        try:
            cantidad = int(input("cantidad: "))
        except ValueError:
            cantidad = 0
        print("estados")
        print("1) disponible")
        print("2) pendiente")
        print("3) agotado")
        opcion_estado = input(
            "seleccione el estado: "
        )
        if opcion_estado == "1":
            estado = "disponible"
        elif opcion_estado == "2":
            estado = "pendiente"
        elif opcion_estado == "3":
            estado = "agotado"
        else:
            estado = "pendiente"
        fecha = input("fecha: ")
        responsable = input("responsable: ")
        observacion = input("observación: ")
        ids.append(id_registro)
        nombres.append(nombre)
        categorias.append(categoria)
        descripciones.append(descripcion)
        cantidades.append(cantidad)
        estados.append(estado)
        fechas.append(fecha)
        responsables.append(responsable)
        observaciones.append(observacion)
        print("información registrada correctamente.")
        print("id:", id_registro)
    #------------------------#
    #--|editar_informacion|--#
    #------------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar información")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{categorias[i]} | "
                    f"{cantidades[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("nombre:", nombres[posicion])
                print(
                    "categoría:",
                    categorias[posicion]
                )
                print(
                    "descripción:",
                    descripciones[posicion]
                )
                print(
                    "cantidad:",
                    cantidades[posicion]
                )
                print(
                    "estado:",
                    estados[posicion]
                )
                print(
                    "fecha:",
                    fechas[posicion]
                )
                print(
                    "responsable:",
                    responsables[posicion]
                )
                print(
                    "observación:",
                    observaciones[posicion]
                )
                nombres[posicion] = input(
                    "nuevo nombre: "
                )
                categorias[posicion] = input(
                    "nueva categoría: "
                )
                descripciones[posicion] = input(
                    "nueva descripción: "
                )
                try:
                    cantidades[posicion] = int(
                        input("nueva cantidad: ")
                    )
                except ValueError:
                    cantidades[posicion] = 0
                print("estados")
                print("1) disponible")
                print("2) pendiente")
                print("3) agotado")
                opcion_estado = input(
                    "seleccione el estado: "
                )
                if opcion_estado == "1":
                    estados[posicion] = "disponible"
                elif opcion_estado == "2":
                    estados[posicion] = "pendiente"
                elif opcion_estado == "3":
                    estados[posicion] = "agotado"
                else:
                    estados[posicion] = "pendiente"
                fechas[posicion] = input(
                    "nueva fecha: "
                )
                responsables[posicion] = input(
                    "nuevo responsable: "
                )
                observaciones[posicion] = input(
                    "nueva observación: "
                )
                print(
                    "información actualizada correctamente."
                )
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|eliminar_informacion|--#
    #--------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar información")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{categorias[i]} | "
                    f"{estados[i]}"
                )
            id_buscar = int(
                input("ingrese la id: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print(
                    "nombre:",
                    nombres[posicion]
                )
                print(
                    "categoría:",
                    categorias[posicion]
                )
                confirmacion = input(
                    "¿desea eliminar este registro? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    descripciones.pop(posicion)
                    cantidades.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    responsables.pop(posicion)
                    observaciones.pop(posicion)
                    print(
                        "registro eliminado correctamente."
                    )
                else:
                    print(
                        "el registro no fue eliminado."
                    )
            else:
                print("id no encontrada.")
    #------------------------#
    #--|buscar_informacion|--#
    #------------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            id_buscar = int(
                input("ingrese la id: ")
            )
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("información del registro")
                print("id:", ids[posicion])
                print(
                    "nombre:",
                    nombres[posicion]
                )
                print(
                    "categoría:",
                    categorias[posicion]
                )
                print(
                    "descripción:",
                    descripciones[posicion]
                )
                print(
                    "cantidad:",
                    cantidades[posicion]
                )
                print(
                    "estado:",
                    estados[posicion]
                )
                print(
                    "fecha:",
                    fechas[posicion]
                )
                print(
                    "responsable:",
                    responsables[posicion]
                )
                print(
                    "observación:",
                    observaciones[posicion]
                )
            else:
                print("id no encontrada.")
    #-----------------------------#
    #--|generar_reporte_general|--#
    #-----------------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            total_cantidad = 0
            disponibles = 0
            pendientes = 0
            agotados = 0
            categorias_temporales = []
            cantidades_categorias = []
            for i in range(len(ids)):
                total_cantidad += cantidades[i]
                if estados[i] == "disponible":
                    disponibles += 1
                elif estados[i] == "pendiente":
                    pendientes += 1
                elif estados[i] == "agotado":
                    agotados += 1
                if categorias[i] in categorias_temporales:
                    posicion_categoria = (
                        categorias_temporales.index(
                            categorias[i]
                        )
                    )
                    cantidades_categorias[
                        posicion_categoria
                    ] += cantidades[i]
                else:
                    categorias_temporales.append(
                        categorias[i]
                    )
                    cantidades_categorias.append(
                        cantidades[i]
                    )
            print("reporte general")
            print(
                "total de registros:",
                len(ids)
            )
            print(
                "cantidad total:",
                total_cantidad
            )
            print(
                "disponibles:",
                disponibles
            )
            print(
                "pendientes:",
                pendientes
            )
            print(
                "agotados:",
                agotados
            )
            if len(ids) > 0:
                promedio = total_cantidad / len(ids)
                print(
                    "cantidad promedio:",
                    round(promedio, 2)
                )
            print("cantidad por categoría")
            for i in range(
                len(categorias_temporales)
            ):
                print(
                    categorias_temporales[i],
                    ":",
                    cantidades_categorias[i]
                )
            if len(categorias_temporales) > 0:
                mayor = cantidades_categorias[0]
                categoria_mayor = (
                    categorias_temporales[0]
                )
                for i in range(
                    1,
                    len(cantidades_categorias)
                ):
                    if (
                        cantidades_categorias[i]
                        > mayor
                    ):
                        mayor = (
                            cantidades_categorias[i]
                        )
                        categoria_mayor = (
                            categorias_temporales[i]
                        )
                print(
                    "categoría con mayor cantidad:",
                    categoria_mayor
                )
                print(
                    "cantidad:",
                    mayor
                )
            if len(historial_ids) == 0:
                id_historial = 1
            else:
                id_historial = (
                    historial_ids[-1] + 1
                )
            historial_ids.append(id_historial)
            historial_tipos.append(
                "reporte general"
            )
            fecha_reporte = input(
                "ingrese la fecha del reporte: "
            )
            historial_fechas.append(
                fecha_reporte
            )
            print(
                "reporte general generado correctamente."
            )
    #------------------------#
    #--|reporte_por_estado|--#
    #------------------------#
    elif opcion == "6":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("reporte por estado")
            print("1) disponible")
            print("2) pendiente")
            print("3) agotado")
            opcion_estado = input(
                "seleccione el estado: "
            )
            if opcion_estado == "1":
                estado_buscar = "disponible"
            elif opcion_estado == "2":
                estado_buscar = "pendiente"
            elif opcion_estado == "3":
                estado_buscar = "agotado"
            else:
                estado_buscar = ""
            if estado_buscar != "":
                encontrados = 0
                cantidad_total = 0
                print(
                    "reporte:",
                    estado_buscar
                )
                for i in range(len(ids)):
                    if (
                        estados[i]
                        == estado_buscar
                    ):
                        print(
                            f"{ids[i]} | "
                            f"{nombres[i]} | "
                            f"{categorias[i]} | "
                            f"{cantidades[i]}"
                        )
                        encontrados += 1
                        cantidad_total += (
                            cantidades[i]
                        )
                print(
                    "total de registros:",
                    encontrados
                )
                print(
                    "cantidad total:",
                    cantidad_total
                )
                if len(historial_ids) == 0:
                    id_historial = 1
                else:
                    id_historial = (
                        historial_ids[-1] + 1
                    )
                historial_ids.append(
                    id_historial
                )
                historial_tipos.append(
                    "reporte por estado"
                )
                fecha_reporte = input(
                    "ingrese la fecha del reporte: "
                )
                historial_fechas.append(
                    fecha_reporte
                )
                print("reporte por estado generado correctamente.")
            else:
                print("opción no válida.")
    #---------------------------#
    #--|reporte_por_categoria|--#
    #---------------------------#
    elif opcion == "7":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            categorias_disponibles = []
            for i in range(len(categorias)):
                if (
                    categorias[i]
                    not in categorias_disponibles
                ):
                    categorias_disponibles.append(
                        categorias[i]
                    )
            print("categorías disponibles")
            for i in range(
                len(categorias_disponibles)
            ):
                print(
                    f"{i + 1}) "
                    f"{categorias_disponibles[i]}"
                )
            opcion_categoria = int(
                input("seleccione una categoría: ")
            )
            if (
                opcion_categoria >= 1
                and
                opcion_categoria <=
                len(categorias_disponibles)
            ):
                categoria_buscar = (
                    categorias_disponibles[
                        opcion_categoria - 1
                    ]
                )
                encontrados = 0
                cantidad_total = 0
                print(
                    "reporte:",
                    categoria_buscar
                )
                for i in range(len(ids)):
                    if (
                        categorias[i]
                        == categoria_buscar
                    ):
                        print(
                            f"{ids[i]} | "
                            f"{nombres[i]} | "
                            f"{cantidades[i]} | "
                            f"{estados[i]}"
                        )
                        encontrados += 1
                        cantidad_total += (
                            cantidades[i]
                        )
                print(
                    "total de registros:",
                    encontrados
                )
                print(
                    "cantidad total:",
                    cantidad_total
                )
                if len(historial_ids) == 0:
                    id_historial = 1
                else:
                    id_historial = (
                        historial_ids[-1] + 1
                    )
                historial_ids.append(
                    id_historial
                )
                historial_tipos.append(
                    "reporte por categoría"
                )
                fecha_reporte = input(
                    "ingrese la fecha del reporte: "
                )
                historial_fechas.append(
                    fecha_reporte
                )
                print(
                    "reporte por categoría generado correctamente."
                )
            else:
                print("categoría no válida.")
    #---------------------------#
    #--|historial_de_reportes|--#
    #---------------------------#
    elif opcion == "8":
        if len(historial_ids) == 0:
            print(
                "no existen reportes generados."
            )
        else:
            print("historial de reportes")
            for i in range(
                len(historial_ids)
            ):
                print(
                    f"{historial_ids[i]} | "
                    f"{historial_tipos[i]} | "
                    f"{historial_fechas[i]}")
            print("total de reportes generados:", len(historial_ids))
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "9":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            disponibles = 0
            pendientes = 0
            agotados = 0
            cantidad_total = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | "
                    f"{nombres[i]} | "
                    f"{categorias[i]} | "
                    f"{cantidades[i]} | "
                    f"{estados[i]}"
                )
                cantidad_total += cantidades[i]
                if estados[i] == "disponible":
                    disponibles += 1
                elif estados[i] == "pendiente":
                    pendientes += 1
                elif estados[i] == "agotado":
                    agotados += 1
            print("estadísticas")
            print("registros:", len(ids))
            print("cantidad total:", cantidad_total)
            print("disponibles:", disponibles)
            print("pendientes:", pendientes)
            print("agotados:", agotados)
            if len(ids) > 0:
                promedio = (cantidad_total / len(ids))
                print("cantidad promedio:", round(promedio, 2))
            print("reportes generados:", len(historial_ids))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "10":
        print("gracias por utilizar el autogenerador de reportes.")
        break
    else:
        print("opción no válida.")