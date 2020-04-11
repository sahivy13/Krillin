from datetime import date, timedelta, datetime
import os
import numpy as np

# start = datetime(2019, 8, 20)
# end = datetime(2019, 12, 31)

# start = datetime(2020, 1, 1)
# end = datetime(2020,2, 12)

# start = datetime(2020, 1, 1)
# end = datetime(2020, 3, 7)

start = datetime(2020, 2, 23)
end = datetime(2020, 4, 10)


delta = end - start

days = [start + timedelta(days = i) for i in range(delta.days + 1)]

#---------

# ORIGINAL

list_of_days = ['Monday', 'Tuesday']

t_t_s_d = [d for i, d in enumerate(days) if days[i].strftime('%A') in ['Tuesday', 'Thursday','Saturday', 'Sunday']] # 

# # RANDOM VALUE

# import random 

# t_t_s_d = []    
# for i in range(int(len(days)/5)):
#     t_t_s_d.append(random.choice(days))

# # OTHER DAYS RANDOM    

# import random

# new_list = [d for i, d in enumerate(days) if days[i].strftime('%A') in ['Monday', 'Wednesday','Fridays']] # 
# t_t_s_d = [] 
# for i in range(int(len(new_list)/3)):
#     t_t_s_d.append(random.choice(new_list))

# ------------

days_list = [dt.day for dt in t_t_s_d]
months_list = list(set([dt.month for dt in t_t_s_d]))
years_list = list(np.unique([dt.year for dt in t_t_s_d]))

#--------------

# ORIGINAL

list_in = [0] #index list of days_list of breaks

for i, num in enumerate(days_list):
    try:
        if days_list[i]>days_list[i+1]:
            list_in.append(i+1)
    except:
        continue

# # RANDOM CHOICE VERSION

# list_in = [0] #index list of days_list of breaks

# step = int(len(days_list)/len(months_list))

# for i in range(1,len(months_list)):
#     list_in.append(i*step)

#--------
        
list_of_list_in = [] #list of list of days per month  

for i, ind in enumerate(list_in):
    
    if i == 0:
        list_ = days_list[ind : list_in[i+1]]
        if len(list_) != 0:
            list_of_list_in.append(list_)
    else:
        try:
            list_ = days_list[ind: list_in[i+1]]
            if len(list_) != 0:
                list_of_list_in.append(list_)
        except:
            list_ = days_list[ind :]
            if len(list_) != 0:
                list_of_list_in.append(list_)

charge = [] #LIST OF MOVES DONE PER ATTACK
for i in range(1):
    flare = f"0{i+1}"
    charge.append(flare)

list_m = []

for i in list(np.unique(months_list)):
    if i <= 9:
        month = f"0{i}"
        list_m.append(month)
    else:
        month = f"{i}"
        list_m.append(month)

def list_d_maker(z):
    list_ = []
    for j in list_of_list_in[z]:
#         print(j)
        if j <= 9:
            day = f"0{j}"
            list_.append(day)
        else:
            day = f"{j}"
            list_.append(day)
    return list_

Y=str(years_list[0])

for z, M in enumerate(list_m):

    list_d = list_d_maker(z)
    
    for D in list_d:

        for i in charge:

            os.system(f'echo "{i} on {M}/{D}/{Y}" > commit.md') # echo "$i on $M/$D/$Y" > commit.md
            os.system(f'export GIT_COMMITTER_DATE="{Y}-{M}-{D} 12:{i}:00"') #export GIT_COMMITTER_DATE="$Y-$M-$D 12:$i:00"
            os.system(f'export GIT_AUTHOR_DATE="{Y}-{M}-{D} 12:{i}:00"') #export GIT_AUTHOR_DATE="$Y-$M-$D 12:$i:00"
            os.system(f'git add commit.md -f') #git add commit.md -f
            os.system(f'git commit --date="{Y}-{M}-{D} 12:0{i}:00" -m "{i} on {M} {D} {Y}"') #git commit --date="$Y-$M-$D 12:0$i:00" -m "$i on $M $D $Y"
                    

# notebooks = [file for file in os.listdir('./') if file.endswith(".ipynb")]

# filename = 'solar_flare.py'

# os.system(f"touch {filename}") #Create file

# f = open(filename, "a") #tell what level of permision with second argument ("a" for example)
# f.write("#Solar Flare!!!")
# f.write("#**Runs Away**")
# f.close()

# last_access = os.stat('solar_flare.py').st_atime

# os.utime(filename, (last_access, t_t_s_d[0].timestamp())) #(path_to_file, (access_time, modification_time)

# os.system(f"rm {filename}")
