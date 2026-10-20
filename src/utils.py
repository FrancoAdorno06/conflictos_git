import re

def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    # ################
    # El profe hizo
    # ################

    patron_id = r"[1-9][0-9]*"
    return bool(re.fullmatch(patron_id, id_usuario))

    #return id_usuario.isdigit()

def validar_nombre(nombre:str):
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    # Franco Adorno
    if nombre is None or not isinstance(nombre, str):
        return False
    nombre = nombre.strip()
    if not nombre:
        return False

    return all(c.isalpha()or c == "" for c in nombre)
    return True

def validar_email(email:str):
    """
    Valida que email sea un correo válido"""
    # Definimos el patrón exacto que debe tener un email
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    # re.fullmatch busca que TODO el email coincida con el patrón.
    # Si coincide devuelve un objeto, si falla devuelve None.
    return re.fullmatch(patron, email) is not None
