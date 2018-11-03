#Created by Lincoln Yan - https://github.com/yyjlincoln
#Date: 20181103

#imports
from functools import wraps
#Default Error Logging
SYS_ALLOW_ERROR=False
SYS_PRINT_VERBOSE=True
SYS_PRINT_ERROR=True

Sep=''
rawprint=print
PRINTLOCK=False

#Error Printing
def StatusMonitor(allow_error=SYS_ALLOW_ERROR,print_error=SYS_PRINT_ERROR,print_verbose=SYS_PRINT_VERBOSE):
    def Status(function):
        @wraps(function)
        def log(*args,**kw):
            global Sep
            ErrorFlag=None
            try:
                if print_verbose:
                    print(Sep+'[Info] Starting',function.__name__,function,'with args',args,'and kwargs',kw,':')
                    Sep+='\t'
                ret=function(*args,**kw)
            except Exception as e:
                ErrorFlag=e
                ret=-9999
                if print_error:
                    print(Sep+'[Error]',e,':')
                    print(Sep+'\tWhen Running',function.__name__,function)
            finally:
                if print_verbose:
                    Sep=Sep[0:len(Sep)-1]
                    if ErrorFlag:
                        print(Sep+'[Info] Finalizing',function.__name__,function,'with Exception')
                    else:
                        print(Sep+'[Info] Finalizing',function.__name__,function,'with return',ret)
                if ErrorFlag and not allow_error:
                    ORIGINAL_EXCEPTION_ABOVE=ErrorFlag
                    raise ORIGINAL_EXCEPTION_ABOVE
                return ret
        return log
    return Status

@wraps(print)
def printlog(*args,level='[Output]',**kw):
    print(Sep+level,end=' ')
    print(*args,**kw)

def print(*args,**kw):
    global PRINTLOCK
    while PRINTLOCK==True:
        # rawprint('PRINTLOCK DENIED')
        pass
    PRINTLOCK=True
    rawprint(*args,**kw)
    PRINTLOCK=False