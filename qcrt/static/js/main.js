$(function(){
    $('#btn_summary').click(function () {
        var dl = $('#slt_dl').find('option:selected').text();
        var cl = $('#slt_cl').find('option:selected').text();
        var data = {
                'codeline': dl,
                'changelist': cl
            }
        $.ajax({
            url: '/show_main_table',
            data: JSON.stringify(data),
            success: function (response) {
                if (response.startsWith('ERROR')){
                    alert(response)
                }
                else{
                    $('#main_div').html(response)
                    $('#detail_div').html('')
                }
            }
        })
    });
})

function selectChange(){
    var dl = $('#slt_dl').find('option:selected').text();
    var data = {
            'codeline': dl
        }
    $.ajax({
            url: '/select_change',
            data: JSON.stringify(data),
            success: function (data) {
                $('#slt_cl').empty()
                for (i=0;i<data.length;i++){
                    $("<option value='"+(i+1).toString()+"'>" + data[i] + "</option>").appendTo('#slt_cl')
                }
            }
        })
}

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
        url: '/show_detail_table',
        data: JSON.stringify(data),
        success: function (response) {
            $('#detail_div').html(response)
        }
    })
}
