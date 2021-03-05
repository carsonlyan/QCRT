# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class MSpeerConflictdetectionconfigrequest(db.Model):
    __tablename__ = 'MSpeer_conflictdetectionconfigrequest'

    id = db.Column(db.Integer, primary_key=True)
    publication = db.Column(db.Unicode(128), nullable=False)
    sent_date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    timeout = db.Column(db.Integer, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    progress_phase = db.Column(db.Unicode(32), nullable=False)
    phase_timed_out = db.Column(db.BIT, nullable=False)



t_MSpeer_conflictdetectionconfigresponse = db.Table(
    'MSpeer_conflictdetectionconfigresponse',
    db.Column('request_id', db.Integer, nullable=False),
    db.Column('peer_node', db.Unicode(128), nullable=False),
    db.Column('peer_db', db.Unicode(128), nullable=False),
    db.Column('peer_version', db.Integer),
    db.Column('peer_db_version', db.Integer),
    db.Column('is_peer', db.BIT),
    db.Column('conflictdetection_enabled', db.BIT),
    db.Column('originator_id', db.Integer),
    db.Column('peer_conflict_retention', db.Integer),
    db.Column('peer_continue_onconflict', db.BIT),
    db.Column('peer_subscriptions', db.Text),
    db.Column('progress_phase', db.Unicode(32), nullable=False),
    db.Column('modified_date', db.DateTime, server_default=db.FetchedValue()),
    db.Index('uci_MSpeer_conflictdetectionconfigresponse', 'request_id', 'peer_node', 'peer_db')
)



class MSpeerLsn(db.Model):
    __tablename__ = 'MSpeer_lsns'
    __table_args__ = (
        db.Index('uci_MSpeer_lsns', 'originator', 'originator_db', 'originator_publication_id', 'originator_db_version', 'originator_lsn'),
    )

    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.DateTime, server_default=db.FetchedValue())
    originator = db.Column(db.Unicode(128), nullable=False)
    originator_db = db.Column(db.Unicode(128), nullable=False)
    originator_publication = db.Column(db.Unicode(128), nullable=False, index=True)
    originator_publication_id = db.Column(db.Integer)
    originator_db_version = db.Column(db.Integer)
    originator_lsn = db.Column(db.LargeBinary(16))
    originator_version = db.Column(db.Integer)
    originator_id = db.Column(db.Integer)



