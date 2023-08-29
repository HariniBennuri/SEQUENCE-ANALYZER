def sequence(string: str) -> int:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = []
    for i in string:
        number_str.append(alphabet.index(i))
    i = number_str
    step = i[2] - i[0]
    if(alphabet[i[4]] == alphabet[(i[2] + step) % 26]):
        return 2
    else:
        return 3
def result( string: str) ->str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = []
    res = " "
    for i in string:
        number_str.append(alphabet.index(i))
    if sequence(string) == 2:
        step1 = number_str[2] - number_str[0]
        step2 = number_str[3] - number_str[1]
        letter = alphabet * 12
        if len(string) % 2 == 0:
            count = 0
            while(count < 6):
                res += letter[((number_str[-2] + (count + 1) * step1))]
                res += letter[((number_str[-1] + (count + 1) * step2))]
                count += 1
            return res
    if sequence(string) == 3:
        letter = alphabet * 12
        step1 = number_str[3] - number_str[0]
        step2 = number_str[4] - number_str[1]
        step3 = number_str[5] - number_str[2]
        if step1 < 0:
            step1 = 26 + step1
        if step2 < 0:
            step2 = 26 + step2
        if step3 < 0:
            step3 = 26 + step3
        if len(string) % 3 == 0:
            count = 0
            while(count < 4):
                res += letter[((number_str[-3] + (count + 1) * step1))]
                res += letter[((number_str[-2] + (count + 1) * step2))]
                res += letter[((number_str[-1] + (count + 1) * step3))]
                count += 1
            return res
print("NOTE : Dear user please enter only 12 character string with sequence!!\n")
input1=input("enter 1st string: ")
input2=input("enter 2nd string: ")       
print(result(input1))
print(result(input2))
