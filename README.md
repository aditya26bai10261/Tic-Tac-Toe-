    def show(a):
        print()
        print(a[0], "|", a[1], "|", a[2])
        print("--+---+--")
        print(a[3], "|", a[4], "|", a[5])
        print("--+---+--")
        print(a[6], "|", a[7], "|", a[8])
        print()


    def check(a, p):
        lines = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]

        for x, y, z in lines:
          if a[x] == p and a[y] == p and a[z] == p:
            return True
        return False


    a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    p = "X"
    moves = 0

    print("TIC TAC TOE")

    while True:
        show(a)

        try:
           n = int(input("Player " + p + ", enter position: ")) - 1
        except ValueError:
           print("Enter a number.")
           continue

        if n < 0 or n > 8:
           print("Choose between 1 and 9.")
           continue

        if a[n] == "X" or a[n] == "O":
           print("This place is already used.")
           continue

        a[n] = p
        moves = moves + 1

        if check(a, p):
           show(a)
           print("Player", p, "wins!")
           break

        if moves == 9:
           show(a)
           print("It's a draw!")
           break

        if p == "X":
           p = "O"
        else:
           p = "X"
