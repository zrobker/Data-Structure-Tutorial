def intersection(company1, company2):

    # creates new set
    bonus_email = set()
    for item in company1:
        # checks if each item in company1 is also in company2
        if item in company2:
            # if true, adds item to new set
            bonus_email.add(item)
    return bonus_email

def union(company1, company2):
    #this function takes advantage of the fact sets cannont have duplicate data
    for item in company2:
        company1.add(item)
    return company1


company1 = {1,9,3,4}
company2 = {8,9,10}
print(intersection(company1,company2))  # output {9}
print(union(company1,company2)) # output {1, 3, 4, 8, 9, 10}

company1 = {"email@gmail.com","email@yahoo.com","email@hotmail.com","email@outlook.com","email@university.com"}
company2 = {"email@gmail.com","name@yahoo.com","name@hotmail.com","name@outlook.com","email@university.com"}
print(intersection(company1,company2))  # output {'email@gmail.com', 'email@university.com'}
print(union(company1,company2)) # output {'name@outlook.com', 'name@hotmail.com', 'name@yahoo.com', 'email@hotmail.com',
                                #'email@university.com', 'email@yahoo.com', 'email@gmail.com', 'email@outlook.com'}