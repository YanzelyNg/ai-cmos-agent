def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

def current_mirror(i_ref, ratio):
    return i_ref * ratio
