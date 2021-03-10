from flask import render_template, request, jsonify, redirect, url_for
from .table import DETAIL_HEADERS, HEADERS, TABLES, create_table, bind_detail_table_data
import math
from . import ajax


data_map = {
    'DEV_D1': ['797242', '794042'],
    'DEVELOP': ['000413-6f0efaf7', '000262-e6fab61a'],
    'default': []
}

@ajax.route('/select_change', methods=['GET','POST'])
def select_change():
    data = request.args
    data = eval(list(data.lists())[0][0])
    codeline = data.get('codeline', 'default')
    return jsonify(data_map[codeline])


@ajax.route('/show_main_table', methods=['GET','POST'])
def show_main_table():
    data = request.args
    data = eval(list(data.lists())[0][0])
    code_line = data['codeline']
    change_list = data['changelist'].split('-')[0]
    if code_line and change_list:
        table_datas = []
        for test_type in TABLES.keys():
            table_datas.append({test_type.upper(): create_table(code_line, change_list, test_type).bind_table_data()})
        return render_template('main_table.html',
                                code_line=code_line,
                                change_list=change_list,
                                headers=HEADERS,
                                table_datas=table_datas)
    else:
        return 'ERROR: code line or change list invalid.'


@ajax.route('/show_detail_table', methods=['GET','POST'])
def show_detail_table():
    data = request.args
    data = eval(list(data.lists())[0][0])
    paginates, table_datas = bind_detail_table_data(data['codeline'],
                                                    data['changelist'],
                                                    data['testtype'],
                                                    data['result'],
                                                    data['testmethod'],
                                                    data['page'],
                                                    data['perpage'])
    total_page = math.ceil(paginates.total/data['perpage'])
    data['testmethod'] = data['testmethod'].replace('\\', '\\\\')
    return render_template('detail_table.html',
                           headers=DETAIL_HEADERS,
                           table_datas=table_datas,
                           data=data,
                           paginates=paginates,
                           total_page=total_page)