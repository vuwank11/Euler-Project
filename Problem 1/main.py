# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def sum_of_multiples(num):
    sum = 0
    for i in range(num):
        if i % 3 ==0 or i % 5 ==0:
            sum += i

    return sum



if __name__ == '__main__':
    num = 19564
    sum = sum_of_multiples(num)
    print(sum)
