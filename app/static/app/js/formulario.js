
var btnEnviar = document.getElementById("btnEnviar")

btnEnviar.addEventListener("click", function() {
    
    //traer los datos del formulario
    let nombre = document.getElementById("nombre").value
    let email  = document.getElementById("email").value
    let telefono = document.getElementById("telefono").value
    let tipoConsulta = document.getElementById("tipoconsulta").value
    let mensaje = document.getElementById("mensaje").value
    let aviso = document.getElementById("avisos").checked

    
    
    console.log(nombre)
    console.log(email)
    console.log(telefono)
    console.log(tipoConsulta)
    console.log(mensaje)
    console.log(aviso)

})
