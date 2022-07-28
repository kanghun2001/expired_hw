import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class PostCovidMindism:
    
    def __init__(self, funny, schlunch, friends, artsport, work, school):
        self.funny = funny
        self.schlunch = schlunch
        self.friends = friends
        self.artsport = artsport
        self.work = work
        self.school = school
        
    @staticmethod    
    def mean(lst):
        temp = [0, 0, 0, 0, 0]
        for n in range(0, len(lst)):
            temp[0] = temp[0] + lst[n].funny
            temp[1] = temp[1] + lst[n].schlunch
            temp[2] = temp[2] + lst[n].friends
            temp[3] = temp[3] + lst[n].artsport
            temp[4] = temp[4] + lst[n].work
        for k in range(0, 5):
            temp[k] = temp[k] / len(lst)
            yield temp[k]
        

    
class MemoryList(PostCovidMindism):

    
    
    def __init__(self, funny, schlunch, friends, artsport, work, school,edulist):
        self.funny = funny
        self.schlunch = schlunch
        self.friends = friends
        self.artsport = artsport
        self.work = work
        self.school = school
        self.edulist = edulist
        

    def register_kid(self, edulist, school):
        self.edulist = edulist
        self.school = school
      
lst = []
for n in range(0, 5):
    edutext = open("edutext"+str(n+1)+".txt", "r", encoding='utf8')
    txt = ''
    gr = []
    ce = []
    school = input("학교 이름: ")
    print("각 지수는 0(최악) 이상 100(최상) 이하로 입력해주세요\n")
    funny = input("학교가 전반적으로 재밌던 정도: ")
    
    
    schlunch = input(" 급식이 얼마나 맛있는지: ")
    friends = input(" 친구는 얼마나 사귀었는지: ")
    artsport = input(" 예체능 수업이 재밌던 정도: ")
    work = input("현장실습은 얼마나 하였는지: 한 적 없으면 0 입력: \n")
    subject = ""
    grade = ""
    while True:
        line = edutext.readline()
        if line == "* 내신/학점 *\n":
            continue
        elif line == "":
            break
        else:
            try:
                gr.append(line.split(" "))

            except ValueError:
                ce.append(line)
    edulist = gr
    mem = MemoryList(int(funny), int(schlunch), int(friends), int(artsport), int(work), school, edulist)
    mem.register_kid(edulist, school)
    edutext.close()
    lst.insert(n, mem)

schl = input("찾으려는 학교의 이름을 입력하시오: ")
temp = []
for n in range(0, 5):
    if lst[n].school == schl:
        temp.append(lst[n])
        
    else:
        continue
mean = MemoryList.mean(temp)
print(schl+"의 재미지수, 급식지수, 교우관계지수, 예체능지수, 현장실습지수를 공개합니다!")
plots = []
k = 0
for item in mean:
    plots.insert(k, item)
    k = k + 1
plt.plot(["Fun", "Lunchtime", "Friends?", "Arts 'n' Sports", "Work as Student"], plots, 'c')
plt.show()
