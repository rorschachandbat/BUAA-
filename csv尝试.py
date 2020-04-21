a=['1','2','3']
b=['4','5','6']
c=['7','8','9']

import csv
with open('try.csv','a',newline='')as f:
    w=csv.writer(f)
    w.writerow(['a','b','c'])
    for i in range(3):
        w.writerow([a[i],b[i],c[i]])
