def drawObsidian(d):
    for i in d:
        for j in range(len(d[i])):
            d[i][j] = f"[[{d[i][j]}]]"

    for i in d:
        with open(f'Data/{i}.md', 'w') as f:
            for j in d[i]:
                f.write(f"{j} \n")