t_MSpeer_originatorid_history = db.Table(
    'MSpeer_originatorid_history',
    db.Column('originator_publication', db.Unicode(128), nullable=False),
    db.Column('originator_id', db.Integer, nullable=False),
    db.Column('originator_node', db.Unicode(128), nullable=False),
    db.Column('originator_db', db.Unicode(128), nullable=False),
    db.Column('originator_db_version', db.Integer, nullable=False),
    db.Column('originator_version', db.Integer, nullable=False),
    db.Column('inserted_date', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Index('uci_MSpeer_originatorid_history', 'originator_publication', 'originator_id', 'originator_node', 'originator_db', 'originator_db_version')
)



t_MSpeer_request = db.Table(
    'MSpeer_request',
    db.Column('id', db.Integer, nullable=False),
    db.Column('publication', db.Unicode(128), nullable=False),
    db.Column('sent_date', db.DateTime, server_default=db.FetchedValue()),
    db.Column('description', db.Unicode(4000))
)



t_MSpeer_response = db.Table(
    'MSpeer_response',
    db.Column('request_id', db.Integer),
    db.Column('peer', db.Unicode(128), nullable=False),
    db.Column('peer_db', db.Unicode(128), nullable=False),
    db.Column('received_date', db.DateTime)
)



t_MSpeer_topologyrequest = db.Table(
    'MSpeer_topologyrequest',
    db.Column('id', db.Integer, nullable=False),
    db.Column('publication', db.Unicode(128), nullable=False),
    db.Column('sent_date', db.DateTime, server_default=db.FetchedValue())
)



t_MSpeer_topologyresponse = db.Table(
    'MSpeer_topologyresponse',
    db.Column('request_id', db.Integer),
    db.Column('peer', db.Unicode(128), nullable=False),
    db.Column('peer_version', db.Integer),
    db.Column('peer_db', db.Unicode(128), nullable=False),
    db.Column('originator_id', db.Integer),
    db.Column('peer_conflict_retention', db.Integer),
    db.Column('received_date', db.DateTime),
    db.Column('connection_info', db.Text)
)



t_MSpub_identity_range = db.Table(
    'MSpub_identity_range',
    db.Column('objid', db.Integer, nullable=False, unique=True),
    db.Column('range', db.BigInteger, nullable=False),
    db.Column('pub_range', db.BigInteger, nullable=False),
    db.Column('current_pub_range', db.BigInteger, nullable=False),
    db.Column('threshold', db.Integer, nullable=False),
    db.Column('last_seed', db.BigInteger)
)



t_T_BODCount = db.Table(
    'T_BODCount',
    db.Column('TestType', db.Unicode(50)),
    db.Column('BODCount', db.Integer, nullable=False)
)



t_T_Bid_Hash_Map = db.Table(
    'T_Bid_Hash_Map',
    db.Column('Branch', db.Unicode(50), nullable=False),
    db.Column('BuildID', db.Unicode(20), nullable=False),
    db.Column('Hash', db.Unicode(50), nullable=False)
)



t_T_Codeline_Changelist = db.Table(
    'T_Codeline_Changelist',
    db.Column('App', db.Unicode(50), nullable=False),
    db.Column('CodeLine', db.Unicode(50), nullable=False),
    db.Column('ChangeList', db.Unicode(20), nullable=False),
    db.Index('AI_App_Codeline', 'App', 'CodeLine', 'ChangeList')
)



class TFullUpload(db.Model):
    __tablename__ = 'T_FullUpload'
    __table_args__ = (
        db.Index('AI_ChangeList', 'ChangeList', 'TestMethod'),
    )

    ID = db.Column(db.BigInteger, primary_key=True)
    CodeLine = db.Column(db.Unicode(50))
    ChangeList = db.Column(db.Unicode(50))
    TestType = db.Column(db.Unicode(50), index=True)
    TestMethod = db.Column(db.Unicode(2000))
    Result = db.Column(db.Unicode(50))
    Duration = db.Column(db.SmallInteger)
    FailMessage = db.Column(db.Unicode)
    LogMessage = db.Column(db.Unicode)
    ApexLogMessage = db.Column(db.Unicode)
    ExecutedTime = db.Column(db.Unicode(50))
    VideoPath = db.Column(db.Unicode(150))
    FilePath = db.Column(db.Unicode(500))
    Sequence = db.Column(db.Integer)
    UploadID = db.Column(db.Unicode(200))
    Machine = db.Column(db.Unicode(200))



t_T_LCTTriggeredBlD = db.Table(
    'T_LCTTriggeredBlD',
    db.Column('id', db.Integer, nullable=False),
    db.Column('Codeline', db.Unicode(50)),
    db.Column('Changelist', db.Unicode(20)),
    db.Column('Hash', db.Unicode(60)),
    db.Column('Domains', db.Unicode)
)



t_T_MachineOS = db.Table(
    'T_MachineOS',
    db.Column('Machine', db.Unicode(50)),
    db.Column('OS', db.Unicode(50))
)



t_T_NewlyAdded = db.Table(
    'T_NewlyAdded',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('TestMethod', db.Unicode(500)),
    db.Column('NewlyAddedCL', db.Unicode(20)),
    db.Column('CodeLine', db.Unicode(20)),
    db.Index('NAI_CodeLine', 'CodeLine', 'TestMethod', 'NewlyAddedCL')
)



t_T_OSTestMethodMap = db.Table(
    'T_OSTestMethodMap',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('TestMethodLin', db.Unicode(2000)),
    db.Column('TestMethodWin', db.Unicode(2000))
)



class TOptionFieldSetting(db.Model):
    __tablename__ = 'T_OptionFieldSetting'

    ID = db.Column(db.BigInteger, primary_key=True)
    Title = db.Column(db.Unicode(20), nullable=False)
    OptionName = db.Column(db.Unicode(20), nullable=False)
    Description = db.Column(db.Unicode(100))



class TPerformance(db.Model):
    __tablename__ = 'T_Performance'

    ID = db.Column(db.BigInteger, primary_key=True)
    CodeLine = db.Column(db.Unicode(50), nullable=False)
    ChangeList = db.Column(db.Unicode(20), nullable=False, index=True)
    Test = db.Column(db.Unicode(200))
    Model = db.Column(db.Unicode(100))
    Measurement = db.Column(db.Unicode(100))
    Duration = db.Column(db.Float(53), nullable=False)
    State = db.Column(db.Unicode(5))
    Grade = db.Column(db.Unicode(5))
    Trend = db.Column(db.Unicode(5))
    Ratio = db.Column(db.Float(53))
    Machine = db.Column(db.Unicode(50))
    Chart = db.Column(db.Unicode(500))
    Bug = db.Column(db.Unicode(50))
    Labels = db.Column(db.Unicode(200))
    Average = db.Column(db.Float(53))
    SD = db.Column(db.Float(53))
    SDRatio = db.Column(db.Float(53))
    LastREL = db.Column(db.Float(53))



class TPreCompute(db.Model):
    __tablename__ = 'T_PreCompute'

    ChangeList = db.Column(db.Unicode(20), primary_key=True)
    Used = db.Column(db.BIT, nullable=False, server_default=db.FetchedValue())



class TSGCondition(db.Model):
    __tablename__ = 'T_SG_Condition'

    ID = db.Column(db.BigInteger, primary_key=True)
    RunID = db.Column(db.SmallInteger)
    TestType = db.Column(db.Unicode(500))
    CodeLine = db.Column(db.Unicode(50))
    ChangeList = db.Column(db.Unicode(20))
    ShelveNumber = db.Column(db.Unicode(20))
    Keyword = db.Column(db.Unicode(800))
    Duration = db.Column(db.Unicode(400))
    Domain = db.Column(db.Unicode(200))
    Value = db.Column(db.Unicode(50))
    MatchCount = db.Column(db.Unicode(50))



class TSGDomainFunctionDEVD1(db.Model):
    __tablename__ = 'T_SG_DomainFunction_DEV_D1'

    ID = db.Column(db.Integer, primary_key=True)
    Domain = db.Column(db.Unicode(200), nullable=False)
    FunctionName = db.Column(db.Unicode(4000), nullable=False)
    SourceFile = db.Column(db.Unicode(2000), nullable=False)



t_T_SG_DomainScope_DEV_D1 = db.Table(
    'T_SG_DomainScope_DEV_D1',
    db.Column('Domain', db.Unicode(200), nullable=False),
    db.Column('StartID', db.Integer, nullable=False),
    db.Column('EndID', db.Integer, nullable=False)
)



t_T_SG_FullData_Bak_DEV_D1 = db.Table(
    'T_SG_FullData_Bak_DEV_D1',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('Domain', db.Unicode(200)),
    db.Column('TestType', db.Unicode(10)),
    db.Column('TestCase', db.Unicode(2000)),
    db.Column('SourceFile', db.Unicode(2000)),
    db.Column('FunctionName', db.Unicode(4000)),
    db.Column('Value', db.Integer),
    db.Column('Duration', db.SmallInteger),
    db.Column('FunID', db.Unicode(20)),
    db.Column('LineNumber', db.Unicode(10))
)



class TSGFullDataDEVD1(db.Model):
    __tablename__ = 'T_SG_FullData_DEV_D1'

    ID = db.Column(db.BigInteger, primary_key=True)
    CodeLine = db.Column(db.Unicode(50))
    ChangeList = db.Column(db.Unicode(20))
    Domain = db.Column(db.Unicode(200))
    TestType = db.Column(db.Unicode(10))
    TestCase = db.Column(db.Unicode(2000))
    SourceFile = db.Column(db.Unicode(2000))
    FunctionName = db.Column(db.Unicode(4000))
    Value = db.Column(db.Integer)
    Duration = db.Column(db.SmallInteger)
    FunID = db.Column(db.Unicode(20))
    LineNumber = db.Column(db.Unicode(10))



class TSGUsage(db.Model):
    __tablename__ = 'T_SG_Usage'

    Usage_Id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Sgid = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), nullable=False)
    Codeline = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), nullable=False)
    Changelist = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), nullable=False)
    Submittedby = db.Column(db.String(50, 'Chinese_PRC_CI_AS'), nullable=False)
    Duration = db.Column(db.Float(53), nullable=False)
    Pass = db.Column(db.Integer, nullable=False)
    Rerun_pass = db.Column(db.Integer, nullable=False)
    Skip = db.Column(db.Integer, nullable=False)
    Fail = db.Column(db.Integer, nullable=False)
    Error = db.Column(db.Integer, nullable=False)
    Inconclusive = db.Column(db.Integer, nullable=False)



