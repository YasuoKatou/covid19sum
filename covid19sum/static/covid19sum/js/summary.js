$(window).on('load', function() {
    $( "#menu_area" ).menu({
        select: function( event, ui ) {
            if ('area_code' in ui.item[0].dataset) {
                try {
                    $('input[name="area_code"]').val(ui.item[0].dataset.area_code);
                    $('#area_form').submit();
                } catch (error) {
                    alert(error);
                }
            }
        }
    });
    $( "#menu_graph" ).menu({
        select: function( event, ui ) {
            try {
                $('input[name="graph_type"]').val(ui.item[0].dataset.graph_type);
                $('#area_form').submit();
            } catch (error) {
                alert(error);
            }
    }
    });
    // フォーム（メニュー）を表示する
    $( "#area_form" ).removeClass( "form_init" );
});
