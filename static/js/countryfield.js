var countrySelected = $('#id_default_country').val();
if (!countrySelected){
    $('#id_default_country').css('color', '#aab7c4');
   
}
$('#id_default_country').change(function(){
    countrySelected = $(this).val();
    if (!countrySelected){
        $('#id_default_country').css('color', '#aab7c4');
         $('#id_default_country').css('background-color', '#669900');
    } else {
        $(this).css('color', '#000000');
    }
});