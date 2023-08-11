
ch = "y"
l = ["b", "c"]
while ch != "n":
    inp = input("b or c")
    l.append(inp)
    c = l.count("b")
    d = len(l)
    # print(l)
    p = c/d
    print(p)

    ch = input("cont?> ")

ch = "y"
while ch != "n":
    if p > 0.5:
        print("b")
        o = input("Correct?")
        if o == "y":
            l.append("b")
        else:
            l.append("c")
    else:
        print("c")
        o = input("Correct?")
        if o != "y":
            l.append("b")
        else:
            l.append("c")
    c = l.count("b")
    d = len(l)
    # print(l)
    p = c/d
    print(p)
    print(l)
    ch = input("cont?> ")

