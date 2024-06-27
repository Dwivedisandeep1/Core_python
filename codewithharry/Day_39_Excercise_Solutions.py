questions =[["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript", "Php", "None", 4]
            ,["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript", "Php", "None", 4]
            ,["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript", "Php", "None", 4]
            ,["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript", "Php", "None", 4]
            ,["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript", "Php", "None", 4]
            ,["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],
            ["Which language was used to create fb?", "Python",
             "French", "Javascript","Php","None",4],]

levels = [1000,2000,3000,5000,10000,20000,40000,
          80000,160000,320000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"question for rs {[levels[i]]}")
    print(f"a. {question[1]}")
    print(f"a. {question[2]}")
    print(f"a. {question[3]}")
    print(f"a. {question[4]}")

    reply = int(input("Enter your answer(1-4)"))

    if reply == question[-1]:
        print(f"Correct answer, you have won rs{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print(f"Wrong Answer")
        break


print(f"your take home money is {money}")