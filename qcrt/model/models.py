# coding: utf-8
from qcrt import db


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