class TSUBAdam(db.Model):
    __tablename__ = 'T_SUB_Adams'

    P_ID = db.Column(db.Integer, primary_key=True)
    F_ID = db.Column(db.ForeignKey('T_TestResult.ID'), nullable=False, index=True)

    T_TestResult = db.relationship('TTestResult', primaryjoin='TSUBAdam.F_ID == TTestResult.ID', backref='tsub_adams')



class TSUBApex(db.Model):
    __tablename__ = 'T_SUB_Apex'

    P_ID = db.Column(db.Integer, primary_key=True)
    F_ID = db.Column(db.ForeignKey('T_TestResult.ID'), nullable=False, index=True)

    T_TestResult = db.relationship('TTestResult', primaryjoin='TSUBApex.F_ID == TTestResult.ID', backref='tsub_apexes')



class TSUBApexLinux(db.Model):
    __tablename__ = 'T_SUB_ApexLinux'

    P_ID = db.Column(db.Integer, primary_key=True)
    F_ID = db.Column(db.ForeignKey('T_TestResult.ID'), nullable=False, index=True)

    T_TestResult = db.relationship('TTestResult', primaryjoin='TSUBApexLinux.F_ID == TTestResult.ID', backref='tsub_apex_linuxes')



class TSUBGende(db.Model):
    __tablename__ = 'T_SUB_Gendes'

    P_ID = db.Column(db.Integer, primary_key=True)
    F_ID = db.Column(db.ForeignKey('T_TestResult.ID'), nullable=False, index=True)

    T_TestResult = db.relationship('TTestResult', primaryjoin='TSUBGende.F_ID == TTestResult.ID', backref='tsub_gendes')



class TSUBHelloLeaf(db.Model):
    __tablename__ = 'T_SUB_HelloLeaf'

    P_ID = db.Column(db.Integer, primary_key=True)
    F_ID = db.Column(db.ForeignKey('T_TestResult.ID'), nullable=False, index=True)

    T_TestResult = db.relationship('TTestResult', primaryjoin='TSUBHelloLeaf.F_ID == TTestResult.ID', backref='tsub_hello_leaves')



class TSUBSmartGate(db.Model):
    __tablename__ = 'T_SUB_SmartGate'

    P_ID = db.Column(db.Integer, primary_key=True)
    F_ID = db.Column(db.ForeignKey('T_TestResult.ID'), nullable=False)
    ShelveNumber = db.Column(db.Unicode(20))
    RunID = db.Column(db.Unicode(20))

    T_TestResult = db.relationship('TTestResult', primaryjoin='TSUBSmartGate.F_ID == TTestResult.ID', backref='tsub_smart_gates')



class TTempResult(db.Model):
    __tablename__ = 'T_TempResult'

    ID = db.Column(db.BigInteger, primary_key=True)
    TestType = db.Column(db.Unicode(10))
    CodeLine = db.Column(db.Unicode(50))
    ChangeList = db.Column(db.Unicode(20))
    TestMethod = db.Column(db.Unicode(2000))
    TestData = db.Column(db.SmallInteger)
    Result = db.Column(db.Unicode(50))
    Duration = db.Column(db.BigInteger)
    Bug = db.Column(db.Unicode(50))
    FailMessage = db.Column(db.Unicode)
    LogMessage = db.Column(db.Unicode)
    ApexLogMessage = db.Column(db.Unicode)
    ExecutedTime = db.Column(db.Unicode(50))
    VideoPath = db.Column(db.Unicode(150))
    RerunVideoPath = db.Column(db.Unicode(150))
    FilePath = db.Column(db.Unicode(500))
    RerunFilePath = db.Column(db.Unicode(500))
    Machine = db.Column(db.Unicode(500))



t_T_TempResult2 = db.Table(
    'T_TempResult2',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('TestType', db.Unicode(10)),
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('TestMethod', db.Unicode(2000)),
    db.Column('TestData', db.SmallInteger),
    db.Column('Result', db.Unicode(50)),
    db.Column('Duration', db.BigInteger),
    db.Column('Bug', db.Unicode(50)),
    db.Column('FailMessage', db.Unicode),
    db.Column('LogMessage', db.Unicode),
    db.Column('ApexLogMessage', db.Unicode),
    db.Column('ExecutedTime', db.Unicode(50)),
    db.Column('VideoPath', db.Unicode(150)),
    db.Column('RerunVideoPath', db.Unicode(150)),
    db.Column('FilePath', db.Unicode(500)),
    db.Column('RerunFilePath', db.Unicode(500)),
    db.Column('Machine', db.Unicode(500))
)



