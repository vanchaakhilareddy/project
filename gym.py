#!/usr/bin/env python
# coding: utf-8

# In[1]:


regimens_dict = {'regimen1' : {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Rest','Thu': 'Back','Fri': 'Triceps','Sat': 'Rest','Sun': 'Rest'}, 'regimen2': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio/Abs','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Rest'}, 'regimen3': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Abs/Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Cardio'}, 'regimen4': {'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'Cardio','Sun': 'Cardio'}}
member_details_dict = {}

class SuperUser:
    try:
        global member_details_dict
        global regimens_dict


        def __init__(self):
            self.superuser_menu()
            pass



        def superuser_menu(self):
            print("Here are your options, SuperUser! \n 1. Create Member\n 2. View Member\n 3. Delete Member            \n 4. Update Member\n 5. Create Regimen\n 6. View Regimen\n 7. Delete Regimen            \n 8. Update Regimen\n 9. Exit")
            i = int(input("Please enter your choice\n"))
            while(i not in range(1,9)):
                if i == 9:
                    login()
                    break
                else:
                    print("Please enter a valid option!\n")
                    i = int(input("Please enter your choice, and make sure it's between 1 to 10\n"))
            else:     
                if i == 1:
                    self.create_member()
                    self.superuser_menu()
                elif i == 2:
                    self.view_member()
                    self.superuser_menu()
                elif i == 3:
                    self.delete_member(input("Please enter contact number of the Member to be deleted!\n"))
                    self.superuser_menu()
                elif i == 4:
                    self.update_member()
                    self.superuser_menu()
                elif i == 5:
                    self.create_regimen()
                    self.superuser_menu() 
                elif i == 6:
                    self.view_regimen()
                    self.superuser_menu()
                elif i == 7:
                    self.delete_regimen()
                    self.superuser_menu()
                elif i == 8:
                    self.update_regimen()
                    self.superuser_menu()

        def create_member(self):
            print("Okay superuser, let's create a new member!\n")
            num = input("Please enter the contact number to check if member does not exist!\n")
            while num in member_details_dict:
                print("Sorry it seems like the member already exists, would you like to update this instead?\n")
                break
            else:
                member_details_dict[num] = {}
                print("Okay seems like the member doesn't exist. Enter the details!\n")
                full_name = input("Please enter Full Name of Member!\n")
                member_details_dict[num]["Full Name"] = full_name

                age = input("Please enter Age of Member!\n")
                while(age.isdigit() == False):
                    age = input("Age has to be a number value!\n")
                member_details_dict[num]["Age"] = age

                gender = input("Please enter Gender of Member!['Male'/'MALE'/'M'/'m'/'Female'/'FEMALE'/'f'/'F'/'Others']\n")
                while(gender not in ['Male','MALE','M','m','Female','FEMALE','f','F','Others']):
                    gender = input("Please enter a valid gender('Male', 'Female' or 'Others')!")
                member_details_dict[num]["Gender"] = gender

                member_details_dict[num]["Contact Number"] = num

                email = input("Please enter Email ID of Member!\n")
                member_details_dict[num]["Email ID"] = email

                bmi = float(input("Please enter bmi of Member![0 to 35]\n"))
                while(isinstance(bmi, float) == False):
                    bmi = float(input("Please enter a correct value for bmi of Member!\n"))
                member_details_dict[num]["bmi"] = bmi

                duration = int(input("Please enter Membership Duration in months!(1/3/6/12)\n"))
                while duration not in [1,3,6,12]:
                    duration = int(input("Please enter Correct Membership Duration in months! (1,3,6,12)\n"))
                member_details_dict[num]["Membership Duration"] = duration

                member_details_dict[num]["Workout Regimen"] = self.select_regimen(bmi)

            print("Lets go back to the Main Menu!\n\n") 


        def select_regimen(self, bmi):
            while(isinstance(bmi,float) == False):
                print("Sorry, Bmi entered is not a correct value!\n")
                break
            else:
                if(bmi < 18.5):
                    regimen = regimens_dict['regimen1']
                elif(bmi >= 18.5 and bmi < 25):
                    regimen = regimens_dict['regimen2']
                elif(bmi >= 25 and bmi < 30):
                    regimen = regimens_dict['regimen3']
                elif(bmi >= 30 and bmi < 35):   
                    regimen = regimens_dict['regimen4']

                return regimen

        def view_member(self):
            check = input("Please enter the Contact Number of the Member!\n")
            if check in member_details_dict:
                print("The Details for Member are: ")
                for detail in member_details_dict[check]:
                    if type(member_details_dict[check][detail]) != dict:
                        print('{} : {}'.format(detail, member_details_dict[check][detail]))
                    else:
                        print(detail + ":")
                        for j in member_details_dict[check][detail]:
                            print('{} : {}'.format(j, member_details_dict[check][detail][j]))
            else: 
                print("Sorry, it seems the Member doesn't exist!\n")

            print("Lets go back to the Main Menu!\n\n") 

        def delete_member(self, num):
            if num in member_details_dict:
                del member_details_dict[num]
            else:
                print("The member doesn't exist\n")
            print("Lets go back to the Main Menu!\n\n") 

        def update_member(self):
            check = input("Please enter the Contact Number of the Member!\n")
            if check in member_details_dict:
                print('Here are the details!')
                label = 1
                for i in member_details_dict[check]:
                    print('{}. {}'.format(label, i))
                    label += 1
                val = input("Please enter the name of the detail you wish to update\n")
                while(val not in member_details_dict[check]):
                    print("This detail is not present for this member!\n\n")
                    break
                else:
                    if val == "Membership Duration":
                        print("Choose either extend or revoke membership!")
                        n = int(input("1. Extend membership by 3 months\n2. Revoke Membership\n"))
                        while(n not in range(1,3)):
                            n = int(input("Please enter a valid value(Either 1 or 2)"))
                        else:
                            if n == 1:
                                member_details_dict[check]["Membership Duration"] += 3
                                print('Congrats! The Membership Duration is now ', member_details_dict[check]["Membership Duration"])
                            elif n == 2:
                                self.delete_member(check)
                                print('Member has been deleted!')
                    elif val == 'Workout Regimen':
                        member_details_dict[check]['Workout Regimen'] = self.update_regimen(regimen = input('Please enter the name of the regimen you would like!')) 
                        print("You have updated the regimen to")
                        for i in member_details_dict[check]['Workout Regimen']:
                            print('{}: {}'.format(i, member_details_dict[check]['Workout Regimen'][i]))
                    else:
                        member_details_dict[check][val] = input("Please enter the updated value\n")
                        print("Great! The value of {} has been updated to {}\n\n".format(val,member_details_dict[check][val]))

            print("Lets go back to the Main Menu!\n\n")

        def create_regimen(self):
            plain_regimen = {'Mon': '', 'Tue': '', 'Wed': '', 'Thu': '', 'Fri': '', 'Sat': '', 'Sun': ''}
            print("Okay lets create a new regimen!")
            regimen_name = input('Please give a name to the new regimen!\n')
            while(regimen_name in regimens_dict):
                print("Sorry the regimen already exists! Please enter a different name!")
                regimen_name = input('Please give a name to the new regimen!\n')
            else:
                regimens_dict[regimen_name] = plain_regimen
                for i in regimens_dict[regimen_name]:
                    print("Enter workout for {}!".format(i))
                    regimens_dict[regimen_name][i] = input()
                print('Workout for {} Regimen is:'.format(regimen_name))
                for i in regimens_dict[regimen_name]:
                    print('{}: {}'.format(i, regimens_dict[regimen_name][i]))
            print("Lets go back to the Main Menu!\n\n")

        def view_regimen(self):
            print('Please choose an option! \n1. View all available regimens\n2. Enter name of regimen to view')
            i = int(input())
            while(i not in range(1,3)):
                print("Please choose a valid option!(Either 1 or 2)")
                i = int(input())
            else:
                if i == 1:
                    for j in regimens_dict:
                        print(j)
                    reg_name = input("Please enter name of regimen you would like to see!\n")
                    if reg_name in regimens_dict:
                        print('Workout for {} Regimen is:'.format(reg_name))
                        for reg in regimens_dict[reg_name]:
                            print('{}: {}'.format(reg, regimens_dict[reg_name][reg]))
                    else:
                        print("Incorrect Regimen Name entered!")
                else:
                    reg_name = input("Please enter name of regimen you would like to see!\n")
                    if reg_name in regimens_dict:
                        print('Workout for {} Regimen is:'.format(reg_name))
                        for reg in regimens_dict[reg_name]:
                            print('{}: {}'.format(reg, regimens_dict[reg_name][reg]))
                    else:
                        print("Incorrect Regimen Name entered!")

            print("Lets go back to the Main Menu!\n\n") 

        def delete_regimen(self):
            regimen = input("Please enter the name of the regimen you would like to delete!")
            if regimen in regimens_dict:
                del regimens_dict[regimen]
            else:
                print("Seems like the regimen you are looking for already doesn't exist!")

        def update_regimen(self, regimen = 0):
            if regimen == 0:
                print('Select a regimen to update!')

                for j in regimens_dict:
                    print(j)
                reg_name = input("Please enter name of regimen you would like to see!\n")
                if reg_name in regimens_dict:
                    print('Update Workout for {} Regimen:'.format(reg_name))
                    for reg in regimens_dict[reg_name]:
                        regimens_dict[reg_name][reg] = input("Update for {}:\n".format(reg))
                    print('Updated Regimen is:')
                    for reg in regimens_dict[reg_name]:
                        print('{}: {}'.format(reg, regimens_dict[reg_name][reg]))
            elif regimen != 0:
                if regimen in regimens_dict:
                    return regimens_dict[regimen]

            else:
                print("Incorrect Regimen Name entered!")
    except:
        print("You must have entered an incorrect value!")
        
