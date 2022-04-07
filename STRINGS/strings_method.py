#there are 33 build in string method

# i) capatalize()
s1="hi hello"
s1=s1.capitalize()#only first letter will be capitalize 
print(s1)

# ii)center()
print("\n")
s2="hii"
s2=s2.center(9,'*')#puts string to the center according to given charecter 
print(s2)

# iii) ljust()
print("\n")
s3="hii"
s3=s3.ljust(9,'*')#puts string to the left according to given charecter
print(s3)

# iv) rjust()
print("\n")
s4="hii"
s4=s4.rjust(9,'*')#puts string to the right according to given charecter
print(s4)

# v) count()
print("\n")
s5="hii hello"
s5=s5.count("h")#used to count number of charecter or sub string present in main string
print(s5)

# vi) startwith()
print("\n")
s6="hii hello"
s6=s6.startswith("hii")#used to check wheather the string is starting with corresponding prefix or not
print(s6)

# vii) endwith()
print("\n")
s7="hii hello"
s7=s7.endswith("llo")#used to check whether the string ends with corresponding suffix or not
print(s7)

# viii) find()
print("\n")
s8="hii hello"
s8=s8.find("i")#returns index position that occurs at very first
print(s8)

# ix) rfind()
print("\n")
s9="hii hello" 
s9=s9.rfind("h")#it starts searching from end of main string
print(s9)

# x) index()
print("\n")
s10="hii hello"
s10=s10.index("i")#it also retursns index position that occurs at very first
print(s10)

# Note:- the difference between find() and index() is that in case of find() if the sub-string is 
# not present it retuns -1 but in case of index() it gives error message if sub-string is not present

# xi) rindex()
print("\n")
s11="hii hello"
s11=s11.rindex("e")#returns index position but starts its searching from end of main string
print(s11)

# xii) isalnum()
print("\n")
s12="hii"
s12=s12.isalnum()#checks for alphabet and number in string
print(s12)

# xiii) isalpha() 
print("\n")
s13="hii"
s13=s13.isalpha()#checks for alphabet in string
print(s13)

# xiv) isdigit()
print("\n")
s14="hii"
s14=s14.isdigit()#checks for digits in string
print(s14)

# xv) islower()
print("\n")
s15="hii"
s15=s15.islower()#checks whether all the charecters in string are lower case or not
print(s15)

# xvi) isupper()
print("\n")
s16="hii"
s16=s16.isupper()#checks whether all the charecters in string are upper case or not
print(s16)

# xvii) isspace()
print("\n")
s17="hii hello" 
s17=s17.isspace()#checks for space in string
print(s17)

# xviii) len()
print("\n")
s18="hii"
s18=len(s18)#returns lenght of the string
print(s18)

# xix) max()
print("\n")
s19="hii"
s19=max(s19)#returns highest ascii value charecter
print(s19)

# xx) min()
print("\n")
s20="hii"
s20=min(s20)#returns lowest ascii value charecter
print(s20)

# xxi) lower()
print("\n")
s21="HII"
s21=s21.lower()#converts all upper case charecter into lower case
print(s21)

# xxii) upper()
print("\n")
s22="hii"
s22=s22.upper()#converts all lower case charecter into upper case
print(s22)

# xxiii) zfill()
print("\n")
s23="hii"
s23=s23.zfill(9)
print(s23)

# xxiv) strip()
print("\n")
s24=" hii "
s24=s24.strip()#removes spaces from string
print(s24)

# xxv) lstrip()
print("\n")
s25="hii"
s25=s25.lstrip()#a space is added to right side
print(s25)
 
# xxvi) rstrip()
print("\n")
s26="hii"
s26=s26.rstrip()#a space is added to left side 
print(s26)

# xxvii) replace()
print("\n")
s27="hii"
s27=s27.replace("h","o")# replaces old charecter or sub-string with new one
print(s27)

# xxviii) swapcase()
print("\n")
s28="hii"
s28=s28.swapcase()#converts all lower case charecter into upper case and vice versa
print(s28)

# xxix) split()
print("\n")
s29="hii hello"
s29=s29.split(" ")#splits string into parts according to charecter given....here it is blank space
print(s29)

# xxx) join()
print("\n")
s30_1="hii"
s30_2="+"
s30=s30_2.join(s30_1)
print(s30)

# xxxi) title()
print("\n")
s31="hii hello"
s31=s31.title()#converts first letter of each charecter into upper case
print(s31)

# xxxii) istitle()
print("\n")
s32="hii hello"
s32=s32.istitle()#checks whether the string is in titled format or not
print(s32)

# xxxiii) isidentifier()
print("\n")
s33="hii"
s33=s33.isidentifier()#checks whether all charecter are identifiers(alphabet,digits,etc,.) or not 
print(s33)