t_T_TempSGUsage = db.Table(
    'T_TempSGUsage',
    db.Column('Date', db.Date, nullable=False),
    db.Column('Sgid', db.String(50, 'Chinese_PRC_CI_AS'), nullable=False),
    db.Column('Codeline', db.String(50, 'Chinese_PRC_CI_AS'), nullable=False),
    db.Column('Changelist', db.String(50, 'Chinese_PRC_CI_AS'), nullable=False),
    db.Column('Submittedby', db.String(50, 'Chinese_PRC_CI_AS'), nullable=False),
    db.Column('Duration', db.Float(53), nullable=False),
    db.Column('Pass', db.Integer, nullable=False),
    db.Column('Rerun_pass', db.Integer, nullable=False),
    db.Column('Skip', db.Integer, nullable=False),
    db.Column('Fail', db.Integer, nullable=False),
    db.Column('Error', db.Integer, nullable=False),
    db.Column('Inconclusive', db.Integer, nullable=False)
)



class TTestResult(db.Model):
    __tablename__ = 'T_TestResult'
    __table_args__ = (
        db.Index('AI_CodeLineChangeList', 'CodeLine', 'ChangeList'),
        db.Index('AI_ChangeList', 'ChangeList', 'TestMethod', 'TestType', 'CodeLine', 'Result'),
        db.Index('AI_Codeline_Changelist_Bug', 'CodeLine', 'ChangeList', 'Bug', 'TestMethod'),
        db.Index('AI_TestType_ChangeList', 'TestType', 'ChangeList', 'CodeLine', 'TestMethod')
    )

    ID = db.Column(db.BigInteger, primary_key=True)
    TestType = db.Column(db.Unicode(10), index=True)
    CodeLine = db.Column(db.Unicode(50), index=True)
    ChangeList = db.Column(db.Unicode(20))
    TestMethod = db.Column(db.Unicode(2000))
    TestData = db.Column(db.SmallInteger)
    Result = db.Column(db.Unicode(50), index=True)
    Duration = db.Column(db.BigInteger)
    Bug = db.Column(db.Unicode(50))
    FailMessage = db.Column(db.Unicode)
    LogMessage = db.Column(db.Unicode)
    ExecutedTime = db.Column(db.Unicode(50))
    VideoPath = db.Column(db.Unicode(150))
    RerunVideoPath = db.Column(db.Unicode(150))
    FilePath = db.Column(db.Unicode(500))
    RerunFilePath = db.Column(db.Unicode(500))
    ApexLogMessage = db.Column(db.Unicode)
    Machine = db.Column(db.Unicode(500))



class TTestResultFrail(db.Model):
    __tablename__ = 'T_TestResultFrail'

    ID = db.Column(db.Integer, primary_key=True)
    TestMethod = db.Column(db.Unicode(2000), nullable=False)
    ExecutedTime = db.Column(db.Unicode(50), nullable=False)
    TestData = db.Column(db.SmallInteger)
    CodeLine = db.Column(db.Unicode(50), nullable=False)
    ChangeList = db.Column(db.Unicode(20), nullable=False)
    TestType = db.Column(db.Unicode(20), nullable=False)



class TTestResultValue(db.Model):
    __tablename__ = 'T_TestResultValue'

    ID = db.Column(db.Integer, primary_key=True)
    TestMethod = db.Column(db.Unicode(2000), nullable=False)
    ExecutedTime = db.Column(db.Unicode(50), nullable=False)
    TestData = db.Column(db.SmallInteger)
    Bug = db.Column(db.Unicode(50))
    CodeLine = db.Column(db.Unicode(50), nullable=False)
    ChangeList = db.Column(db.Unicode(20), nullable=False)
    TestType = db.Column(db.Unicode(20), nullable=False)



class TUser(db.Model):
    __tablename__ = 'T_User'

    ID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.Unicode(50))
    Passward = db.Column(db.Unicode(50))
    UserRole = db.Column(db.Unicode(10))



t_TempBBT = db.Table(
    'TempBBT',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('ChangeList', db.Unicode(50)),
    db.Column('TotalCount', db.Integer)
)



t_TempExport = db.Table(
    'TempExport',
    db.Column('TestMethod', db.Unicode(2000)),
    db.Column('RerunCount', db.SmallInteger)
)