class Member:
    def __init__(self):
        self.num = input("Please enter contact number.")
        if self.num in member_details_dict:
            print("Welcome, {} to Akhila's gym!".format(member_details_dict[self.num]['Full Name']))
            self.member_menu()
        else:
            print("Sorry it seems, you are not a member!\n Please ask the super user to add your details!")
    
    def member_menu(self):
        try:
            print("Please choose one of the following options!\n1. My Regimen\n2. My Profile\n3. Exit Menu.")
            i = int(input())
            while(i not in range(1,3)):
                if i == 3:
                    login()
                    break
                i = int(input("Please enter a valid value!(Either 1 or 2)"))
            else:
                if i == 1:
                    self.member_regimen()
                    self.member_menu()
                elif i ==2:
                    self.member_profile()
                    self.member_menu()
        except:
            print("Please enter a valid value!")

    def member_regimen(self):
        print("Your Workout Regimen is:")
        for i in member_details_dict[self.num]['Workout Regimen']:
            print('{}: {}'.format(i, member_details_dict[self.num]['Workout Regimen'][i]))
            
    def member_profile(self):
        print('Your Complete Profile is:')
        for i in member_details_dict[self.num]:
            if i != 'Workout Regimen':
                print("{}: {}".format(i, member_details_dict[self.num][i]))
            else:
                self.member_regimen()




def login():

    print("------Welcome to Akhila's Gym!------")
    i = int(input("Please enter one of the following!\n1. Superuser\n2. Member\n3. Exit\n"))
    while(i not in range(1,3)):
        if i == 3:
            break
        i = int(input("Please enter a valid value!(Either 1 or 2)\n"))
    else:
        if i == 1:
            obj = SuperUser()
        else:
            obj = Member()

login()


# In[ ]:




