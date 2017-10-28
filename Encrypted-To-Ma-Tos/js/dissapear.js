$(document).ready(function(){
    var check=false
  $("button").click(function dissapear(){
    check=!check
    if (check){
     $('encrypted').css('display', 'none');
     $('decrypted').css('display', 'inherit');}

     else {
      $('decrypted').css('display', 'none');
      $('encrypted').css('display', 'inherit');}
    });
})
//$("p").css("background-color", "yellow");
