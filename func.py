def func_allow(context):
    print("Hi from inside the func_allow")
    return 1


def func_prevent(context):
    print("Hi from inside the func_prevent")
    return 1


def func_constrain(context):
    print("Hi from inside the func_constrain")
    return 1

def func_error(context):
    print("start of func_error")
    x = {"amit":"elbaz"}
    y = x['gilad']
    print("end of func_error")
    return 1
