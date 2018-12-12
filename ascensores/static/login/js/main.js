$('.btnlogin').click( function() {
    $.ajax({
             url : "http://localhost:8000/usuario",
             dataType: "json",
             success : function (data) {
                var f = false;
                data.forEach(element => {
                    if($('#correo').val() == element.correo){
                        // alert("correo encontrado");
                        f = true;
                        window.location.replace("http://localhost:8000/cliente/registro/")
                       
                    }
                    else{
                        if(f=false) {
                        alert("no encontrado");
                        }
                    }
                });
             
                
                    
                

                    }
                 });
             });