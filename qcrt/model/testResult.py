from .models import db, TTestResult, TUser, TSUBApex


def query_by_columns(**columns) -> list:
    query_result = TTestResult.query.filter_by(**columns).all()
    return query_result


def query_first_data(change_list):
    query_result = TTestResult.query.filter_by(ChangeList=change_list).first()
    return query_result


def query_result_count(code_line, change_list, test_type, test_method='') -> list:
    if test_method.lower() == 'total':
        test_method = ''
    query_result = TTestResult.query.with_entities(
            TTestResult.Result,
            db.func.count(TTestResult.Result).label('Count')
        ).join(TSUBApex
        ).filter(
            TTestResult.CodeLine==code_line,
            TTestResult.ChangeList==change_list,
            TTestResult.TestType==test_type
        ).filter(
            db.func.lower(TTestResult.TestMethod).like(
                '%{}%'.format(test_method))
        ).group_by(
            TTestResult.Result
        ).all()
    return query_result


def query_pagination_detail(code_line, change_list, test_type, result, test_method='', page=1, per_page=10):
    if test_method.lower() == 'total':
        test_method = ''
    query_result = TTestResult.query.with_entities(
            TTestResult.TestMethod,
            TTestResult.Result
        ).join(TSUBApex
        ).filter(
            TTestResult.CodeLine==code_line,
            TTestResult.ChangeList==change_list,
            TTestResult.TestType==test_type,
            db.func.lower(TTestResult.TestMethod).like(
                '%{}%'.format(test_method))
        )
    if result.lower() != 'total':
        query_result = query_result.filter(TTestResult.Result==result)
    query_result = query_result.order_by(TTestResult.ID).paginate(page,per_page,error_out=False)
    return query_result


def query_duration(code_line, change_list, test_type, test_method) -> list:
    if test_method.lower() == 'total':
        test_method = ''
    query_result = TTestResult.query.with_entities(
        db.func.sum(TTestResult.Duration)
    ).join(TSUBApex
    ).filter(
        TTestResult.CodeLine==code_line,
        TTestResult.ChangeList==change_list,
        TTestResult.TestType==test_type
    ).filter(
        db.func.lower(TTestResult.TestMethod).like(
            '%{}%'.format(test_method))
    ).all()
    return query_result
