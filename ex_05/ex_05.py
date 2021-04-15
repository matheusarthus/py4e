count = 0
totalSum = 0

while True:
    try:
        inSomething = input("> ")

        if inSomething == "done":
            print("Count:", count)
            print("Total:", totalSum)
            if count != 0:
                print("Average:", totalSum / count)
            break
            
        inNumberFloat = float(inSomething)

        count = count + 1
        totalSum = totalSum + inNumberFloat
    except:
        print("Invalid input")
