document.addEventListener("DOMContentLoaded", function() {
    fetch("/static/core/data/provincias.json")
        .then(function(response) {
            return response.json();
        })
        .then(function(provincias) {
            let placeholder = document.getElementById("provincias");
            let out = "<option value=''>Selecciona una ciudad</option>"; 
            for (let provincia of provincias) {
                out += `<option value="${provincia.code}">${provincia.label}</option>`;
            }
            placeholder.innerHTML = out;
        })
        .catch(function(error) {
            console.log("Error al obtener las ciudades:", error);
        });
});

document.addEventListener("DOMContentLoaded", function() {
    fetch("/static/core/data/profesiones.json")
        .then(function(response) {
            return response.json();
        })
        .then(function(ocupaciones) {
            let placeholder = document.getElementById("profesiones");
            let out = "<option value=''>Selecciona una ocupación</option>"; 
            for (let ocupacion of ocupaciones.ocupaciones) {
                out += `<option value="${ocupacion.code}">${ocupacion.label}</option>`;
            }
            placeholder.innerHTML = out;
        })
        .catch(function(error) {
            console.log("Error al obtener las ocupaciones:", error);
        });
});