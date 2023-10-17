# numbers="Abu"
# new_numbers=[n for n in numbers]
# print(new_numbers)
# import random
# numbers=[1,2,3,4,5,6,7,8]
# listNumbers=[n for n in numbers if n%2==0]
# print(listNumbers)

# names=["Abu","Samar","Utsav","Chaudhary","Priyanshu","Dash"]
# new_names=[name.upper() for name in names if len(name)>=5]
# print(new_names)

# new_dictionary={student:random.randint(1,100) for student in names}
# print(new_dictionary)
# passed={pass_student:score for pass_student,score in new_dictionary.items() if score>50}
# print(passed)


# sentence="Hello my name is Abu Samar"
# listItems=(sentence.split())
# wordLength={
#     word:len(word) for word in listItems
# }
# print(wordLength)


# days={"Monday":12,"Tuesday":14,"Wednesday":15,"Thursday":14,"Friday":32,"Saturday":22,"Sunday":24,}
# newTemp={
#     day:(temp*9/5)+32 for day,temp in days.items()
# }
# print(newTemp)

import tkinter
window=tkinter.Tk()
window.mainloop()