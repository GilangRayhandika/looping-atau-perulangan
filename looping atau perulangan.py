#!/usr/bin/env python
# coding: utf-8

# In[2]:


# for in range
# print 1 - 10

for i in range(1,11):
    print(i)
    
    
    
    


# In[4]:


#print 10 20 30 40 50 --- 100

for i in range (1,11):
    print(i*10)


# In[5]:


for i in range(10,110,10):
    print(i)


# In[6]:


for i in range(10,0,-1):
    print(i)


# In[7]:


# 10 9 8 7

for i in range(10,0,-1):
    print(i)


# In[15]:


# 1 -2 3 -4 5 -6 7 -8 9 -10
sign = 1
for i in range(1,11):
    print(i* sign)
    sign *=-1
   


# In[21]:


# faktorial => linput 4! = 4 * 3 * 2 * 1 =24

number = int(input('isikan bilangan:'))
pangkat = int(input('isikan pangkat:'))

result = 1
for i in range(1, number+1):
    result = result * pangkat
    
print(f"faktorial dari {number}! adalah {result}")
    


# In[23]:


number = int(input('isikan bilangan:'))
pangkat = int(input('isikan pangkat:'))

result = 1
for i in range(1, pangkat+1):
    result = result * pangkat
    
print(f"{number} pangkat {pangkat} adalah {result}")

    


# In[30]:


# cek bilangan prima
# bilangan prima adalah bilangan yang hanya bisa dibagi dengan bilangan itu 
# sendiri dan 1  

#Bill. Prima punya 2 faktor  

#jika number % i == 0 maka nilai faktor  di increment(=1)
#setelah selesai perulangan, jika faktor == 2 maka bilangan prima
number = int(input('isikan bilangan:'))
faktor = 0 
for i in range(1,number+1): 
    sisa = number % 1 
    if number % i == 0:
        faktor = faktor+1


if faktor == 2:
    print(f"{number} bilangan prima")
else: 
    print(f"{number} adalah bukan bilangan prima")

    
    
    
    


# In[36]:


kampus = "universitas nusa putra" # panjang = 22
print(len(kampus))
print(kampus[0])
for i, huruf in enumerate (kampus):
    print(i,huruf)


# In[47]:


#menghitung jumlah huruf vokal 
#panjang 22

kampus = "universitas nusa putra"  
panjang = len(kampus)

vokal_a=0
vokal_i=0
vokal_u=0
vokal_e=0
vokal_o=0
for i in range(0,panjang):
    if kampus[i]=='a' or kampus[i]=='A':
        vokal_a +=1
    elif kampus[i]=='i' or kampus[i]=='I':
        vokal_i +=1
    elif kampus[i]=='u' or kampus[i]=='U': 
        vokal_u +=1
    elif kampus[i]=='e' or kampus[i]=='E':
        vokal_e +=1
    elif kampus[i]=='o' or kampus[i]=='O':    
        vokal_o +=1
        
print(f"jumlah huruf vokal a:{vokal_a}")
print(f"jumlah huruf vokal i:{vokal_i}")
print(f"jumlah huruf vokal u:{vokal_u}")
print(f"jumlah huruf vokal e:{vokal_e}")
print(f"jumlah huruf vokal o:{vokal_o}")
jumlah_vokal = vokal_a + vokal_i + vokal_u + vokal_e + vokal_o
print(f"jumlah huruf vokal keseluruhan: {jumlah_vokal}")









# In[1]:


ulang = "y"
while ( ulang=="y"):
    kalimat = input("isikan kalimat")
    panjang_kalimat =len(kalimat)

#aku => uka
#mengecek kalimat polindrome
#polindrome =. kalimat yang dibaca dari kiri > kanan dan
#kanan > kekiri
#katak => palindrome
#kasur rusak => palindrome
    ispalindrome = True
    for i in range(0,panjang_kalimat):
        urut = kalimat[i]
        kebalikan = kalimat [panjang_kalimat - i-1 ]
        if urut != kebalikan:
            ispalindrome = False
            break
    if ispalindrome==True:
        print(f"{kalimat} adalah palindrome")
    else :
        print(f"{kalimat} bukan palindrome")
    ulang = input('apakah mau mengulang program?: Y/N')
    


# In[2]:


#nested for

for i in range(1,5):
    for j in range(1,5):
        print(f"i {i} dan j :{j}")


# In[ ]:




