def divisors(num):
    divisors =[i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    try:
        num = int(input("ingresa un numero :"))
        if num <= 0:
            raise ValueError ("no se aceptan numeros negativos")  
        print(divisors(num))
        print("termina el programa")
    except ValueError as Va:
        print(Va)
        return False 
    


if __name__ == '__main__':
    run()