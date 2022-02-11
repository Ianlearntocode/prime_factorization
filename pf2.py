product = []
def prime_factorization(num):
    if num >= 2:    
        x = 2
        while x <= num:
            if num % x != 0:
                x += 1
            else:
                product.append(x)
                num = num / x
    else:
        print('不能分')
    



def main():
    num = input('請輸入數字: ')
    num = int(num)
    prime_factorization(num)
    print(product)
    print(num,'=','*'.join(map(str,product))) #把列表的每一個元素用*連線起來


main()