import random

def Alotto_numbers():
    return sorted(random.sample(range(1, 45), 6))

def main():
    lotto_numbers = Alotto_numbers()
    print("생성된 로또번호는 {}입니다".format(lotto_numbers))

    number_list = {}
    not_in_number_list = [number for number in lotto_numbers if number not in number_list]

    for number in not_in_number_list:
        print("{}은 number_list에 해당 숫자가 없습니다.".format(number))

if __name__ == "__main__":
    main()




