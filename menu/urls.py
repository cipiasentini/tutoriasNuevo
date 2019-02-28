from django.urls import path
from . import views

app_name = 'menu'

# el name es el nombre al cual debemos referenciar desde los templates o el codigo html.
urlpatterns = [
    path('', views.verNovedades, name = 'index'),
    path('alumno/nuevo', views.agregarAlumno, name = 'alta-alumno'),
    path('alumno/editar/<int:dni>/', views.editarAlumno, name='editar-alumno'),
    path('alumno/buscar', views.buscarAlumno, name = 'buscar-alumno'),
    # path('buscar/alumno/<int:id>', views.buscarAlumnoId, name = 'buscar-alumno-id'),
    path('tutor/nuevo', views.agregarTutor, name = 'alta-tutor'),
    path('tutor/nuevo/alta-personalizada', views.agregarTutorPersonalizado, name = 'alta-tutor-personalizada'),
    path('tutor/buscar', views.buscarTutor, name = 'buscar-tutor'),
    path('tutor/editar/<int:dni>/', views.editarTutor, name='editar-tutor'),
    path('tutor/editar/baja/<int:dni>/', views.bajaTutor, name='baja-tutor'),
    path('tutor/editar/alta/<int:dni>/', views.altaTutor, name='alta-tutor'),
    path('intervencion/nueva', views.agregarIntervencion, name = 'alta-intervencion'),
    path('intervencion/nueva/tipo', views.agregarIntervencionTipo, name = 'alta-tipo-intervencion'),
    path('intervencion/editar/<int:id>/', views.editarIntervencion, name='editar-intervencion'),
    path('intervenciones', views.listarIntervenciones, name = 'intervenciones'),
    path('intervenciones/cerrar/<int:id>/', views.cerrarIntervencion, name = 'cerrar-intervencion'),
    path('intervenciones/abrir/<int:id>/', views.abrirIntervencion, name = 'abrir-intervencion'),
    path('intervenciones/eliminar/<int:id>/', views.eliminarIntervencion, name = 'eliminar-intervencion'),
    path('buscar/alumno/cerrar/<int:id>/', views.cerrarIntervencionB, name = 'cerrar-intervencion-b'),
    path('buscar/alumno/abrir/<int:id>/', views.abrirIntervencionB, name = 'abrir-intervencion-b'),
    path('novedades/panel', views.panelNovedades, name = 'panel-novedades'),
    path('novedades/panel/cerrar/<int:id>/', views.cerrarNovedad, name = 'cerrar-novedad'),
    path('novedades/panel/abrir/<int:id>/', views.abrirNovedad, name = 'abrir-novedad'),
    path('novedades/panel/eliminar/<int:id>/', views.eliminarNovedad, name = 'eliminar-novedad'),
    path('novedad/nueva', views.agregarNovedad, name = 'alta-novedad'),
    path('novedad/editar/<int:id>/', views.editarNovedad, name = 'editar-novedad'),
    path('update_session/<int:collapse>/', views.update_session, name = 'update-session'),
    path('estadisticas', views.estadisticas, name = 'estadisticas'),
    path('password', views.change_password, name='change_password'),
    path('tarea/nueva', views.agregarTarea, name='alta-tarea'),
    path('agenda/<int:year>/<int:month>/<int:day>/', views.bcal, name='agenda-tareas'),
    path('tarea/<int:id>/', views.mostrarTareaId, name='tarea'),
    path('tarea/editar/<int:id>/', views.editarTarea, name='editar-tarea'),
    path('tarea/eliminar/<int:id>/', views.eliminarTarea, name='eliminar-tarea'),
    path('grupo/nuevo', views.agregarGrupo, name = 'alta-grupo'),
    path('grupos', views.listarGrupos, name = 'listar-grupos'),
    path('grupo/editar/<int:id>/', views.editarGrupo, name='editar-grupo'),
    path('grupo/eliminar/<int:id>/', views.eliminarGrupo, name = 'eliminar-grupo'),
    path('informes/ranking-consultas/', views.rankingConsultas, name = 'ranking-consultas'),
    path('informes/estado-escuelas/', views.estadoEscuelas, name = 'estado-escuelas'),
    path('informes/categorizacion-alumnos/', views.categorizacionAlumnos, name = 'categorizacion-alumnos'),
    path('intervencion/tipo/eliminar/<int:id>/', views.eliminarTipoIntervencion, name = 'eliminar-tipo-intervencion'),
]
