$(function(){
    $('#btn_summary').click(function () {
        var dl = $('#slt_dl').find('option:selected').text();
        var cl = $('#slt_cl').find('option:selected').text();
        var data = {
                'codeline': dl,
                'changelist': cl
            }
        $.ajax({
            url: '/ajax_receive',
            data: JSON.stringify(data),
            success: function (response) {
                $('#button_div').html(response)
            }
        })
    });
})
function showDetails(dl, cl, test_type, test_method, result){
    var data = {
        'codeline': dl,
        'changelist': cl,
        'testtype': test_type,
        'testmethod': test_method,
        'result': result
    }
    $.ajax({
        url: '/ajax_receive',
        data: JSON.stringify(data),
        success: function (response) {
            $('#detail_div').html(response)
        }
    })
}
