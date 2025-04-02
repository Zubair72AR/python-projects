def age_friend():
    anton_age: int = 21  # Anton is 21 years old.
    beth_age: int = 6 + anton_age  # Beth is 6 years older than Anton.
    chen_age: int = 20 + beth_age  # Chen is 20 years older than Beth.
    # Drew is as old as Chen's age plus Anton's age.
    drew_age: int = anton_age + chen_age
    ethan_age: int = chen_age  # Ethan is the same age as Chen.

    # Print out all of the ages!
    print("Anton is " + str(anton_age))
    print("Beth is " + str(beth_age))
    print("Chen is " + str(chen_age))
    print("Drew is " + str(drew_age))
    print("Ethan is " + str(ethan_age))


if __name__ == '__main__':
    age_friend()
