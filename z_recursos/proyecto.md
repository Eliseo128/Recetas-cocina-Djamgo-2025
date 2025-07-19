¡Excelente iniciativa! Aquí tienes una guía completa y detallada para desarrollar tu proyecto de recetas de cocina en Django, siguiendo todos los puntos que has solicitado.

---

### **Resumen del Proyecto**

Este documento es una guía paso a paso para crear una aplicación web de gestión de recetas de cocina utilizando el framework Django. El proyecto, llamado "Pj_recetas", permitirá a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las recetas. Cada receta podrá tener un nombre, una descripción y una imagen asociada. La interfaz de usuario se diseñará con Bootstrap para un aspecto moderno y responsivo, y no se utilizará el fichero `forms.py` de Django, manejando los formularios directamente en las vistas.

### **Tecnologías Utilizadas**

*   **Backend:** Python 3, Django 4.x
*   **Base de Datos:** SQLite (por defecto en Django)
*   **Frontend:** HTML5, Bootstrap 5
*   **Librerías Python:** Pillow (para el manejo de imágenes)

---

### **Procedimiento Detallado**

Sigue estos pasos en orden para construir tu aplicación.

#### **1. Prerrequisitos (Verificación)**

Abre una terminal o línea de comandos (CMD, PowerShell, Terminal) y ejecuta:

```bash
# Verificar la versión de Python
python --version
# o en algunos sistemas
python3 --version

# Verificar la versión de pip
pip --version
# o
pip3 --version
```
Si no están instalados, deberás descargarlos desde [python.org](https://www.python.org/).

#### **2. Entorno Virtual**

Es una buena práctica aislar las dependencias de tu proyecto.

```bash
# Crear una carpeta para el proyecto y navegar a ella
mkdir ProyectoRecetas
cd ProyectoRecetas

# Crear el entorno virtual (ej. llamado "venv")
python -m venv venv

# Activar el entorno virtual
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```
Verás `(venv)` al principio de la línea de tu terminal, indicando que el entorno está activo.

#### **3. Seleccionar el Intérprete de Python (en VS Code)**

Si usas Visual Studio Code, presiona `Ctrl+Shift+P` y busca "Python: Select Interpreter". Elige el que tenga la ruta a tu entorno virtual (`./venv/Scripts/python.exe` en Windows o `./venv/bin/python` en macOS/Linux).

#### **4. Instalación de Dependencias**

Con el entorno virtual activado, instala Django y Pillow.

```bash
pip install django pillow
```

#### **5. Creación del Proyecto y la Aplicación**

```bash
# Crear el proyecto Django "Pj_recetas"
# El punto "." al final evita crear un subdirectorio extra
django-admin startproject Pj_recetas .

# Ejecutar el servidor por primera vez para verificar
python manage.py runserver
```
Visita `http://127.0.0.1:8000/` en tu navegador para ver la página de bienvenida de Django. Detén el servidor con `Ctrl+C`.

```bash
# Crear la aplicación "app_receta"
python manage.py startapp app_receta
```

#### **6. Estructura de Archivos y Carpetas**

Tu estructura debería verse así:

```
ProyectoRecetas/
├── Pj_recetas/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_receta/
│   ├── migrations/
│   ├── templates/  <-- Créala manualmente
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── venv/
└── manage.py
```

#### **7. Configuración del Proyecto (`settings.py` y `urls.py`)**

**A. En `Pj_recetas/settings.py`:**

1.  Agrega `app_receta` a `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app_receta', # <-- AGREGAR AQUÍ
    ]
    ```

2.  Configura los archivos multimedia. Agrega esto al final del archivo:

    ```python
    # Configuración para archivos multimedia (imágenes)
    import os
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

**B. En `Pj_recetas/urls.py`:**

Importa `include` y las configuraciones estáticas. Configura las rutas para que el proyecto reconozca las URLs de `app_receta` y sirva los archivos multimedia en modo de desarrollo.

```python
from django.contrib import admin
from django.urls import path, include # Importar include
from django.conf import settings # Importar settings
from django.conf.urls.static import static # Importar static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirige cualquier petición a la app de recetas
    path('', include('app_receta.urls')),
]

# Añadir configuración para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### **8. Modelo de Datos (`app_receta/models.py`)**

Este es el modelo que proporcionaste. Define la estructura de la tabla `Receta` en la base de datos.

