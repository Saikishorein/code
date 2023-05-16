import string

def main():
    i = 0
    j = 0
    x = 0
    add = []
    d = []
    expr = input("Expression terminated by $: ")
    n = len(expr) - 1
    
    print("Given Expression:", expr)
    print("\nSymbol Table")
    print("Symbol \t addr \t type")
    
    while j <= n:
        c = expr[j]
        if c.isalpha():
            p = str(c)
            add.append(p)
            d.append(c)
            print(f"{c} \t {p} \t identifier")
            x += 1
            j += 1
        elif c.isdigit():
            p = str(c)
            add.append(p)
            d.append(c)
            print(f"{c} \t {p} \t constant")
            x += 1
            j += 1
        else:
            ch = c
            if ch in ['+', '-', '*', '=']:
                p = str(ch)
                add.append(p)
                d.append(ch)
                print(f"{ch} \t {p} \t operator")
                x += 1
                j += 1
            else:
                j += 1

if __name__ == "__main__":
    main()
