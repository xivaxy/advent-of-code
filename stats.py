import requests, re, time

def get_leaderboard_page(year, day):
    url = 'https://adventofcode.com/' + str(year) + '/leaderboard/day/' + str(day)
    return requests.get(url).text


marker100= '"leaderboard-position">100)'

def extract100time(page: str):
    # extract time of solution from line <span class="leaderboard-position">100)</span> <span class="leaderboard-time">Dec 07  00:16:00</span>  <span
    groups = re.findall(r'<span class="leaderboard-position">100\)</span> <span class="leaderboard-time">(.*?)</span>', page)
    res = []
    for i in range(2):
        ts = groups[i]
        ts = ts.split("  ")[1]
        t = ts.split(":")
        res.append(int(t[0])*60 + int(t[1]) + int(t[2])/60)
    return res


for i in range(25, 0, -1):
    t2, t1 = extract100time(get_leaderboard_page(2023, i))
    print(i, t1, t2)
    time.sleep(1)


