var nombre = document.getElementById("nom");
const form = document.getElementById("form1");
var msj = document.getElementById("mensajes");

form.addEventListener("submit", e =>{
    e.preventDefault();
    let mensajesMostrar = "";
    let entrar = false;

    if(nombre.value.length < 4 || nombre.value.length > 7){
        mensajesMostrar += "La longitud no es correcta<br>";
        entrar = true;
    }

    var letraInicial = nombre.value.charAt(0);
    if(!esMayuscula(letraInicial)){
        mensajesMostrar += "La primera letra es minúscula<br>";
        entrar = true;
    }

    if(entrar){
        msj.innerHTML = mensajesMostrar;
    }
    else{
        msj.innerHTML = "Formulario Enviado";
    }

});

function esMayuscula(letra){
    return letra == letra.toUpperCase();
}
