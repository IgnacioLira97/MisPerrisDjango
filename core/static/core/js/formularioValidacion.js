$(document).ready(function()
{
    $("#formularioPostulante").validate(
        {
            rules:
            {
                txtRun: 
                {
                    required:true,
                    minlength:11,
                    maxlength:12
                },
                txtNombre:
                {
                    required:true
                },
                txtCorreo:
                {
                    required:true,
                    email:true

                },
                txtNacimiento:
                {
                    required:true,
                    date:true,
                    min:1920,
                    max:2000
                    
                },
                cboRegion:
                {
                    required:true
                },
                cboCiudad:
                {
                    required:true
                }
            },
            messages:
            {
                txtNacimiento:
                {
                    required:"Campo requerido",
                    min:"El año minima es de 1920",
                    max:"No se puede ingresar un año igual o superior a 2001"
                },
                txtRun:
                {
                    required:"Campo requerido",
                    minlength:"minimo 11 caracteres",
                    maxlength:"maximo 12 caracteres"
                },
                txtCorreo: 
                {
                    required:"Campo requerido",
                    
                },
                txtNombre:
                {
                    required:"Campo requerido"
                },
                cboRegion:
                {
                    required:"Elija una opcion"
                },
                cboCiudad:
                {
                    required:"Elija una opcion"
                }
            }
        }
    );


});