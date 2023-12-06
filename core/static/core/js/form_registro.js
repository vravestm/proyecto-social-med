document.addEventListener("DOMContentLoaded", function () {

    let divCiudad = document.getElementById("divCiudad");
    divCiudad.style.display = "none";

    fetch("/static/core/data/provincias.json")
        .then(function (response) {
            return response.json();
        })
        .then(function (provincias) {
            let placeholder = document.getElementById("ciudad");
            let out = "<option value='' disabled selected>Selecciona una ciudad</option>";
            for (let provincia of provincias) {
                out += `<option value="${provincia.code}">${provincia.label}</option>`;
            }
            placeholder.innerHTML = out;
        })
        .catch(function (error) {
            console.log("Error al obtener las ciudades:", error);
        });

    fetch("/static/core/data/profesiones.json")
        .then(function (response) {
            return response.json();
        })
        .then(function (ocupaciones) {
            let placeholder = document.getElementById("profesiones");
            let out = "<option value='' disabled selected>Selecciona una ocupación</option>";
            for (let ocupacion of ocupaciones.ocupaciones) {
                out += `<option value="${ocupacion.code}">${ocupacion.label}</option>`;
            }
            placeholder.innerHTML = out;
        })
        .catch(function (error) {
            console.log("Error al obtener las ocupaciones:", error);
        });


});



document.getElementById("id_nacionalidad").addEventListener("change", function (e) {
    let seleccion = e.target.value;
    // alert(seleccion);
    let divCiudad = document.getElementById("divCiudad");
    if (seleccion == "española") {

        divCiudad.style.display = "block";
    } else {
        divCiudad.style.display = "none";
    }
});