```python
# app_receta/models.py

from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    # Relación con el usuario que crea la receta (opcional)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_receta = models.CharField(max_length=100)
    descripcion_receta = models.TextField()
    # Campo para la imagen, se guardará en la carpeta 'media/recetas'
    imagen_receta = models.ImageField(upload_to="recetas", null=True, blank=True)
    # Contador simple de vistas (no implementado en las vistas, pero disponible)
    ver_contar_receta = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre_receta
```

#### **9. Migraciones y Superusuario**

Estos comandos sincronizan tu modelo con la base de datos.

```bash
# Preparar los archivos de migración
python manage.py makemigrations

# Aplicar las migraciones a la base de datos
python manage.py migrate

# Crear un superusuario para acceder al panel de administración
python manage.py createsuperuser
```
Sigue las instrucciones para crear tu usuario administrador.

#### **10. Registrar Modelo en `admin.py`**

Para poder ver y gestionar tus recetas desde `http://127.0.0.1:8000/admin/`:

```python
# app_receta/admin.py

from django.contrib import admin
from .models import Receta

# Register your models here.
admin.site.register(Receta)
```

#### **11. Definición de las URLs de la App (`app_receta/urls.py`)**

Este archivo enruta las peticiones dentro de tu aplicación a las funciones correspondientes en `views.py`. Usa el código que proporcionaste.

```python
# app_receta/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL principal que muestra el formulario y la lista de recetas
    path('', views.recetas, name='recetas'),
    # URL para borrar una receta específica por su ID
    path('borrar_receta/<int:id>', views.borrar_receta, name='borrar_receta'),
    # URL para la página de actualización de una receta
    path('actualizar_receta/<int:id>', views.actualizar_receta, name='actualizar_receta'),
]
```

#### **12. Creación de las Vistas (`app_receta/views.py`)**

Aquí está la lógica principal de la aplicación. Maneja las peticiones HTTP, interactúa con la base de datos y renderiza las plantillas HTML.

```python
# app_receta/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from django.contrib import messages

# Vista principal: Muestra, busca y crea recetas
def recetas(request):
    # Lógica para la búsqueda
    busqueda = request.GET.get("buscar")
    lista_recetas = Receta.objects.all().order_by('-id') # Ordena por más reciente

    if busqueda:
        lista_recetas = Receta.objects.filter(
            nombre_receta__icontains=busqueda
        ).distinct()

    # Lógica para crear una nueva receta (manejo del POST)
    if request.method == 'POST':
        nombre = request.POST.get("nombre_receta")
        descripcion = request.POST.get("descripcion_receta")
        imagen = request.FILES.get("imagen_receta")

        # Validación simple
        if not nombre or not descripcion:
            messages.error(request, "El nombre y la descripción son obligatorios.")
        else:
            # Crear y guardar la nueva receta
            Receta.objects.create(
                nombre_receta=nombre,
                descripcion_receta=descripcion,
                imagen_receta=imagen
            )
            messages.success(request, "Receta guardada exitosamente.")
            return redirect('recetas')

    return render(request, "receta.html", {"recetas": lista_recetas})


# Vista para actualizar una receta
def actualizar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)

    if request.method == 'POST':
        nombre = request.POST.get("nombre_receta")
        descripcion = request.POST.get("descripcion_receta")
        imagen = request.FILES.get("imagen_receta")

        receta.nombre_receta = nombre
        receta.descripcion_receta = descripcion
        
        # Solo actualiza la imagen si se sube una nueva
        if imagen:
            receta.imagen_receta = imagen
        
        receta.save()
        messages.success(request, "Receta actualizada correctamente.")
        return redirect('recetas')

    return render(request, "actualizar_receta.html", {"receta": receta})


# Vista para borrar una receta
def borrar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    messages.info(request, "La receta ha sido eliminada.")
    return redirect('recetas')
```

#### **13. Creación de las Plantillas (HTML)**

Dentro de la carpeta `app_receta/templates/` crea los siguientes archivos:

