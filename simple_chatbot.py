

import datetime

user_info = {
    "name": "Anuj Kumar Thakur",
    "dob": "2007-06-01",
    "age": datetime.datetime.now().year - int("2007-06-01".split('-')[0]),
    "plus_2_collage": "Prasadi Academy",
    "lower_secondary_school": "shree Laxmi Basic School",
    "district": "Sarlahi",
    "birth_city": "malangwa",  
    "father_name": "ram Thakur",
    "mother_name": "sita Thakur",
    "total_siblings": 3,
    "elder_siblings": "Sunil Thakur",
    "younger_siblings": "Ankit Thakur",
    "total_family_members": 5,  
    "country": "Nepal",
    "greet": "Namaste",
    "farewell": "Thank you for using the chatbot. Goodbye!"
}



print(f'Welcome {user_info["name"]} to the your personal chatbot')
print('='*100)
question_map = {
    "name": "name",
    "your name": "name",
    "age": "age",
    'old': 'age',
    "your age": "age",
    "dob": "dob",
    "date of birth": "dob",
    "school": "lower_secondary_school",
    "collage": "plus_2_collage",
    "district": "district",
    "birth city": "birth_city",
    "father name": "father_name",
    "mother name": "mother_name",
    "siblings": "total_siblings",
    "elder sibling": "elder_siblings",
    "younger sibling": "younger_siblings",
    "family members": "total_family_members",
    "country": "country"
}
while True:
    query = input("Ask something: ").strip().lower()
    for key in question_map:
        if key in query:
            print(user_info[question_map[key]])
            break
    else:
        print("Sorry, I don't understand that.")
