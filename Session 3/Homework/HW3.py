from HW1 import customers_collection
import matplotlib.pyplot as plt

ads = []
events = []
wom = []

if __name__ == "__main__":
    customers_list = customers_collection.find()

    for customer in customers_list:
        if customer["ref"] == "ads":
            ads.append(customer)
        elif customer["ref"] == "events":
            events.append(customer)
        else:
            wom.append(customer)

lists = [len(ads), len(events), len(wom)]
activities = ["Advertisement", "Events", "Word of mouth"]
colors = ["green", "blue", "red"]

plt.pie(
    lists, 
    labels= activities, 
    colors= colors,
    autopct='%1.1f%%',
    startangle=150
)
 
plt.axis("equal")
plt.show()