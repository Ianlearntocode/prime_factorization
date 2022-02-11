product = []
new = []
def prime_factorization(num):

    while True:
        # num = input('請輸入一個大於0整數: ')
        # if num == 'q':
        #     break
        # num = int(num)
        # if num <= 0:
        #     print('別鬧')
        # elif num == 1:
        #     print('1 = 1')
        # else:
        if num >= 2:    
            x = 2
            c = 0
            while x <= num:
                if num % x != 0:
                    x += 1
                    c = 0 
                else:
                    p = []
                    num = num / x
                    c += 1
                    p.append(x)
                    p.append(c)
                    product.append(p)
        else:
            break

def sim(s,w):
    w.append(s[0])
    for t in range(1, len(s)):
        if s[t][0] == s[t-1][0]:
            w[-1] = s[t]
        else:
            w.append(s[t])


def show(n,s):
    b = ''
    for i in range(len(s)):
        b += f'{s[i][0]}^{s[i][1]}*'
        print(n,'= ',b[:-1] )


def main():
    num = int(input('請輸入一個大於0整數: '))
    prime_factorization(num)
    sim(product,new)
    print(new)
    show(num,new)



main()
