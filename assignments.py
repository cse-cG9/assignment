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
# menus={
#     "subject_bipc":["zoology","biology","physics"],
#     "subject_mpc":["maths","chemistry","physics","english"],
#     "subject_cse":["noun","devops","dbms"]
# }
# print(menus["subject_bipc"])
# print(menus["subject_mpc"])
# your_subject=input("enter your subject:")
# if your_subject in menus["subject_bipc"]:
#     print(f"hey your subject {your_subject} is belongs to bipc group")
# elif your_subject in menus["subject_mpc"]:
#     print(f"hey your subject {your_subject} is belongs to mpc group")
# elif your_subject in menus["subject_cse"]:
#     print(f"hey your subject {your_subject} is belongs to cse group")
# elif your_subject==["graphics"]:
#     print(f"hey your subject {your_subject} is not belongs to bipc or mpc")
# elif your_subject==["economics"]:
#     print(f" {your_subject} is belongs to cec group")
# elif your_subject==["noun"]:
#     print(f"your subject {your_subject} is belongs to english grammar")
# elif your_subject==["social"]:
#     print(f"{your_subject} is belong to mpc group")
# elif your_subject==["sancrit"]:
#     print(f"hey your subject {your_subject} belongs to  mpc and bipc")

# else:
#  print(f"hey your subject {your_subject} is not belongs to bipc/mpc group")

#50 line code
menus=["biryani","chapathi","idly","dhosa","friedrice","upma","eggcurry"]
one_dhosa=30
one_biryani=110
one_chapathi=20
one_idly=30
one_friedrice=60
one_upma=30
one_eggcurry=50
your_order=input("entyer your order:")
if your_order in menus:
  print(f"yes!.... {your_order} is available")
  quantity=int(input(f"how many {your_order} you want:"))
  if your_order=="dhosa":
    total=one_dhosa*quantity
    print(f"your total bill is {total}")
    print("thankyou for visiting")
  elif your_order=="biryani":
    total=one_biryani*quantity
    print(f"your total bill is {total}")
    print("thankyou for visiting")
  elif your_order=="chapathi":
    total=one_chapathi*quantity
    print(f"your total bill is {total}")
    print("thankyou for visiting")
  elif your_order=="idly":
    total=one_idly*quantity
    print(f"your total bill is {total}")
    print("thankyou for visiting")
  elif your_order=="friedrice":
    total=one_friedrice*quantity
    print(f"your total bill is {total}")
    print("thankyou for visiting")
  elif your_order=="upma":
    total=one_upma*quantity
    print(f"your total bill is {total}")
    print("thankyou for visiting")
  elif your_order=="eggcurry":
    total=one_eggcurry*quantity
    print(f"your total bill is{total}")
    print("thankyou for visiting")
else:
  print(f"sorry{your_order}is not available")
  print("sir can you please select another item")

  


