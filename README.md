# Easy Python3 Logging.
Welcome to SmartLogging for Python3!

You can use this as a tool when you are developing.
# Simple to use
It's super easy to setup. Just take 30 seconds and it can save your time of tracing errors.

    from errors import StatusMonitor # Trace your errors.
    from errors import printlog as print # Make every print CLEAR.

# Clear, Always.

    import .......
    def Token_Generator():
        ......
        yield ...
    
    def ConnectionHandler():
        Socket=socket()
        ......
        while True:
            print('Waiting for connection...')
            sx,addr=Socket.accept()
            # DO SOMETHING
            sx.close()
    
    TokenGen = Token_Generator()    
    print('Initialized. Lauching server...')
    ConnectionHandler()
            
Will give you an output like:

    [Info] Starting Token_Generator <function Token_Generator at 0x0000000004A82048> with args () and kwargs {} :
    [Info] Finalizing Token_Generator <function Token_Generator at 0x0000000004A82048> with return <generator object Token_Generator at 0x000000000466E7C8>
    [Output] Initialized. Lauching server...
    [Info] Starting ConnectionHandler <function ConnectionHandler at 0x0000000004A82620> with args () and kwargs {} :
            [Output] Successfully launched.
            [Output] Waiting for connection...

It will use \t to indicate a call of function.

# Functions
## errors.StatusMonitor(allow_error=SYS_ALLOW_ERROR,print_error=SYS_PRINT_ERROR,print_verbose=SYS_PRINT_VERBOSE):
*Default Values:*

SYS_ALLOW_ERROR=False

SYS_PRINT_VERBOSE=True

SYS_PRINT_ERROR=True

## errors.printlog(*args,level='[Output]',**kw):
It will automatically add \t and level to the front of the text. All the other args and kw will be passed to errors.print

## errors.print(*args,**kw):
It will create a PRINTLOCK which can prevent logs being very messy.
All the args and kw will be passed to print.
