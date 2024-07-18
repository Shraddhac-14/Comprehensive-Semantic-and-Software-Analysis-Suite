import copy
import os, shutil
from git import Repo
import requests
import shutil
from bs4 import BeautifulSoup
import pprint



def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
# merge function ot cmbine a dictonary


opfile=open('out.txt','w+')

keyfile=open('Vvce\\Uploaded_files\\Topic.txt')
key=keyfile.read()
#mernkey2 = input()
url_to_call = "https://github.com/trending/"+key
print(url_to_call)
response=requests.get(url_to_call,headers={"User-Agent":"Mozilla/5.0"})
response_code = response.status_code
if response_code !=200:
    print("error")
html_content = response.content
dom = BeautifulSoup(html_content, 'html.parser')
# trending_repositories = []
repo = {}
all_trending_repo=dom.select("article.Box-row h1")
for each_trending_repo in all_trending_repo:
    href_link = each_trending_repo.a.attrs["href"]
    name = href_link[1:]
    # repo = {"label":name,
    #         "link":"https://github.com{}".format(href_link)}
    url="https://github.com{}".format(href_link)
    # trending_repositories.append(repo)
    repo[name]=url
if repo:
    # print(repo)
    pass
    #return trending_repositories
print("new scrape")    
url = "https://github.com/search?q=" + key + '&type='   
r = requests.get(url)
# print(r)
soup= BeautifulSoup(r.text,'html.parser')
# from bs4 import BeautifulSoup as soup
# from selenium import webdriver
# url = "https://github.com/"+key

# driver = webdriver.Firefox()
# driver.get(url)

# page = driver.page_source
# page_soup = soup(page,'html.parser')


li = soup.findAll('div',class_='f4 text-normal')
base_url = "https://github.com/"
link_dict={}

for _,i in enumerate(li):
    for a in i.findAll('a'):
        newUrl = base_url + a["href"]
    # print(_,i.text.strip(), newUrl) 
    link_dict[i.text.strip()]=newUrl
# print(link_dict)    
print("scrape over")

# url_to_call = "https://github.com/topics/"+key2
# print(url_to_call)
# response=requests.get(url_to_call,headers={"User-Agent":"Mozilla/5.0"})
# response_code = response.status_code
# if response_code !=200:
#     print("error")
# html_content = response.content
# dom = BeautifulSoup(html_content, 'html.parser')
# # trending_repositories = []
# repo = {}
# all_trending_repo=dom.select("h3.f3 color-fg-muted text-normal lh-condensed")
# for each_trending_repo in all_trending_repo:
#     href_link = each_trending_repo.a.attrs["href"]
#     name = href_link[1:]
#     # repo = {"label":name,
#     #         "link":"https://github.com{}".format(href_link)}
#     url="https://github.com{}".format(href_link)
#     # trending_repositories.append(repo)
#     repo[name]=url
# print(repo)    

final_link_dict= Merge(link_dict,repo)
print(final_link_dict)

stop_count=0
flag_list={}
line_list={}


for i,v in final_link_dict.items():
    # Repo.clone_from(v, f'backend\gitfiles\\f{stop_count}')
    print(i,v,'ffff')
    stop_count+=1
    if stop_count==5:
        break

    

for dirname in os.listdir('Vvce\\backend\\gitfiles'):
    # delete all non extension files
    for filename in os.listdir('Vvce\\backend\\gitfiles\\'+dirname):
        # f = os.path.join('backend\\gitfiles\\'+dirname, filename)
        f='Vvce\\backend\\gitfiles\\'+dirname+'\\'+filename
        # f='C:\\Users\\pooji\\OneDrive\\Desktop\\Vvce\\backend\\gitfiles\\f1\\JdBuyer.py'
        # print(f)

        if os.path.isfile(f):
            # try:
                flag_list={}
                line_list={}
                # the input file has to be in a text format
                # if it is not a text it should be converted into a text file
                
                with open('C:\\Users\\pooji\\OneDrive\\Desktop\\Vvce\\Uploaded_files\\Studentfile\\file2.txt') as file1, open(f, 'r',encoding='cp850') as file2:
                    lines_of_file1 = file1.readlines()
                    # print(lines_of_file1,'2222')
                    lines_of_file2 = file2.readlines()
                    print(lines_of_file2)
                    print(lines_of_file1)
                    for i in lines_of_file1:
                        for j in  lines_of_file2:
                            if i in j:
                                print('line',str(lines_of_file1.index(i)),'     found at '+str( lines_of_file2.index(j)) + 'of file', str( file2.name ))

                    # line_num=0
                    # lines_of_file1=''.join(lines_of_file1)
                    # # lines_of_file2_str=''.join(lines_of_file2)
                    # for i in lines_of_file1:
                    #     for j in lines_of_file2:
                    #         if i==j:
                    #             opfile.write(i[:20].replace('\n','')+ str(lines_of_file1.index(i)) + '....'+'  was found at line number: '+ str(line_num)+' in file '+str(file2.name.split('\\')[-1])+'\n\n\n')








                    # a=lines_of_file2_str
                    # print(lines_of_file2)
                    # check each line in file 1 for in test file for match
                    # lines_of_file1_deep = copy.deepcopy(lines_of_file1)
#                     for line1 in lines_of_file1:
#                         line_num+=1
#                         if line1 in a:
                            
#                         # print(len(line1))
#                             print(line1)
#                         # print(len(lines_of_file1))
#                         # print(line1,'kkkkk')
#                             opfile.write(line1[:20].replace('\n','')+ str(lines_of_file1.index(line1)) + '....'+'  was found at line number: '+ str(line_num)+' in file '+str(file2.name.split('\\')[-1])+'\n\n\n')
#                             # print(file2.name)
#                                     # try:
#                                     #     if file1.name.split('\\')[-1] not in flag_list:
#                                     #         flag_list[file1.name.split('\\')[-1]]=[]
#                                     #     flag_list[file1.name.split('\\')[-1]].append(line1)
#                                     #     # display output as (from this file we have copied theese lines)
#                                     #     line_list[line_num]=file2.name.split('\\')[-1]
#                                     # except :
#                                     #     flag_list.update({file1.name.split('\\')[-1]:line1})
#                                     #     # y_dict["Name"].append("Guru")


#                         # print(line1)
#                     #     for line2 in lines_of_file2:
#                     #         # print(line2)
#                     #         if line1 in line2:
#                     #             if file1.name.split('\\')[-1] in flag_list:
#                     #                 flag_list[file1.name.split('\\')[-1]].append(line1)
#                     #                 # display output as (from this file we have copied theese lines)
#                     #                 line_list[line_num]=file2.name  +  '  ' + str(lines_of_file2.index(line2)+1)
#                     #                 # this line has been copied from this file at this number

#                     #             else:
#                     #                 flag_list[file1.name.split('\\')[-1]]=[line1]
#             # except:
#             #     pass
#     # flag_list_keys=[i for i,_ in flag_list]
#     # flag_lsit_keys_priority_list={}
#     # for i in flag_list_keys:
#         # flag_lsit_keys_priority_list[i]=flag_list_keys.count(i)
#     # priotity_dict={i,flag_list_keys.count(i) for i,v in }

# # flag_list_key_length={}

# # for i,v in flag_list.items():
# #     flag_list_key_length[i]=len(flag_list[i])
# # a = sorted(flag_list_key_length.items(), key=lambda x: x[1],reverse=True)    
# # print(a)
# # for i in a: 
# #     print(flag_list,line_list)
# #     print()

# # print(line_list,flag_list)

# # for ele in flag_list:
# #     print(*flag_list[ele])
# #     print(line_list)




