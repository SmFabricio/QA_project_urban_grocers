import configuration
import requests
import data

# Método de ingreso usuario nuevo
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Método de ingreso kit nuevo
def post_new_client_kit(kit_body, auth_token):
    # Realiza una solicitud POST para los nuevos kits
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_token)