t_TempOther = db.Table(
    'TempOther',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('ChangeList', db.Unicode(50)),
    db.Column('TotalCount', db.Integer)
)



t_TempTestResult = db.Table(
    'TempTestResult',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('TestType', db.Unicode(10)),
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('TestMethod', db.Unicode(2000)),
    db.Column('TestData', db.SmallInteger),
    db.Column('Result', db.Unicode(50)),
    db.Column('Duration', db.BigInteger),
    db.Column('Bug', db.Unicode(50)),
    db.Column('FailMessage', db.Unicode),
    db.Column('LogMessage', db.Unicode),
    db.Column('ExecutedTime', db.Unicode(50)),
    db.Column('VideoPath', db.Unicode(150)),
    db.Column('RerunVideoPath', db.Unicode(150)),
    db.Column('FilePath', db.Unicode(500)),
    db.Column('RerunFilePath', db.Unicode(500)),
    db.Column('ApexLogMessage', db.Unicode),
    db.Column('Machine', db.Unicode(500))
)



t_TempValueFrail = db.Table(
    'TempValueFrail',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('TestMethod', db.Unicode(2000)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('Value', db.Integer),
    db.Column('Frail', db.Integer)
)



t_Temp_789311L_TestResultCouples = db.Table(
    'Temp_789311L_TestResultCouples',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('TestType', db.Unicode(10), nullable=False),
    db.Column('CodeLine', db.Unicode(50), nullable=False),
    db.Column('ChangeList', db.Unicode(20), nullable=False),
    db.Column('TestMethod', db.Unicode(2000), nullable=False),
    db.Column('Result', db.Unicode(20), nullable=False)
)



t_View_DistinctChangeList = db.Table(
    'View_DistinctChangeList',
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('CodeLine', db.Unicode(50))
)



t_View_DistinctCodeLine = db.Table(
    'View_DistinctCodeLine',
    db.Column('CodeLine', db.Unicode(50))
)



t_View_ShortTestResult = db.Table(
    'View_ShortTestResult',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('TestMethod', db.Unicode(500)),
    db.Column('TestData', db.SmallInteger),
    db.Column('Result', db.Unicode(50)),
    db.Column('TestType', db.Unicode(10))
)



t_View_TestResultLastMonth = db.Table(
    'View_TestResultLastMonth',
    db.Column('ID', db.BigInteger, nullable=False),
    db.Column('TestType', db.Unicode(10)),
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('TestMethod', db.Unicode(500)),
    db.Column('TestData', db.SmallInteger),
    db.Column('Result', db.Unicode(50)),
    db.Column('Duration', db.SmallInteger),
    db.Column('Bug', db.Unicode(50)),
    db.Column('FailMessage', db.Unicode),
    db.Column('LogMessage', db.Unicode),
    db.Column('ExecutedTime', db.Unicode(50)),
    db.Column('VideoPath', db.Unicode(100)),
    db.Column('RerunVideoPath', db.Unicode(100)),
    db.Column('FilePath', db.Unicode(500)),
    db.Column('RerunFilePath', db.Unicode(100)),
    db.Column('ApexLogMessage', db.Unicode)
)



t_sysarticlecolumns = db.Table(
    'sysarticlecolumns',
    db.Column('artid', db.Integer, nullable=False),
    db.Column('colid', db.Integer, nullable=False),
    db.Column('is_udt', db.BIT, server_default=db.FetchedValue()),
    db.Column('is_xml', db.BIT, server_default=db.FetchedValue()),
    db.Column('is_max', db.BIT, server_default=db.FetchedValue()),
    db.Index('idx_sysarticlecolumns', 'artid', 'colid')
)



t_sysarticles = db.Table(
    'sysarticles',
    db.Column('artid', db.Integer, nullable=False),
    db.Column('creation_script', db.Unicode(255)),
    db.Column('del_cmd', db.Unicode(255)),
    db.Column('description', db.Unicode(255)),
    db.Column('dest_table', db.Unicode(128), nullable=False),
    db.Column('filter', db.Integer, nullable=False),
    db.Column('filter_clause', db.UnicodeText(1073741823)),
    db.Column('ins_cmd', db.Unicode(255)),
    db.Column('name', db.Unicode(128), nullable=False),
    db.Column('objid', db.Integer, nullable=False),
    db.Column('pubid', db.Integer, nullable=False),
    db.Column('pre_creation_cmd', db.Integer, nullable=False),
    db.Column('status', db.Integer, nullable=False),
    db.Column('sync_objid', db.Integer, nullable=False),
    db.Column('type', db.Integer, nullable=False),
    db.Column('upd_cmd', db.Unicode(255)),
    db.Column('schema_option', db.BINARY(8)),
    db.Column('dest_owner', db.Unicode(128)),
    db.Column('ins_scripting_proc', db.Integer),
    db.Column('del_scripting_proc', db.Integer),
    db.Column('upd_scripting_proc', db.Integer),
    db.Column('custom_script', db.Unicode(2048)),
    db.Column('fire_triggers_on_snapshot', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Index('c1sysarticles', 'artid', 'pubid')
)



t_sysarticleupdates = db.Table(
    'sysarticleupdates',
    db.Column('artid', db.Integer, nullable=False),
    db.Column('pubid', db.Integer, nullable=False),
    db.Column('sync_ins_proc', db.Integer, nullable=False),
    db.Column('sync_upd_proc', db.Integer, nullable=False),
    db.Column('sync_del_proc', db.Integer, nullable=False),
    db.Column('autogen', db.BIT, nullable=False),
    db.Column('sync_upd_trig', db.Integer, nullable=False),
    db.Column('conflict_tableid', db.Integer),
    db.Column('ins_conflict_proc', db.Integer),
    db.Column('identity_support', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Index('unc1sysarticleupdates', 'artid', 'pubid')
)



class Sysdiagram(db.Model):
    __tablename__ = 'sysdiagrams'
    __table_args__ = (
        db.Index('UK_principal_name', 'principal_id', 'name'),
    )

    name = db.Column(db.Unicode(128), nullable=False)
    principal_id = db.Column(db.Integer, nullable=False)
    diagram_id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Integer)
    definition = db.Column(db.LargeBinary)



t_sysextendedarticlesview = db.Table(
    'sysextendedarticlesview',
    db.Column('artid', db.Integer, nullable=False),
    db.Column('creation_script', db.Unicode(255)),
    db.Column('del_cmd', db.Unicode(255)),
    db.Column('description', db.Unicode(255)),
    db.Column('dest_table', db.Unicode(128), nullable=False),
    db.Column('filter', db.Integer),
    db.Column('filter_clause', db.UnicodeText(1073741823)),
    db.Column('ins_cmd', db.Unicode(255)),
    db.Column('name', db.Unicode(128), nullable=False),
    db.Column('objid', db.Integer, nullable=False),
    db.Column('pubid', db.Integer, nullable=False),
    db.Column('pre_creation_cmd', db.Integer, nullable=False),
    db.Column('status', db.Integer, nullable=False),
    db.Column('sync_objid', db.Integer),
    db.Column('type', db.Integer, nullable=False),
    db.Column('upd_cmd', db.Unicode(255)),
    db.Column('schema_option', db.BINARY(8)),
    db.Column('dest_owner', db.Unicode(128)),
    db.Column('ins_scripting_proc', db.Integer),
    db.Column('del_scripting_proc', db.Integer),
    db.Column('upd_scripting_proc', db.Integer),
    db.Column('custom_script', db.Unicode(2048)),
    db.Column('fire_triggers_on_snapshot', db.Integer, nullable=False)
)



t_syspublications = db.Table(
    'syspublications',
    db.Column('description', db.Unicode(255)),
    db.Column('name', db.Unicode(128), nullable=False, unique=True),
    db.Column('pubid', db.Integer, nullable=False, unique=True),
    db.Column('repl_freq', db.Integer, nullable=False),
    db.Column('status', db.Integer, nullable=False, index=True),
    db.Column('sync_method', db.Integer, nullable=False),
    db.Column('snapshot_jobid', db.BINARY(16)),
    db.Column('independent_agent', db.BIT, nullable=False),
    db.Column('immediate_sync', db.BIT, nullable=False),
    db.Column('enabled_for_internet', db.BIT, nullable=False),
    db.Column('allow_push', db.BIT, nullable=False),
    db.Column('allow_pull', db.BIT, nullable=False),
    db.Column('allow_anonymous', db.BIT, nullable=False),
    db.Column('immediate_sync_ready', db.BIT, nullable=False),
    db.Column('allow_sync_tran', db.BIT, nullable=False),
    db.Column('autogen_sync_procs', db.BIT, nullable=False),
    db.Column('retention', db.Integer),
    db.Column('allow_queued_tran', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('snapshot_in_defaultfolder', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('alt_snapshot_folder', db.Unicode(255)),
    db.Column('pre_snapshot_script', db.Unicode(255)),
    db.Column('post_snapshot_script', db.Unicode(255)),
    db.Column('compress_snapshot', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('ftp_address', db.Unicode(128)),
    db.Column('ftp_port', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ftp_subdirectory', db.Unicode(255)),
    db.Column('ftp_login', db.Unicode(128), server_default=db.FetchedValue()),
    db.Column('ftp_password', db.Unicode(524)),
    db.Column('allow_dts', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('allow_subscription_copy', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('centralized_conflicts', db.BIT),
    db.Column('conflict_retention', db.Integer),
    db.Column('conflict_policy', db.Integer),
    db.Column('queue_type', db.Integer),
    db.Column('ad_guidname', db.Unicode(128)),
    db.Column('backward_comp_level', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('allow_initialize_from_backup', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('min_autonosync_lsn', db.BINARY(10)),
    db.Column('replicate_ddl', db.Integer, server_default=db.FetchedValue()),
    db.Column('options', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('originator_id', db.Integer)
)



class Sysreplserver(db.Model):
    __tablename__ = 'sysreplservers'

    srvname = db.Column(db.Unicode(128), primary_key=True)
    srvid = db.Column(db.Integer)



t_sysschemaarticles = db.Table(
    'sysschemaarticles',
    db.Column('artid', db.Integer, nullable=False),
    db.Column('creation_script', db.Unicode(255)),
    db.Column('description', db.Unicode(255)),
    db.Column('dest_object', db.Unicode(128), nullable=False),
    db.Column('name', db.Unicode(128), nullable=False),
    db.Column('objid', db.Integer, nullable=False),
    db.Column('pubid', db.Integer, nullable=False),
    db.Column('pre_creation_cmd', db.Integer, nullable=False),
    db.Column('status', db.Integer, nullable=False),
    db.Column('type', db.Integer, nullable=False),
    db.Column('schema_option', db.BINARY(8)),
    db.Column('dest_owner', db.Unicode(128)),
    db.Index('c1sysschemaarticles', 'artid', 'pubid')
)



t_syssubscriptions = db.Table(
    'syssubscriptions',
    db.Column('artid', db.Integer, nullable=False),
    db.Column('srvid', db.SmallInteger, nullable=False),
    db.Column('dest_db', db.Unicode(128), nullable=False),
    db.Column('status', db.Integer, nullable=False),
    db.Column('sync_type', db.Integer, nullable=False),
    db.Column('login_name', db.Unicode(128), nullable=False),
    db.Column('subscription_type', db.Integer, nullable=False),
    db.Column('distribution_jobid', db.BINARY(16)),
    db.Column('timestamp', db.TIMESTAMP, nullable=False),
    db.Column('update_mode', db.Integer, nullable=False),
    db.Column('loopback_detection', db.BIT, nullable=False),
    db.Column('queued_reinit', db.BIT, nullable=False, server_default=db.FetchedValue()),
    db.Column('nosync_type', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('srvname', db.Unicode(128), nullable=False, server_default=db.FetchedValue()),
    db.Index('unc1syssubscriptions', 'artid', 'srvid', 'dest_db', 'srvname')
)



t_systranschemas = db.Table(
    'systranschemas',
    db.Column('tabid', db.Integer, nullable=False),
    db.Column('startlsn', db.BINARY(10), nullable=False, unique=True),
    db.Column('endlsn', db.BINARY(10), nullable=False),
    db.Column('typeid', db.Integer, nullable=False, server_default=db.FetchedValue())
)



t_v_SG_map = db.Table(
    'v_SG_map',
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('Domain', db.Unicode(200)),
    db.Column('TestType', db.Unicode(10)),
    db.Column('TestCase', db.Unicode(2000)),
    db.Column('FunID', db.Unicode(20))
)



t_v_test = db.Table(
    'v_test',
    db.Column('CodeLine', db.Unicode(50)),
    db.Column('ChangeList', db.Unicode(20)),
    db.Column('Domain', db.Unicode(200)),
    db.Column('TestType', db.Unicode(10)),
    db.Column('TestCase', db.Unicode(2000)),
    db.Column('SourceFile', db.Unicode(2000)),
    db.Column('FunctionName', db.Unicode(2000))
)