**A. `base.html`**
Esta es la plantilla base que contendrá la estructura común (navbar, Bootstrap, etc.).

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestor de Recetas</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Iconos de Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        body { background-color: #f8f9fa; }
        .card { box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .table-hover tbody tr:hover { background-color: #e9ecef; }
        .img-thumbnail-custom {
            width: 80px;
            height: 80px;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'recetas' %}">
                <i class="bi bi-journal-album"></i> Mis Recetas
            </a>
        </div>
    </nav>

    <main class="container mt-4">
        {% block content %}
        <!-- El contenido de las otras plantillas irá aquí -->
        {% endblock %}
    </main>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**B. `receta.html`**
La página principal para agregar, buscar y listar las recetas.

```html
{% extends 'base.html' %}

{% block content %}
<div class="row">
    <!-- Columna del Formulario para Agregar y Buscar -->
    <div class="col-md-4">
        <div class="card mb-4">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0"><i class="bi bi-plus-circle-fill"></i> Agregar Nueva Receta</h4>
            </div>
            <div class="card-body">
                <!-- El atributo enctype es CRUCIAL para subir archivos -->
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="nombre_receta" class="form-label">Nombre de la Receta</label>
                        <input type="text" class="form-control" name="nombre_receta" required>
                    </div>
                    <div class="mb-3">
                        <label for="descripcion_receta" class="form-label">Descripción / Pasos</label>
                        <textarea class="form-control" name="descripcion_receta" rows="4" required></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="imagen_receta" class="form-label">Imagen de la Receta</label>
                        <input type="file" class="form-control" name="imagen_receta" accept="image/*">
                    </div>
                    <button type="submit" class="btn btn-primary w-100"><i class="bi bi-check-lg"></i> Guardar Receta</button>
                </form>
            </div>
        </div>

        <div class="card">
            <div class="card-header">
                <h4 class="mb-0"><i class="bi bi-search"></i> Buscar Receta</h4>
            </div>
            <div class="card-body">
                <form method="get">
                    <div class="input-group">
                        <input type="text" class="form-control" name="buscar" placeholder="Buscar por nombre...">
                        <button class="btn btn-outline-secondary" type="submit"><i class="bi bi-search"></i></button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Columna de la Tabla de Recetas -->
    <div class="col-md-8">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            {% endfor %}
        {% endif %}

        <div class="card">
            <div class="card-header bg-success text-white">
                <h4 class="mb-0"><i class="bi bi-list-ul"></i> Listado de Recetas</h4>
            </div>
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-dark">
                        <tr>
                            <th scope="col">No.</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Descripción</th>
                            <th scope="col">Foto</th>
                            <th scope="col">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for receta in recetas %}
                        <tr>
                            <th scope="row">{{ forloop.counter }}</th>
                            <td>{{ receta.nombre_receta }}</td>
                            <td>{{ receta.descripcion_receta|truncatewords:15 }}</td>
                            <td>
                                {% if receta.imagen_receta %}
                                    <img src="{{ receta.imagen_receta.url }}" alt="{{ receta.nombre_receta }}" class="img-thumbnail img-thumbnail-custom">
                                {% else %}
                                    <span class="text-muted">Sin imagen</span>
                                {% endif %}
                            </td>
                            <td>
                                <a href="{% url 'actualizar_receta' receta.id %}" class="btn btn-warning btn-sm" title="Editar">
                                    <i class="bi bi-pencil-square"></i>
                                </a>
                                <a href="{% url 'borrar_receta' receta.id %}" class="btn btn-danger btn-sm" onclick="return confirm('¿Estás seguro de que quieres eliminar esta receta?');" title="Eliminar">
                                    <i class="bi bi-trash-fill"></i>
                                </a>
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="5" class="text-center text-muted">No hay recetas registradas.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

**C. `actualizar_receta.html`**
Formulario para editar una receta existente.

```html
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header bg-warning text-dark">
                <h4 class="mb-0"><i class="bi bi-pencil-fill"></i> Actualizar Receta</h4>
            </div>
            <div class="card-body">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="nombre_receta" class="form-label">Nombre de la Receta</label>
                        <input type="text" class="form-control" name="nombre_receta" value="{{ receta.nombre_receta }}" required>
                    </div>
                    <div class="mb-3">
                        <label for="descripcion_receta" class="form-label">Descripción / Pasos</label>
                        <textarea class="form-control" name="descripcion_receta" rows="5" required>{{ receta.descripcion_receta }}</textarea>
                    </div>
                    <div class="mb-3">
                        <label for="imagen_receta" class="form-label">Cambiar Imagen (opcional)</label>
                        {% if receta.imagen_receta %}
                            <p class="mb-1">Imagen Actual:</p>
                            <img src="{{ receta.imagen_receta.url }}" alt="{{ receta.nombre_receta }}" class="img-thumbnail mb-2" style="max-width: 150px;">
                        {% endif %}
                        <input type="file" class="form-control" name="imagen_receta" accept="image/*">
                    </div>
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'recetas' %}" class="btn btn-secondary me-md-2"><i class="bi bi-x-circle"></i> Cancelar</a>
                        <button type="submit" class="btn btn-warning"><i class="bi bi-save-fill"></i> Guardar Cambios</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### **14. Generar Archivo de Requerimientos**

Este archivo es útil para que otros puedan instalar las mismas dependencias que tú usaste.

```bash
pip freeze > requirements.txt
```

---

### **Explicación de Puntos Importantes del Proyecto**

1.  **Manejo de Formularios sin `forms.py`**: En las vistas (`views.py`), accedemos a los datos del formulario directamente desde el objeto `request`. `request.POST` es un diccionario que contiene los datos de los campos de texto, y `request.FILES` contiene los archivos subidos. Este enfoque es más directo pero renuncia a las validaciones automáticas y la renderización de campos que ofrece `forms.py`.
2.  **`enctype="multipart/form-data"`**: Este atributo es **esencial** en la etiqueta `<form>` de tus plantillas HTML. Le dice al navegador que el formulario enviará archivos además de texto, permitiendo que `request.FILES` funcione correctamente.
3.  **Configuración de `MEDIA_URL` y `MEDIA_ROOT`**:
    *   `MEDIA_ROOT`: Es la ruta absoluta en tu sistema de archivos donde Django guardará los archivos subidos por los usuarios (en este caso, en una carpeta `media/` en la raíz de tu proyecto).
    *   `MEDIA_URL`: Es la URL base que se usará para acceder a esos archivos desde el navegador (ej: `http://localhost:8000/media/recetas/mi-foto.jpg`).
    *   La configuración en `Pj_recetas/urls.py` es un truco para que el servidor de desarrollo de Django pueda servir estos archivos. **En producción, se debe usar un servidor web como Nginx o Apache para servirlos.**
4.  **`get_object_or_404`**: Es una función de atajo de Django muy útil. Intenta obtener un objeto de la base de datos por su clave primaria (u otro campo) y, si no lo encuentra, levanta un error HTTP 404 (Página no encontrada) automáticamente, evitando que el programa se rompa.

### **Listado de Palabras Clave**

*   **Django**: Framework de alto nivel para Python que fomenta el desarrollo rápido y el diseño limpio y pragmático.
*   **MTV (Model-Template-View)**: El patrón de arquitectura de Django. El **Modelo** define los datos, la **Vista** (View) procesa la lógica y la **Plantilla** (Template) muestra la información.
*   **ORM (Object-Relational Mapping)**: Sistema que permite interactuar con la base de datos usando objetos de Python (los Modelos) en lugar de escribir SQL directamente.
*   **CRUD**: Acrónimo de **C**reate, **R**ead, **U**pdate, **D**elete. Son las cuatro operaciones básicas de la persistencia de datos.
*   **Pillow**: Una librería bifurcada de PIL (Python Imaging Library) que es fundamental en Django para procesar y guardar imágenes (`ImageField`).
*   **Bootstrap**: Un popular framework de frontend para crear interfaces de usuario responsivas y modernas con componentes predefinidos.
*   **Entorno Virtual (venv)**: Una herramienta para crear entornos de Python aislados, evitando conflictos de dependencias entre proyectos.
*   **`request.POST`**: Un objeto similar a un diccionario en Django que contiene todos los datos enviados a través de un método HTTP POST desde un formulario.
*   `**request.FILES**`: Similar a `request.POST`, pero contiene específicamente los archivos subidos en el formulario.

### **Referencias de Consultas**

*   **Documentación oficial de Django**: [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
*   **Trabajar con formularios en Django**: [https://docs.djangoproject.com/en/stable/topics/forms/](https://docs.djangoproject.com/en/stable/topics/forms/)
*   **Manejo de archivos subidos**: [https://docs.djangoproject.com/en/stable/topics/http/file-uploads/](https://docs.djangoproject.com/en/stable/topics/http/file-uploads/)
*   **Documentación oficial de Bootstrap**: [https://getbootstrap.com/docs/5.3/](https://getbootstrap.com/docs/5.3/)

### **Licencia**

**Licencia:** MIT
**Descripción:** Proyecto de Recetas de Cocina en Django. Desarrollado por Eliseo Nava.
