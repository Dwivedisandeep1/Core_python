def func():
    try:
        l = [1,5,6,7]
        i = int(input("Enter The index: "))

        print(l[i])
        return 0
    except:
        print("Some Error Occured")
        return 1

    finally:
        print("I am always executed")

x = func()
print(x)