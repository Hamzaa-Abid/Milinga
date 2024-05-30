import datetime

def toTimestamp(oDateTime):
    return datetime.datetime.timestamp(oDateTime)*1000

def fromTimestamp(iTimestamp):
    return datetime.datetime.fromtimestamp(iTimestamp//1000)

def toDate(oDate):
    return datetime.date.isoformat(oDate)

def fromDate(sDate):
    raise NameError('not implemented')

def now():
    return datetime.datetime.now()

def nowToTimestamp():
    return datetime.datetime.now().timestamp()*1000