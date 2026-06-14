def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)
