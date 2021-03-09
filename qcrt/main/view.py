from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, request
from .table import HEADERS, TABLES, DETAIL_HEADERS,  create_table, bind_detail_table_data
import math
import json
from . import main


class Selector(FlaskForm):
    changeList = SelectField(
        label='ChangeList',
        id='slt_cl',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control'
        },
        choices=[(1, '000262-e6fab61a'), (2, '456'), (3, '789'), (4, '794042')],
        default=4,
        coerce=int
    )
    codeLine = SelectField(
        label='CodeLine',
        id='slt_dl',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control'
        },
        choices=[(1, 'DEVELOP'), (2, 'D2'), (3, 'D3'), (4, 'DEV_D1')],
        default=4,

        coerce=int
    )
    summary = SubmitField('Summary')


@main.route('/', methods=('GET', 'POST'))
def index():
    selector = Selector(csrf_enabled=False)
    for choice in selector.codeLine.choices:
        if choice[0] == selector.codeLine.data:
            code_line = choice[1]
    for choice in selector.changeList.choices:
        if choice[0] == selector.changeList.data:
            change_list = choice[1].split('-')[0]
    table_datas = []
    for test_type in TABLES.keys():
        table_datas.append({test_type.upper(): create_table(code_line, change_list, test_type).bind_table_data()})
    return render_template('index.html',
                           selector=selector,
                           code_line=code_line,
                           change_list=change_list,
                           headers=HEADERS,
                           table_datas=table_datas)


@main.route('/ajax_receive', methods=['GET','POST'])
def ajax_receive():
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
    return render_template('ajax_table.html',
                           headers=DETAIL_HEADERS,
                           table_datas=table_datas,
                           data=data,
                           paginates=paginates,
                           total_page=total_page)


    # headers = ['TestCases', 'Total', 'Pass', 'Rerun_Pass', 'Skip', 'Fail', 'Error', 'Inconclusive', 'Duration(h)']
    # testTypes = ['lrt']
    #
    # codeline = data['codeline']
    # changeList = data['changelist'].split('-')[0]
    # for testType in testTypes:
    #     table_data = LRTTable(changeList).bind_table_data()
    # return render_template('ajax_table.html', codeline=codeline, changelist=changeList, headers=headers, table_data=table_data)