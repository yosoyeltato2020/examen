import requests

def llamar_servidor(url):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print("Respuesta del servidor:", respuesta.text)
        else:
            print("Error en la respuesta del servidor:", respuesta.status_code)
    except requests.exceptions.RequestException as e:
        print("Error al conectar con el servidor:", e)

if __name__ == "__main__":
    url_servidor = "http://127.0.0.1:5000/"  # Reemplaza con la dirección IP y puerto del servidor
    llamar_servidor(url_servidor)