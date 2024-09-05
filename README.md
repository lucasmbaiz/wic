# PROYECTO: WICA. (Wealth Invest Capital) 

El proyecto nace a partir de mi actividad como asesor financiero (Idóneo CNV - Comisión Nacional de Valores) y consiste en una startup financiera (QUE SE ENCUENTRA EN PROCESO DE REGISTRO DE MARCA) y que pretende ayudar a las personas a lograr su desarrollo financiero y así cumplir sus metas a través del ahorro, la planificación y la inversión. La idea central es que cada ahorrista y/o inversor pueda gestionar sus ahorros de una manera simple, a través de instrumentos financieros de las mejores empresas que cotizan a traves del mercado local e internacional.

# AUTOR

Lucas M. Baiz - Financial Advisor / CEO y Founder en wica. / Team Leader Customer Service en GRSA (Concesionario Oficial Toyota - Toyota Argentina SA). Estudiante de la comisión 57820 de CODERHOUSE

# SUPER USUARIO
lbaiz
Ls430250

# TECNOLOGÍA APLICADA

LENGUAJE: PYTHON (Principal) / HTML / CSS 
FRAMEWORK: DJANGO
TEMPLATES: BOOTSTRAP

# ESTRUCTURA DEL SITIO

1. INICIO: Interface de interacción principal, con botones NAVBAR, link de accesos, comentarios de clientes y FOOTER con redirección a Inicio, y links externos a una API de Whatsapp e Instagram
2. EMPRESA: ¿Quienes Somos? Detalle de la empresa y equipo de trabajo, existe
3. SERVICIOS: Nombra las tres areas principales y detalla a través de un link el procedimiento, además un boton lleva a suscripciones. Además un botón de linkeo a una API de whatsapp
4. SUSCRIPCIONES: Monetiza los servicios en tres niveles, además existe un boton que linkea al listado de servicios con FormApi y desde allí retorna a suscripciones, donde tiene un link que lleva a Mercado Pago. Si o Si tenés que estar logueado para visualizar este contenido y poder contratar.
5. CONTACTO: Un formulario de Django que registra la información de las consultas, registrando nombre, apellido, mail, telefono y consulta.
6. MI CUENTA: Donde podés registrarte e iniciar sesión. Cambia cuando estas logueado, permitiendo observar "Cerrar Sesión" y "Editar"

PATH

# Páginas estáticas

    path('Inicio/', views.inicio, name="Inicio"),
    path('Servicios/', views.servicios, name="Servicios"),
    path('Empresa/', views.empresa, name="Empresa"),
    path('Suscripciones/', views.suscripciones, name="Suscripciones"),
    path('Contacto/', views.contacto, name="Contacto"),
    path('Activos/', views.activos, name="Activos"),
    path('Clientes/', views.clientes, name="Clientes"),
    path('Login/', views.login, name="Login"),

# Formularios

    path('formulario/', views.formulario, name='formulario'),
    path('form_con_api/', views.form_con_api, name='FormConApi'),

# Busquedas 

    path('buscar/', views.buscar_form_con_api, name='buscar_form_con_api'),
    path('buscar_form_con_api/', views.buscar_form_con_api, name='buscar_form_con_api'),

# Registro / Login-out / Edición Usuario-Contraseña

    path('login/', views.login_request, name='login')
    path('register/', views.register, name='Register')
    path('logout/', LogoutView.as_view(template_name="app/Inicio.html"), name="Logout")
    path('editar_usuario/', views.editar_usuario, name="EditarUsuario")
    path('cambiar_pass/', views.CambiarPassView.as_view(), name="CambiarPass")

# CRUD

    path('', views.home),
    path('registrarServicio/', views.registrarServicio, name='registrarServicio'),
    path('edicionServicio/<id>', views.edicionServicio, name='edicionServicio'),
    path('editarServicio/', views.editarServicio, name='editarServicio'),
    path('eliminarServicio/<id>', views.eliminarServicio, name='eliminarServicio')

# AGRADECIMIENTOS

CODERHOUSE - Equipo de la Comisión 57820 del curso de PYTHON / Docente - Por el contenido y el soporte. En especial a Diego Caceres y Smailliw Arrillaga (Tutores de Coder) que siempre estuvieron para todas las dudas, me han dado una mano muy grande.

