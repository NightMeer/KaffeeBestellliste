$(document).ready(function () {
    $("button[type=submit]").click(function () {
        var gramm = '#gramm' + this.value
        var menge = '#menge' + this.value
        var id = '#kaffee' + this.value

        console.log("gramm = " + $(gramm).val())
        console.log("menge = " + $(menge).val())
        console.log("kaffeeid = " + $(id).val())

        gramm = $(gramm).val()
        menge = $(menge).val()
        id =  $(id).val()

        var data = { kaffeeid : id, gramm : gramm, menge : menge }

        console.log(window.location.pathname);

        if (window.location.pathname == "/home"){
            $.ajax({
              type: "POST",
              url: "/home",
              data: data,
              success: function(msg){
                    console.log( "Data Saved: " + msg );
              },
              error: function(XMLHttpRequest, textStatus, errorThrown) {
                 console.log("some error");
              }
            });
        }else{
            $.ajax({
              type: "POST",
              url: "/einkaufswagen",
              data: data,
              success: function(msg){
                  location.reload();
              },
              error: function(XMLHttpRequest, textStatus, errorThrown) {
                 console.log("some error");
              }
            });
        }
    });
})
