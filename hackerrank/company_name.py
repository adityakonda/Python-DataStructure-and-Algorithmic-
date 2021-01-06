

def company_name(input):

    input = sorted(input)

    logo = ''
    logo_occ = {}
    for ch in input:
        if len(logo) < 3 and ch not in logo:
            logo += ch

    print(logo)

    for i in logo:
        count = 0
        for ch in input:
            if i == ch:
                count += 1

        logo_occ[i] = count
        print(i, count)

    logo_o = sorted(logo_occ.items(), key = lambda x: x[1], reverse= True)

    for k, v in logo_o.items():
        print("-->",k, v)

    print(logo_occ)







if __name__ == '__main__':
    company_name("aabbbccde")
