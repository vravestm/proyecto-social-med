function toggleDesplegable(id) {
    var desplegable = document.getElementById(id);

    // Cerrar todas las capsulas antes de abrir la actual
    var capsulas = document.querySelectorAll('.contenido-desplegable');
    capsulas.forEach(function(capsula) {
      if (capsula.id !== id) {
        capsula.style.display = 'none';
      }
    });

    // Toggle para abrir/cerrar la capsula actual
    desplegable.style.display = (desplegable.style.display === 'none') ? 'block' : 'none';

    // Revertir estilos al hacer clic
    desplegable.classList.remove('capsula-clicked');
    setTimeout(function() {
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

        console.log('Comentario:', comentario);
        console.log('¿Publicar Nombre?', publicarNombre);
    }

$(document).ready(function() {
      $('.stars i').on('click', function() {
          // Obtener la calificación desde el atributo data-rating
          var rating = $(this).data('rating');

          // Remover y agregar la clase 'text-warning' según la calificación
          $(this).siblings().removeClass('text-warning').css('color','#146448');
          $(this).prevAll().addBack().addClass('text-warning');
      });
});

