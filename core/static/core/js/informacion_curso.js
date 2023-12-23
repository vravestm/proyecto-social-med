function toggleDesplegable(id) {
  var desplegable = document.getElementById(id);

  // Cerrar todas las capsulas antes de abrir la actual
  var capsulas = document.querySelectorAll('.contenido-desplegable');
  capsulas.forEach(function (capsula) {
    if (capsula.id !== id) {
      capsula.style.display = 'none';
    }
  });

  // Toggle para abrir/cerrar la capsula actual
  desplegable.style.display = (desplegable.style.display === 'none') ? 'block' : 'none';

  // Revertir estilos al hacer clic
  desplegable.classList.remove('capsula-clicked');
  setTimeout(function () {
    desplegable.classList.add('capsula-clicked');
  }, 10);
}

// Contador de caracteres
var textarea = document.getElementById('comentario');
var contador = document.getElementById('contadorCaracteres');

textarea.addEventListener('input', function () {
    var conteo = textarea.value.length;
    contador.innerText = conteo + '/150';
});

function publicarComentario() {
  var comentario = textarea.value;
  var publicarNombre = document.getElementById('publicarNombre').checked;
  var calificacion = $('calificacion').val();

  var calificacionContainer = document.getElementById('publicarNombre').checked;
  calificacionContainer.innerHTML = 'Calificación:' + calificacion + 'estrellas';

  console.log('Comentario:', comentario);
  console.log('¿Publicar Nombre?', publicarNombre);
  console.log('Calificación:', calificacion);
}

$(document).ready(function () {
  $('.stars i').on('click', function () {
    // Obtener la calificación desde el atributo data-rating
    var rating = $(this).data('rating');

    // Remover y agregar la clase 'text-warning' según la calificación
    $(this).siblings().removeClass('text-warning').css('color', '#146448');
    $(this).prevAll().addBack().addClass('text-warning');
  });
});

$(document).ready(function () {
  $('star').on('click', function () {
    var value = $(this).data('value');
    $('#calificacion').val(value);
    $('star').removeClass('text-warning').addClass('text-muted');
    $(this).prevAll.addBack().removeClass('text-muted').addClass('text-warning');
  });

  var initialRacing = $('calificacion').val();
  $('.star:lt(' + initialRacing + ')').removeClass('text-muted').addClass('text-warning');
});
