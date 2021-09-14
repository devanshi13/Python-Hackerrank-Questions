def count_substring(string, sub_string):
    c = 0
    ssl = len(sub_string)
    for i in range(0,len(string)-2):
        scom = string[i:ssl+i]
        if sub_string == scom:
            c += 1
    return c

if __name__ == '__main__':
    string = input("Enter String ").strip()
    sub_string = input("Enter Substring ").strip()
    
    count = count_substring(string, sub_string)
    print(count)