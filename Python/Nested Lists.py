# Link: https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    main = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main.append([name,score])
    removers = []
    minimum=100000
    for y in main:
        if y[1]<minimum:
            minimum=y[1]
    remove = []
    for y in main:
        if y[1]==minimum:
            remove.append(y)
    for e in remove:
        main.remove(e)
    minimum=100000
    for y in main:
        if y[1]<minimum:
            minimum=y[1]
    final = []
    for t in main:
        if t[1]==minimum:
            final.append(t[0])
    for w in sorted(final):
        print(w)
