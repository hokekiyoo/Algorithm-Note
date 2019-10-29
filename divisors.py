"""
# 約数列挙
"""
def make_divisors(n):
    """
    input
        n : 整数
    output
        divisort : 約数のリスト
    """
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

if __name__ == "__main__":
    n = int(input())
    divs = make_divisors(n)
    divs.sort()
    print(divs)