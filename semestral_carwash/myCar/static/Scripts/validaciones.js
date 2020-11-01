function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("verifique el largo del rut");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();

    if (dv != dv_usuario) {
        alert("rut incorrecto");
        return false;
    } else {
        alert("Rut Correcto");
        return true;
    }
}

function validarNombre() {
    var nom = document.getElementById("txtNombre").value;
    if (nom.length >= 3 && nom.length <= 80) {
        return true;
    } else {
        alert("largo del nombre debe estar entre 3 y 80");
        return false;
    }
}

function validarApellido() {
    var nom = document.getElementById("txtApellido").value;
    if (nom.length >= 3 && nom.length <= 80) {
        return true;
    } else {
        alert("largo del nombre debe estar entre 3 y 80");
        return false;
    }
}
function validarFecha() {
    var nom = document.getElementById('txtEmail');
        
    emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
    //Se muestra un texto a modo de ejemplo, luego va a ser un icono
    if (emailRegex.test(campo.value)) {
      valido.innerText = "válido";
    } else {
      valido.innerText = "incorrecto";
    }
}

function validaFecha() {
    var fechaFormulario = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    //////////////////////////////////////////////////
    var anno = fechaFormulario.slice(0, 4);
    var mes = fechaFormulario.slice(5, 7);
    var dia = fechaFormulario.slice(8, 10);
    //////////////////////////////////////////////////
    var fechaMia = new Date(anno, (mes - 1), dia); //0-+
    //////////////////////////////////////////////////
    if (fechaMia > fechaSistema) {
        alert("fecha incorrecta");
        return false;
    } else {
        alert("fecha de nacimiento correcta");
        return true;
    }

}

function validarNombreusuario() {
    var nom = document.getElementById("txtNombreusuario").value;
    if (nom.length >= 8 ) {
        return true;
    } else {
        alert("largo del nombre de usuario debe ser mayor a 8");
        return false;
    }
}

function validarPass() {
    var nom = document.getElementById("txtNombre").value;
    if (nom.length >= 8) {
        return true;
    } else {
        alert("largo de la contraseña debe ser mayor a 8");
        return false;
    }
}


function validarFormulario() {
    var resp;
    resp = validarRut();
    if (resp == false) {
        return false;
    }
    resp = validarNombre();
    if (resp == false) {
        return false;
    }
    resp = validaFecha();
    if (resp == false) {
        return false;
    }
}

function validarProducto() {
    var nom = document.getElementById("txtProducto").value;
    if (nom.length >= 3 && nom.length <= 120) {
        return true;
    } else {
        alert("largo del nombre debe estar entre 3 y 120");
        return false;
    }
}

function validarPrecio() {
    var num = document.getElementById("txtPrecio").value;
    if (num.length >1) {
        return true;
    } else {
        alert("Precio debe ser mayor a 1 Peso");
        return false;
    }
}