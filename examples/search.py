import json
from time import sleep
from tinder import TinderClient

tc = TinderClient("501d1515-b84d-0c35-ef33-345901de5bf5")

sugar = None
c=0
n=0
checked_list = []

with open("ckd.json","r") as f:
    checked_list = json.loads(f.read())

while True:
    users = tc.get_recommendations()["results"]
    c+=1
    n+=len(users)
    print("\nscanned ",c," times and ",n," people")
    if len(users)==0:
        print("no more active user in this area")
        break
    else:
        sugar = [u for u in users if (u["name"]=="Sugar" or u["name"]=="sugar" )]
        if sugar:
            print("User found !!!")
            break
        else:
            print("Did not find users. Disliking them all...",end="")
            for u in users:
                if u["_id"] in checked_list:
                    print(" ",u["name"],"already checked")
                    sleep(10)
                else:
                    tc.dislike(u["_id"])
                    checked_list.append(u["_id"])
                    print(" ",u["name"],u["distance_mi"],end="")

with open("ckd.json","w") as f:
    f.write(json.dumps(checked_list))


print(sugar)
