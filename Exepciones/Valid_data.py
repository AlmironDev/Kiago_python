def validar_tipos(valores: dict, tipos: dict):
    """
    Valida que los valores sean del tipo esperado.

    :param valores: Diccionario con los nombres de los parámetros y sus valores.
    :param tipos: Diccionario con los nombres de los parámetros y los tipos esperados.
    :raises ValueError: Si algún valor no coincide con su tipo esperado.
    """
    for nombre, valor in valores.items():
        tipo_esperado = tipos.get(nombre)
        if not isinstance(valor, tipo_esperado):
            raise ValueError(
                f"El parámetro '{nombre}' debe ser de tipo {tipo_esperado.__name__}."
            )
