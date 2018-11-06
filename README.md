# UI Tests

## Instalación

Se requiere python3 y el [módulo de virtualenv](https://docs.python.org/3/library/venv.html)

### Creación del virtualenv:
`python3 -m venv venv`

### Activación del virtualenv:
`source venv/bin/activate`

### Instalación de dependencias:
`pip install -r requirements.txt`

---
Se debe colocar el webdriver de chrome con el nombre `chromedriver` en la carpeta raíz del proyecto.

Para correr los tests:
`python3 tests.py`
