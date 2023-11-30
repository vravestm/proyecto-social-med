$(document).ready(function () {


    // show the alert
    $(".alert").first().hide().slideDown(500).delay(4000).slideUp(500, function () {
        $(this).remove();
    });
});


// $(".btn_suscribir").on("click", function () {
//     Swal.fire({
//         title: "¿Desea inscribirse a este curso?",
//         text: "",
//         icon: "warning",
//         showCancelButton: true,
//         confirmButtonColor: "#186A3B",
//         cancelButtonColor: "#d33",
//         confirmButtonText: "CONFIRMAR"
//     }).then((result) => {
//         if (result.isConfirmed) {
//             //AQUI PONER LA FUNCION JS PARA SUBIR INFORMACION
//             Swal.fire({
//                 title: "Inscrito!",
//                 text: "Te haz inscrito correctamente.",
//                 icon: "success"
//             });
//         }
//     });
// });


