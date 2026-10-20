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
    # Completar
    return True