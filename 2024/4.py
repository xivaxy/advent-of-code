from aocd import data, submit

s='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
test = False
if test:
    data=s
ans=0
lines = data.split('\n')

if False:
    patterns = ["XMAS", "SAMX"]
    a = data
    for pattern in patterns:
        ans+=a.count(pattern)

    transposed = list(map(list, zip(*lines)))
    a = "\n".join(["".join(x) for x in transposed])
    for pattern in patterns:
        ans+=a.count(pattern)

    all_diagonals = []
    for i in range(len(lines)):
        all_diagonals.append("".join([lines[i+x][x] for x in range(len(lines)-i)]))
        if i>0:
            all_diagonals.append("".join([lines[x][i+x] for x in range(len(lines)-i)]))
        all_diagonals.append("".join([lines[i+x][len(lines)-1-x] for x in range(len(lines)-i)]))
        if i>0:
            all_diagonals.append("".join([lines[x][len(lines)-1-i-x] for x in range(len(lines)-i)]))

    for pattern in patterns:
        for diagonal in all_diagonals:
            ans+=diagonal.count(pattern)

for i in range(1,len(lines)-1):
    for j in range(1,len(lines[0])-1):
        if lines[i][j] == "A":
            corners = [lines[i-1][j-1], lines[i-1][j+1], lines[i+1][j-1], lines[i+1][j+1]]
            if corners.count("M") == 2 and corners.count("S") == 2:
                if corners[1]!=corners[2]:
                    ans+=1

print(ans)
if not test:
    submit(ans)