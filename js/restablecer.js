const nombre = document.getElementById("name") // CONSTANTE  ID NAME
const email = document.getElementById("email") // CONSTANTE  ID MAIL
const form = document.getElementById("form") // CONSTANTE  ID FORM
const parrafo = document.getElementById("warnings") // CONSTANTE  ID ADVERTENCIAS

form.addEventListener("submit", e=>{ //FUNCION PARA ESCUCHAR EL EVENTO SUBMIT, FUNCION FLECHA 
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/ /* EXPRECIONES REGULARES, PARA QUE COINCIDA LOS CARACTERES DE LA CADENA @ - .COM */
    parrafo.innerHTML = ""
    if(nombre.value.length <6){ //SI  NOMBRE ES  MAYOR A 6
        warnings += ` - El nombre no es valido, debe ser mayor o igual a 6 caracteres. <br>`
        entrar = true
    }
    if(!regexEmail.test(email.value)){ //SI  CONTRASEÑA ES  MAYOR A 6
        warnings += ` - El email no es valido. <br>`
        entrar = true
    }
    if(entrar){
        parrafo.innerHTML = warnings // SI ENTRAR  ES VERDADERO ARROJA LA ADVERTENCIA
    }else{
        parrafo.innerHTML = "Enviado" // SI ENTRAR  ES FALSO ARROJA LA ADVERTENCIA
    }
})