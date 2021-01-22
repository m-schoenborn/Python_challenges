#opening files
input_file = "input.txt"
output_file = "output.txt"
errors_file = "errors.txt"

s = 0

with open(input_file, 'r') as f_r, \
    open(errors_file, 'w') as f_e:
        for l in f_r.readlines():
            if l[:-1].isnumeric():
                s += int(l)
            else:
                f_e.write(l)

with open(errors_file, 'r') as f:
     message = f.read()

print(message)

# Question 1 : How many people are in titanic and how many survivors?
print(df['PassengerId'].count())
print(df[df['Survived'] > 0]['Survived'].count())


# Question 2 : How many that survived were female and how many that died were female?
print(df[(df['Survived'] == 1) & (df['Sex'] == 'female')]['Survived'].count())

# Question 3 : How many children were on the titanic?
print(df[df['Age'] < 19]['Age'].count())


# Question 4 : How many children died that were on the ship?
print(df[(df['Survived'] == 0) & (df['Age'] < 19)]['Survived'].count())


# Question 5 : How many people had families with them?
print(df[(df['SibSp'] == 1) & (df['Parch'] == 1)]['Survived'].count())


# Question 6 : What is the ratio of female to male?
female = df[df['Sex'] == 'female']['Survived'].count()
male = df[df['Sex'] == 'male']['Survived'].count()
print(female/ (female + male)) # percentage of females
print(male / (female + male)) # percentage of males


# Question 7 : What contributed to the survival of those who survived?

print((df[df['Survived'] == 1]['Pclass']).value_counts()) # more people from passenger class 1 and 2 survived
print((df[df['Survived'] == 1]['Sex']).value_counts()) # more females than males survived
print((df[df['Survived'] == 1]['Age']).value_counts(ascending=False)) #younger people were more likely to survive than older people
print((df[df['Survived'] == 1]['SibSp']).value_counts()) #people travelling alone were more likely to survive (not sibling or spouse)
print((df[df['Survived'] == 1]['Parch']).value_counts()) #people who were not a parent or a child were more likely to survive (not traveling as a family)
print((df[df['Survived'] == 1]['Fare']).mean()) # the average ticket price of people who survived is 48.4 --> higher ticket price means higher chance of survival
print((df[df['Survived'] == 1]['Embarked']).value_counts()) #more people survived of those embarking on Port S.
