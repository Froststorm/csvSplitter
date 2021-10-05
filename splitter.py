import os

files = os.listdir()

for f in files:
	print(f)

# os.path.(PATHS[0])
# print(os.getcwd())


# csvfile = open("atu_atu.csv", "r", encoding="utf-8").readlines()
# filename = 1
# for i in range(len(csvfile)):
#     if i % 100000 == 0:
#         open(str(filename) + ".csv", "w+").writelines(csvfile[i : i + 1000])
#         filename += 1
#
# print(os.listdir())
