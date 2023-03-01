n = input()
def f(n):
    if (int(n) % 4 == 0 and int(n) % 100 != 0) or (int(n) % 400 == 0):
        return "Год" + " " + str(n) + " " + "- високосный"
    else:
        return "Этот год не високосный"
print(f(n))