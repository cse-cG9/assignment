'''
Mary Teresa Bojaxhiu (born Anjezë Gonxhe Bojaxhiu, Albanian: [aˈɲɛzə ˈɡɔndʒɛ bɔjaˈdʒi.u];
 26 August 1910 – 5 September 1997), better known as Mother Teresa or Saint Mother Teresa
 ,[a] was an Albanian-Indian Catholic nun, founder of cathelic
'''
# username="mary teresa"
# date=1910
# founder="catholic"
# print(username)
# print(date)
# print(founder)

'''
Mohandas Karamchand Gandhi[c] (2 October 1869 – 30 January 1948)[2] was an Indian lawyer,
 anti-colonial nationalist, and political ethicist who employed nonviolent resistance to lead the successful campaign for India's
   independence from British rule.
 He inspired movements for civil rights and freedom across the world. The h
'''
# fullname=input("enter the fullname:")
# date=int(input("enter the date:"))
# rights=input("enter the rights:")
# print(f"fullname is {fullname} and date of birth is {date} and his rights are {rights}")

#assignment-3
menus={
    "subject_bipc":["zoology","biology","physics"],
    "subject_mpc":["maths","chemistry","physics","english"],
    "subject_cse":["noun","devops","dbms"]
}
print(menus["subject_bipc"])
print(menus["subject_mpc"])
your_subject=input("enter your subject:")
if your_subject in menus["subject_bipc"]:
    print(f"hey your subject {your_subject} is belongs to bipc group")
elif your_subject in menus["subject_mpc"]:
    print(f"hey your subject {your_subject} is belongs to mpc group")
elif your_subject in menus["subject_cse"]:
    print(f"hey your subject {your_subject} is belongs to cse group")
elif your_subject==["graphics"]:
    print(f"hey your subject {your_subject} is not belongs to bipc or mpc")
elif your_subject==["economics"]:
    print(f" {your_subject} is belongs to cec group")
elif your_subject==["noun"]:
    print(f"your subject {your_subject} is belongs to english grammar")
elif your_subject==["social"]:
    print(f"{your_subject} is belong to mpc group")
elif your_subject==["sancrit"]:
    print(f"hey your subject {your_subject} belongs to  mpc and bipc")

else:
 print(f"hey your subject {your_subject} is not belongs to bipc/mpc group")
