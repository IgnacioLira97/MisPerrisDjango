
function formulario(){
    var nombre=document.getElementById("txtNombre").value;
    var rut=document.getElementById("txtRut").value;
    var largo=rut.length;
    if (largo!=8) {
        
        
        return alert("Ingrese un rut válido.");
    }
    var suma=0
    ;var mult=3;
    for (var index = 0; index < 8; index++) {
        var caracter=rut.substring(index,index+1);
        suma=suma+(parseInt(caracter)*mult);
        mult--;
        if (mult==1) {}

            mult=7;
        }        
        
    }
    alert("suma:"+suma);    
    alert("Digito:"+(11-(suma % 11)));
