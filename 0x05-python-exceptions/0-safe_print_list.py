def safe_print_list(my_list=[], x=0):
    try:
        printed_count = 0
        for i in my_list:
            if printed_count < x:
                print(i, end=' ')
                printed_count += 1
        print()  # Add a new line after printing the elements
        return printed_count
    except Exception as e:
        print(f"Error: {e}")
        return 0
