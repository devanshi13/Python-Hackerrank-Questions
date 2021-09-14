def solve(s):
    name = s.split(' ')
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    NameCaps = ' '.join(word for word in name)
    return NameCaps

if __name__ == '__main__':
    s = input("Enter String/Name ")
    result = solve(s)
    print(result)