# 2) შექმენით ორი ლისთი და ლუპის მეშევოებით შექმენით ახალი ლისთი რომელიც იქნება ამ ორის გაერთანება

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = []

for item in list1:
    combined_list.append(item)

for item in list2:
    combined_list.append(item)

print(combined_list)