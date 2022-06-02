const nombre = document.getElementById("name") // CONSTANTE  ID NAME
const email = document.getElementById("email") // CONSTANTE  ID MAIL
const pass = document.getElementById("password") // CONSTANTE  ID PASSWORD
const form = document.getElementById("form") // CONSTANTE  ID FORM
const parrafo = document.getElementById("warnings") // CONSTANTE  ID ADVERTENCIAS

form.addEventListener("submit", e=>{ //FUNCION PARA ESCUCHAR EL EVENTO SUBMIT, FUNCION FLECHA 
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/ /* EXPRECIONES REGULARES, PARA QUE COINCIDA LOS CARACTERES DE LA CADENA @ - .COM */
    parrafo.innerHTML = ""
    if(nombre.value.length <6){ //SI  NOMBRE ES  MAYOR A 6
        warnings += ` - El nombre no es valido, debe ser mayor o igual a 6 caracteres. <br>` // CONCATENACION WARNING  Y MSJ
        entrar = true
    }
    if(!regexEmail.test(email.value)){ // VALIDAR LAS EXPRECIONES REGULARES DEL CORREO
        warnings += ` - El email no es valido. <br>` // CONCATENACION WARNING  Y MSJ
        entrar = true
    }
    if(pass.value.length < 8){ //SI  CONTRASEÑA ES  MAYOR A 8
        warnings += ` - La contraseña no es valida, debe ser mayor o igual a 8 caracteres. <br>` // CONCATENACION WARNING  Y MSJ
        entrar = true
    }

    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado"
    }
})