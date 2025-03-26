Score = int(input("whats your Score"))
if 90 <= Score <= 100:
    print("Your possition is excellent")
elif 80 <= Score < 89:
    print("very good")
elif 70 <= Score < 79:
    print ("good")
elif 60 <= Score < 69:
    print ("satisfactory")
elif 50 <= Score < 59:
    print ("needs improvement")
elif 0 <= Score < 49:
    print("fail")
else:
    print ("invalid Score, input a number between 0 to 100")
    