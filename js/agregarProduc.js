
$('#form-agregar').submit(function (e) {
    e.preventDefault();
    var nombre = $('#nombre_pelicu').val();

    var descripcion = $('#desc_pelicu').val();

    var mensaje = '';

    let entrar = false;

    if (nombre.trim().length < 4 || nombre_pelicu.trim().length > 20) {
        mensaje +=
            'El nombre debe tener un largo minimo de 4 y maximo de 20 <br>';
        entrar = true;
    }



    if (descripcion.length < 10 || descripcion.length > 120) {
        mensaje += 'La descripcion debe ser mayor a 10 y menor a 120 letras <br>';
        entrar = true;
    }

    if (entrar) {
        $('#warnings').html(mensaje);
    } else {
        $('#warnings').html('Producto agregado correctamente');
    }
});