def arithmetic_arranger(problems, *args):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    mylist = []
    
    for problem in problems:
        mylist.append(problem.split())

    row_1 = ""  #first row
    row_2 = ""  #second row
    row_3 = ""  #third row
    row_4 = ""  #fourth row

    mylist_len = len(mylist)
    count = 0   #cycle counter
    for problem in mylist:

        num_len = len(max(problem, key=len))
        problem.append(num_len)

        num_1 = problem[0] #first operand
        op = problem[1] #operator
        num_2 = problem[2] #second operand
        num_max_len = problem[3]   #longest operand length
        
        if not(num_1.isdigit()) or not(num_2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if  len(num_1) > 4 or len(num_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if op == "+":
            result = int(num_1) + int(num_2)
        elif op == "-":
            result = int(num_1) - int(num_2)
        else:
            return "Error: Operator must be '+' or '-'."
        problem.append(str(result))

        sol = problem[4]  #solution

        offset = 1 + 1  #number of spaces between sign and longest operand + space occupied by operator

        #first row
        row_1 += num_1.rjust(num_max_len + offset)
        if count < mylist_len - 1:  #-1 because spaces are not necessary after last problem
            row_1 += "    "
        
        #second row
        row_2 += op + " " + num_2.rjust(num_max_len)
        if count < mylist_len - 1:  #-1 because spaces are not necessary after last problem
            row_2 += "    "
        
        #third row
        row_3 += "".join("-"*(num_max_len + offset))
        if count < mylist_len - 1:  #-1 because spaces are not necessary after last problem
            row_3 += "    "
        
        #fourth row
        row_4 += sol.rjust(num_max_len + offset)
        if count < mylist_len - 1:  #-1 because spaces are not necessary after last problem
            row_4 += "    "
        
        count += 1
    
    if args:
        arranged_problems = row_1 + "\n" + row_2 + "\n" + row_3 + "\n" + row_4
    else:
        arranged_problems = row_1 + "\n" + row_2 + "\n" + row_3
    
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))