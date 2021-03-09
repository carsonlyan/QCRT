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
function showDetails(dl, cl, testtype, testmethod, result, page, perpage){
    if (page < 0){
        var page = parseInt($('#jumpPage').val())
    }
    var data = {
        'codeline': dl,
        'changelist': cl,
        'testtype': testtype,
        'testmethod': testmethod,
        'result': result,
        'page': page,
        'perpage': perpage
    }
    $.ajax({
        url: '/ajax_receive',
        data: JSON.stringify(data),
        success: function (response) {
            $('#detail_div').html(response)
        }
    })
}
