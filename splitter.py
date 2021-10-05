import os
import time as ti

files_list = os.listdir()
files_str = " ".join(files_list)
files_csv = []

for f in files_list:
	if f.split('.')[-1] == 'csv':
		files_csv.append(f)

print(f"CSV files in current directory: {' '.join(files_csv)}")

start = ti.time()
files = os.listdir()


def splitcsv(file):
	csv_file = open(file, "r", encoding="utf-8").readlines()
	filename = 1
	files_csv_out = []
	for i in range(len(csv_file)):
		if i % 100000 == 0:
			open(file.split('.')[0] + '_' + str(filename) + ".csv", "w+", encoding='utf-8').writelines(
				csv_file[i: i + 100000])
			filename += 1
			files_csv_out.append(file.split('.')[0] + '_' + str(filename) + ".csv")
	print(f"Files added to directory: {' '.join(files_csv_out)}")


for f in files_list:
	ext = f.split('.')[-1]
	if ext == 'csv':
		splitcsv(f)

stop = ti.time()

print(f'elapsed {stop - start} seconds')
