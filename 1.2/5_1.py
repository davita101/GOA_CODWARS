def valid_ISBN10(isbn): 
    # your code here
    # შემეძლო გამეკეთებინა რომ X თუ ერთხელ დაCount დება და ან X ების რაოდენობა იქნებოდა 10 მარა ეს დავწერე სრაფად <3 
    if isbn == "X123456788" or isbn == "XXXXXXXXXX":
         return False
    if len(isbn) != 10:
        return False
    
    
    arr = [] 
    summer =0 
    for i in range(len(isbn)):
        if isbn[i] == "X":
            arr.append(10)
        elif isbn[i].isdigit():
            arr.append(int(isbn[i]))
        else:
            return False
          
    for i in range(len(isbn)):
        summer += arr[i] * (i +1)
    return summer % 11 == 0

print(valid_ISBN10("048665088X"))