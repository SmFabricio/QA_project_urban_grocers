import sender_stand_request
import data

# Función para cambiar el nombre del kit
def get_kit_body(kit_name):
    # Copia el kit name desde el archivo de datos
    current_kit_body = data.kit_body.copy()
    # Para cambiar el valor del parámetro name
    current_kit_body["name"] = kit_name
    return current_kit_body

# Función para generar encabezados con "Authorization"
def get_new_user_autoken():
    # Obtiene una copia de los datos del usuario nuevo
    new_user = sender_stand_request.post_new_user(data.user_body.copy())
    # Almacena el token de usuario en formato json
    auth_token_value = new_user.json()["authToken"]
    # Obtiene una copia de los encabezados
    new_user_autoken = data.headers.copy()
    # Agrega al encabezado Authorization
    new_user_autoken["Authorization"]= f"Bearer {auth_token_value}"
    # Obtiene los encabezados actualizados
    return new_user_autoken

# Función de pruebas positivas
def positive_assert(kit_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body(kit_name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_autoken())
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo name está en la respuesta y contiene un valor igual al nombre del kit
    assert kit_response.json()["name"] == kit_name

# Función de pruebas negativas
def negative_assert(kit_name):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body(kit_name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_autoken())
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba que el code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400

# Prueba 1. El número permitido de caracteres 1
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("A")

# Prueba 2. El número permitidos de caracteres 511
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. El número de caracteres es mejor al permitido 0
def test_create_kit_zero_letters_in_kit_name_get_error_response():
    negative_assert("")

# Prueba 4. El número de caracteres es mayor al permitido 512
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. El parámetro kit_name contiene caracteres especiales
def test_create_kit_has_special_symbols_in_kit_name_get_success_response():
    positive_assert("№%A&@")

# Prueba 6. El parámetro kit_name contiene espacios
def test_create_kit_has_spaces_in_kit_name_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7. El parámetro kit_name contiene números
def test_create_kit_has_numbers_in_kit_name_get_success_response():
    positive_assert("123")

# Prueba 8. Falta el parámetro name en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name") # Elimina la clave name
    negative_assert(kit_body)

# Prueba 9. El tipo de parámetro en name es numérico
def test_create_kit_number_type_in_kit_name_get_error_response():
    negative_assert(123)






