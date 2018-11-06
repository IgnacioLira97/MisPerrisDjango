$(document).ready(function()
{
    $("#cboRegion").change(function()
    {
        //este codigo se ejecuta cuando e usuario
        //selecciona un item del combobox
        var regionId = $("#cboRegion").val();
       // console.log(regionId);

       if(regionId =="")
            {
                $("#cboCiudad").prop("disabled",true);
                $("#cboCiudad").val("");
                return ;
            }

       //enviamos el id a nuestro php
        $.get("region.php",{id:regionId}, function(respuesta)
        {   
            //dejamos la respuesta dentro del combobox
            //de comuna
            $("#cboCiudad").html(respuesta)
            $("#cboCiudad").prop("disabled",false);

        });

    });
});