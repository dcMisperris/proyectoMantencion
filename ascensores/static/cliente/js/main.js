$('#btnenviar').click( function() {
    $.ajax({
             url : "http://localhost:8000/apicliente",
             dataType: "json",
             method:'POST',
             success : function (data) {
                var name = toString.$('#i_nombre');
                data.nombre = name;
                console.log('bien');
             }

                });
             
                
                    
                

                    
                 });
           