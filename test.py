from github import Github
from drawer import drawObsidian
import time

g = Github("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")

initialUser = "lschwetlick"
users = [initialUser]
comer = initialUser
d = {}

counter = 0
done = False
while not done:
    if counter == 0:
        followers = g.get_user(users[counter]).get_followers()

    else:
        followers = users[counter].get_followers()
        comer = users[counter].login

    for i in followers:
        users.append(i)

    tl = []
    for i in followers:
        tl.append(i.login)
    d[comer] = tl 

    followers = []

    counter += 1
    print(f"{counter}/3000")


    if counter >= 50:
        done = True


drawObsidian(d)
