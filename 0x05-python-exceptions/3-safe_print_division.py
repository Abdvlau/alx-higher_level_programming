def safe_print_division(a, b):
    try:
        result= int(a) / int(b)     
    
    except ZeroDivisionError:
        print(None)
            
    finally:
        try:
             print("{:d} / {:d} = {}".format(a, b, result))
        except NameError:
            print("Inside result: None")
