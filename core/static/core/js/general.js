$(document).ready(function () {


    // show the alert
    $(".alert").first().hide().slideDown(500).delay(4000).slideUp(500, function () {
        $(this).remove();
    });
});


$(".btn_suscribir").on("click", function (event) {

    event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
    let codigoCurso = $(this).attr("data-curso")
    Swal.fire({
        title: "Confirmar inscripción",
        text: "¿Esta seguro que desea inscribirse?",
        icon: "question",
        showCancelButton: true,
        confirmButtonColor: "#186A3B",
        cancelButtonColor: "#d33",
        confirmButtonText: "CONFIRMAR"
    }).then((result) => {
        if (result.isConfirmed) {
            //AQUI PONER LA FUNCION JS PARA SUBIR INFORMACION

            generarPeticion(codigoCurso)

        }
    });
});

function generarPeticion(curso) {
    var formData = new FormData();
    let token = $("input[name='csrfmiddlewaretoken']").val();
    console.log(token)
    // Agrega datos adicionales a FormData si es necesario
    formData.append("valor", curso);
    formData.append("csrfmiddlewaretoken", token);
    console.log("init generar peticion")
    console.log(curso)
    $.ajax({
        url: "/confirmacion_curso/", // Ejemplo de URL para pruebas
        method: "POST",
        data: formData,
        dataType: "json",
        processData: false,
        contentType: false,
        beforeSend: function () { },
        success: function (data) {
            console.log(data)
            if (data['resp'] == "inscripcion_ok") {
                Swal.fire({
                    title: "Inscrito!",
                    text: data['mensaje'],
                    icon: "success"
                }).then(() => {
                    window.location.href = '/cursos/';
                });
            } else if (data['resp'] == "inscripcion_existe") {
                Swal.fire({
                    title: "UPS. curso inscrito",
                    text: data['mensaje'],
                    icon: "info"
                }).then(() => { });
            } else {
                Swal.fire({
                    title: "error",
                    text: "ERROR AL INSCRIBIR CURSO",
                    icon: "danger"
                });
            }


        },
        complete: function () {
            // Después de que la solicitud se haya completado (ya sea éxito o error)
            console.log("Solicitud completada");
            // Puedes ocultar el indicador de carga aquí
        },
        error: function (xhr, status, error) {
            // En caso de un error en la solicitud
            console.error("Error en la solicitud:", status, error);
        }
    });

}



$(".btnContact").on("click", function (event) {

    event.preventDefault();

    Swal.fire({
        position: "center",
        icon: "success",
        title: "Correo enviado correctamente",
        showConfirmButton: false,
        timer: 1500
    });
});


$(".btnEliminarCuenta").on("click", function (event) {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
    Swal.fire({
        title: "Confirmar eliminación de cuenta",
        text: "¿Estás seguro de que deseas eliminar tu cuenta? Esta acción no se puede deshacer.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
        confirmButtonText: "Eliminar",
    }).then((result) => {
        if (result.isConfirmed) {
            eliminarCuenta();
        }
    });
});

function eliminarCuenta() {
    // Obtén el token CSRF del formulario
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();

    // Realiza la solicitud AJAX con el token CSRF
    $.ajax({
        url: "/eliminar_cuenta/",
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
        data: {
            csrfmiddlewaretoken: csrfToken,
        },
        dataType: "json",
        success: function (data) {
            // Maneja la respuesta del servidor aquí
            Swal.fire({
                title: data.title,
                text: data.message,
                icon: data.icon,
            }).then(() => {
                if (data.icon === 'success') {
                    // Redirige al usuario después de eliminar la cuenta
                    window.location.href = '/'; // Ajusta la URL según sea necesario
                }
            });
        },
        error: function (xhr, status, error) {
            // Maneja el error aquí
            Swal.fire({
                title: "Error",
                text: "Ocurrió un error al intentar eliminar la cuenta. Por favor, inténtalo de nuevo más tarde.",
                icon: "error",
            });
        },
    });
}