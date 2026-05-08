![Typing SVG](https://readme-typing-svg.demolab.com/?Code&weight=500&size=30&duration=3000&pause=1000&color=00FF00&center=true&vCenter=true&width=700&lines=OWASP+SECURITY+LAB+;LABORATORIO+PRACTICO+DE+CIBERSEGURIDAD;)

![Typing SVG](https://readme-typing-svg.demolab.com/?Code&weight=500&size=12&duration=3000&pause=1000&color=00FF00&center=true&vCenter=true&width=700&lines=SQL+INJECTION+;XSS+|+Flask+|+SQLite+|+Docker;)

# ◼ Descripción

Laboratorio práctico de ciberseguridad orientado a demostrar vulnerabilidades incluidas en el OWASP Top 10 y su mitigación mediante buenas prácticas de desarrollo seguro.

El proyecto incluye versiones:

- ❌ Vulnerables
- ✅ Seguras

para comparar cómo se explotan y cómo se corrigen diferentes vulnerabilidades web.

---

# ⚠ Vulnerabilidades implementadas ⚠ 

## 🔴 SQL Injection (SQLi)

Demostración de bypass de autenticación mediante concatenación insegura de consultas SQL.

### Payload utilizado

```text
username: admin' --
password: x
```

### Resultado vulnerable
<img width="700" src="screenshots/login-page3.PNG"/>

### ✔ Mitigación aplicada

Uso de consultas parametrizadas (prepared statements):

```
cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
)
```

## 🔴 Cross-Site Scripting (XSS)

Demostración de ejecución de JavaScript mediante renderizado inseguro de comentarios.

```
<script>alert('XSS')</script>
```

### Resultado vulnerable

<img width="700" src="screenshots/sql-injection3.PNG"/>

### ✔ Mitigación aplicada

Eliminación del renderizado inseguro mediante |safe en Jinja2:

```
{{ comment }}
```

---

## ◼ Características

- Aplicación web desarrollada con Flask
- Base de datos SQLite
- Interfaz visual de login
- Sistema de comentarios vulnerable a XSS
- Entorno Dockerizado
- Modos seleccionables:
  - 🔴 vulnerable
  - 🟢 secure
- Demostración práctica de vulnerabilidades OWASP
- Mitigación segura aplicada

---

## ◼ Ejecución del proyecto

### Modo vulnerable

```bash
APP_MODE=vulnerable docker compose up --build
```

### Modo seguro

```bash
APP_MODE=secure docker compose up --build
```

## ◼ Endpoint disponible

### Login

```bash
POST /login
```

 Parámetros:

- username
- password

### Comentarios (XSS)

```bash
- GET /comments
- POST /comments
```

## ◼ Tecnologías utilizadas

- Python
- Flask
- SQLite
- HTML/CSS
- Docker
- Docker Compose
- Git

## ◼ Objetivo del proyecto

Proyecto orientado al aprendizaje práctico de:

- OWASP Top 10
- Desarrollo seguro
- Vulnerabilidades web
- Mitigación de ataques comunes
- Docker y entornos reproducibles
- Seguridad en aplicaciones web

## ◼ Capturas

### Página de login
<img width="700" src="screenshots/login-page1.PNG"/>

### SQL Injection exitosa

<img width="700" src="screenshots/login-page2.PNG"/>

### SQL Injection mitigada

<img width="700" src="screenshots/login-page3.PNG"/>

### Página de Comentarios

<img width="700" src="screenshots/sql-injection1.PNG"/>

### XSS vulnerable

<img width="700" src="screenshots/sql-injection2.PNG"/>
<img width="700" src="screenshots/sql-injection3.PNG"/>

### XSS mitigado
<img width="700" src="screenshots/sql-injection4.PNG"/>

## ◼ Autor

Desarrollado por Juan Jesús como proyecto práctico de aprendizaje en ciberseguridad ofensiva y desarrollo seguro.



