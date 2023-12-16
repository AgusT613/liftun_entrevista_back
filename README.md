# 🔷 Backend Liftun Environment Django 🔷

- [Frontend del proyecto hecho en NextJS](https://github.com/AgusT613/liftun_entrevista_front) 🏹
- [Configuración del proyecto](#🔸-instalación-del-proyecto) ⏬
- [Credenciales de base de datos](#🔸-credenciales) ⏬

## 🔸 Instalación del proyecto

- Clonar el repositorio, acceder a la carpeta, y crear un entorno virtual.
- En este ejemplo se usó git bash.
- Los comandos pueden variar dependiendo de la terminal usada. Para información más detallada visitar la [documentacion de .venv](https://docs.python.org/3/library/venv.html).

```bash
  git clone https://github.com/AgusT613/liftun_entrevista_back.git

  cd liftun_entrevista_back

  python -m venv .venv
```

- Una vez hecho, acceder al instalador de paquetes de python (pip) desde el entorno virtual creado.

```bash
  source .venv/bin/activate
```

- Ahora se pueden instalar todos los paquetes necesarios para el proyecto desde el archivo `requirements.txt` usando el entorno virtual.

```bash
  pip install -r requirements.txt
```

- Por último, acceder a la carpeta `app` y arrancar el servidor de desarrollo:

```bash
  cd app

  python manage.py runserver
```

## 🔸 Credenciales

- Creadas para testear la aplicación en el admin de Django

```json
{
  username = agust613
  password = agustin123
}
```
