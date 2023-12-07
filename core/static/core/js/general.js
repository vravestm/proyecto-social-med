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