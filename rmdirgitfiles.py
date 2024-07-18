import os

# x=open(f)
# print(f)

for dirname in os.listdir('backend\\gitfiles'):
    # delete all non extension files
    for filename in os.listdir('backend\\gitfiles\\'+dirname):
        # f = os.path.join('backend\\gitfiles\\'+dirname, filename)
        f='backend\\gitfiles\\'+dirname+'\\'+filename
        # print(filename)
        # f= 'backend\gitfiles\f0\__main__.py'
        if os.path.isfile(f):
            # try:
                flag_list={}
                line_list={}
                # the input file has to be in a text format
                # if it is not a text it should be converted into a text file
                with open('C:\\Users\\pooji\\OneDrive\\Desktop\\Vvce\\Uploaded_files\\Studentfile\\file2.txt') as file1, open(f, 'r',encoding='cp850') as file2:
                    lines_of_file1 = file1.readlines()
                    lines_of_file2=file2.readlines()
                    # print(lines_of_file2)
                    # print(f1)
                    line_num=0
                    # check each line in file 1 for in test file for match
                    for line1 in lines_of_file1:
                        line_num+=1
                        for line2 in lines_of_file2:
                            if line1==line2:
                                if file1.name.split('\\')[-1] in flag_list:
                                    flag_list[file1.name.split('\\')[-1]].append(line1)
                                    # display output as (from this file we have copied theese lines)
                                    line_list[line_num]=file2.name  +  '  ' + str(lines_of_file2.index(line2)+1)
                                    # this line has been copied from this file at this number

                                else:
                                    flag_list[file1.name.split('\\')[-1]]=[line1]
            # except:
            #     pass
    # flag_list_keys=[i for i,_ in flag_list]
    # flag_lsit_keys_priority_list={}
    # for i in flag_list_keys:
        # flag_lsit_keys_priority_list[i]=flag_list_keys.count(i)
    # priotity_dict={i,flag_list_keys.count(i) for i,v in }

    flag_list_key_length={}

for i,v in flag_list.items():
    flag_list_key_length[i]=len(flag_list[i])
a = sorted(flag_list_key_length.items(), key=lambda x: x[1],reverse=True)    
print(a)
for i in a: 
    print(flag_list[i[0]])
    print()

# for ele in flag_list:
#     print(*flag_list[ele])
#     print(line_list)




