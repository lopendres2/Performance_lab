import sys

def main(n_value, m_value):
    arr = [i + 1 for i in range(n_value)]

    current = 0
    print("Ответ: ", end="")
    while True:
        print(arr[current], end="")
        current = (current + m_value - 1) % n_value
        if current == 0:
            break

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <количество элементов в массиве> <интервал>")
    else:
        n_value = int(sys.argv[1])
        m_value = int(sys.argv[2])
        main(n_value, m_value)
