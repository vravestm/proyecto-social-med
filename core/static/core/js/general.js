$(document).ready(function () {


    // show the alert
    $(".alert").first().hide().slideDown(500).delay(4000).slideUp(500, function () {
        $(this).remove();
    });
});


$(".user-button").on("click", function () {
    Swal.fire({
        title: "Desea modificar?",
        text: "este cambio sera irreversible",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "CONFIRMAR"
    }).then((result) => {
        if (result.isConfirmed) {
            //AQUI PONER LA FUNCION JS PARA SUBIR INFORMACION
            Swal.fire({
                title: "Deleted!",
                text: "Your file has been deleted.",
                icon: "success"
            });
        }
    });
});


