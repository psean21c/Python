import sys
import datetime, time
#
'''
Key, Value = TABLE_NAME, List[A, B]
- TableName will be used for Key in Dictionary
- Where A,B are integers which are the count number of records in the table.

PIPER_PRD_OWNER.ACT_HI_ACTINST	:18	20


'''
#
def readFiles(file1, file2, file3):
	# 1) Get the result from the 1st file
	#print(file1 + ":" + file2)
	lst1 = []
	with open(file1, "r") as f1:
		data1 = f1.readlines()
		
	for line in data1:
		count = line.split()
		lst1.append(count[0])
		
	results1 = list(map(int, lst1))
	#print(results1)

	# 2) Get the result from the 2nd file
	lst2 = []
	with open(file2, "r") as f2:
		data2 = f2.readlines()
		
	for line in data2:
		count = line.split()
		lst2.append(count[0])
		
	results2 = list(map(int, lst2))
	#print(results2)

	# 3) Use dictoinary : TableName will be used for Key in Dictionary
	dict = {}
	print(file3)
	
	with open(file3, "r") as f3:
		data3 = f3.readlines()
		#print(data2)
	
	# 4) Set the key(table_name), value (1st,2nd)
	cnt = 0
	idx = 0
	for line in data3:
		names = line.split()
		pair = []
		if (cnt % 2 ==0):
			#print (names[3] + ":\t" + lst1[idx] + ":" + lst2[idx] )
			pair.append(lst1[idx])
			pair.append(lst2[idx])
			dict[names[3]] = pair
			idx = idx + 1
		cnt = cnt + 1

	# 5) Prepare the output file
	out_file_name = "impacted-tables-" + file_suffix() + ".txt"
	out = open(out_file_name,"w") 
	# Need a format to print aligned..
	header = '{:^55}'.format("Table Name") + "" + '{:>10}'.format("BEFORE") + "" + '{:>10}'.format("AFTER") + "\n"
	separator = '{:^55}'.format("=========================================") + "" + '{:>10}'.format("=======") + "" + '{:>10}'.format("=======") + "\n"
	out.write(header)
	out.write(separator)
	
	# 6) Detect which tables are impacted from the activities..
	for key,value in dict.items():
		#str = key + "\t:" + value[0] + "\t" + value[1] + "\n"
		str = '{:55}'.format(key) + "" + '{:>10}'.format( value[0]) + "" + '{:>10}'.format(value[1]) + "\n"
		print(str) 
		v1 = int(value[0])
		v2 = int(value[1])
		if(v1 != v2):
			print("\t" + str) 
			out.write(str) 
		
		#print(key + "," + dict[key])
		#key, 'corresponds to', d[key]
	
	f1.close()
	f2.close()
	f3.close()
	out.close()

'''
return the string value for file suffix : i.e. 2018-05-08-22h49m
'''
def file_suffix():
	today = datetime.date.today()
	#print(today)
	
	ts = datetime.datetime.now()
	timestamp = str(ts.hour) + "h" + str(ts.minute) + "m"
	#print(str(ts) + ":\t" + timestamp)
	
	suffix = str(today) + "-" + timestamp
	#print(suffix)
	return suffix
	
'''
- How to run 
$ python result1.txt result2.txt count.sql

>> Will fail if the count of all files are difference

'''		
if __name__ == "__main__":
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	file3 = sys.argv[3]
	readFiles(file1, file2, file3)

