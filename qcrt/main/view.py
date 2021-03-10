from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, request
from . import main


class Selector(FlaskForm):
    changeList = SelectField(
        label='ChangeList:',
        id='slt_cl',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control'
        },
        choices=[(1, '')],
        default=1,
        coerce=int
    )
    codeLine = SelectField(
        label='CodeLine:',
        id='slt_dl',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control'
        },
        choices=[(1, ''), (2, 'DEV_D1'), (3, 'DEVELOP')],
        default=1,

        coerce=int
    )
    summary = SubmitField(label='Summary', id='btn_summary')


@main.route('/', methods=('GET', 'POST'))
def index():
    selector = Selector(csrf_enabled=False)
    for choice in selector.codeLine.choices:
        if choice[0] == selector.codeLine.data:
            code_line = choice[1]
    for choice in selector.changeList.choices:
        if choice[0] == selector.changeList.data:
            change_list = choice[1].split('-')[0]
    return render_template('index.html', selector=selector)