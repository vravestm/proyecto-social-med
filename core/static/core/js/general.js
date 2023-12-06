$(document).ready(function () {


    // show the alert
    $(".alert").first().hide().slideDown(500).delay(4000).slideUp(500, function () {
        $(this).remove();
    });
});


$(".btn_suscribir").on("click", function (event) {

    event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace

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
            var url = $(this).attr("href");
            Swal.fire({
                title: "Inscrito!",
                text: "Te haz inscrito correctamente.",
                icon: "success"
            });
        }
    });
});




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