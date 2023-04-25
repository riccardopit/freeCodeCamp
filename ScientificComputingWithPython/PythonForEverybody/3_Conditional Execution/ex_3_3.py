score = input("Enter score: ")
try:
    s = float(score)    #score
    if s < 0.0 or s > 1.0:
        print("Score out of range!")
    else:
        if s >= 0.9:
            print("A")
        elif s >= 0.8:
            print("B")
        elif s >= 0.7:
            print("C")
        elif s >= 0.6:
            print("D")
        elif s < 0.6:
            print("F")
except:
    print("Input not valid!")