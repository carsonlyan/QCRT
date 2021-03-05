from qcrt.model import testResult
import importlib
import time

HEADERS = ['TestCases',
           'Total',
           'Pass',
           'Rerun_Pass',
           'Skip',
           'Fail',
           'Error',
           'Inconclusive',
           'Duration'
           ]

DETAIL_HEADERS = ['TestType',
                  'CodeLine',
                  'ChangeList',
                  'TestMethod',
                  'Result'
                 ]


def bind_detail_table_data(code_line, change_list, test_type, result, test_method):
    known_data = {'CodeLine': code_line,
                  'ChangeList': change_list,
                  'TestType': test_type,
                  'Result': result}
    detail_table_datas = []
    tmp_detail_table_data = {}
    for item in testResult.query_detail(code_line, change_list, test_type, result, test_method):
        tmp_detail_table_data['testmethod'] = item[0]
        for head in DETAIL_HEADERS:
            if head in known_data.keys():
                tmp_detail_table_data.setdefault(head.lower(), known_data[head])
        detail_table_datas.append(tmp_detail_table_data)
    return detail_table_datas


TABLES = {
    'bbt': 'BBTTable',
    'lrt': 'LRTTable'
}


class BaseTable(object):
    _Test_Cases = None

    def __init__(self, code_line, change_list, test_type):
        self._code_line = code_line
        self._change_list = change_list
        self._test_type = test_type
        self._db_has_data = False
        self.__check_db_data()
        self._table_data = {}
        self.__init_table_data()

    def __check_db_data(self):
        self._db_has_data = True if testResult.query_first_data(self._change_list) else False

    def __init_table_data(self):
        if not self._db_has_data:
            return
        for test_case in self._Test_Cases:
            self._table_data.setdefault(test_case, {})
            for header in HEADERS[1:]:
                self._table_data[test_case].setdefault(header.lower(), 0)

    def bind_table_data(self):
        if not self._db_has_data:
            return {}
        for test_case in self._Test_Cases:
            total_count = 0
            duration = testResult.query_duration(self._code_line, self._change_list, self._test_type, test_case)[0][0]
            if duration is None:
                self._table_data.pop(test_case)
                continue
            for item in testResult.query_result_count(self._code_line, self._change_list, self._test_type, test_case):
                result = item[0].lower()
                count = item[1]
                total_count += count
                count = str(count)
                if count != '0':
                    count = '''<a href="javascript:;" onclick="showDetails('{}', '{}', '{}', '{}', '{}')">{}</a>'''.format(
                                                                                                    self._code_line,
                                                                                                    self._change_list,
                                                                                                    self._test_type,
                                                                                                    test_case,
                                                                                                    result,
                                                                                                    count)
                self._table_data[test_case][result] = count
            total_count = str(total_count)
            if total_count != '0':
                total_count = '''<a href="javascript:;" onclick="showDetails('{}', '{}', '{}', '{}', '{}')">{}</a>'''.format(
                                                                                                    self._code_line,
                                                                                                    self._change_list,
                                                                                                    self._test_type,
                                                                                                    test_case,
                                                                                                    result,
                                                                                                    total_count)
            self._table_data[test_case]['total'] = total_count
            self._table_data[test_case]['duration'] = duration

        return self._table_data


class BBTTable(BaseTable):
    _Test_Cases = ['Framework.AppFW',
                   'Framework.Graphics',
                   'Framework.UIFW',
                   'Plugin.Display',
                   'Plugin.FEM',
                   'Plugin.Geometry',
                   'Plugin.Measure',
                   'Plugin.MidSurface',
                   'Plugin.Modeling',
                   'Plugin.Motion',
                   'Plugin.Post',
                   'Plugin.THD',
                   'Plugin.Transform',
                   'total']


class LRTTable(BaseTable):
    _Test_Cases = [r'Framework\AppFW',
                   r'Framework\Graphics',
                   r'Framework\UIFW',
                   r'Misc\RtestVerification',
                   r'Plugins\BasePlugin',
                   r'Plugins\DisplayPlugin',
                   r'Plugins\FEMPlugin',
                   r'Plugins\GeomPlugin',
                   r'Plugins\MarcPlugin',
                   r'Plugins\MeasurePlugin',
                   r'Plugins\MidsurfPlugin',
                   r'Plugins\ModelingPlugin',
                   r'Plugins\MotionPlugin',
                   r'Plugins\PostPlugin',
                   r'Plugins\ShellPlugin',
                   r'Plugins\THDPlugin',
                   r'Plugins\TransformPlugin',
                   r'Services\FTC',
                   r'Services\MQC',
                   r'Services\MUC',
                   'total']


def create_table(code_line, change_list, test_type):
    class_name = TABLES[test_type]
    main_module = importlib.import_module('qcrt.main.table')
    return main_module.__dict__[class_name](code_line, change_list, test_type)
