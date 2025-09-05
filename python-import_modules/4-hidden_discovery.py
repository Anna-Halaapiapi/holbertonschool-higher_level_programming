#!/usr/bin/python3.10

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for i in range(len(names)):
        if (names[i][0] != '_' or names[i][1] !='_'):
            print(names[i])
