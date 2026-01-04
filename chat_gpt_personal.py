while True:
    query = input('Ask your query: ').strip().lower()
    if query == 'exit' or query == 'quit':
        print('See to you later buddy!, Have a great time ahead......')
        break
    elif query == 'your name' or  'name' in query:
        print('My name is Anuj and I am a personl chatbot created to assist you. If you have any queries about anuj please ask me....')
    elif query == 'your age' in query or 'age' in query or query == 'old' in query:
        print(f'Anuj is 20 years old')
    elif query == 'your dob' in query or 'date of birth' in query or query == 'dob' in query:
        print('Anuj was born on 1st June 2007')
    elif query == 'your school' in query or  'school' in query:
        print('Anuj completed his lower secondary education from shree Laxmi Basic School')
    elif query == 'your collage' in query or 'collage' in query:
        print('Anuj is currently studying in Prasadi Academy for his +2 education')
    elif query == 'your district' in query or 'district' in query:
        print('Anuj belongs to Sarlahi district of Nepal')
    elif query == 'your birth city' or 'birth city' in query:
        print('Anuj was born in malangwa')
    elif query == 'your father name' in query or 'father name' in query:
        print('Anuj\'s father name is ram Thakur')
    elif query == 'your mother name' in query or 'mother name' in query:
        print('Anuj\'s mother name is sita Thakur')
    elif query == 'your siblings' in query or 'siblings' in query:
        print('Ankit elder brother and pappu younger brother, Anuj has total 3 siblings')
    elif query == 'your elder sibling' in query or 'elder sibling' in query:
        print('Anuj\'s elder sibling is Sunil Thakur')
    elif query == 'your younger sibling' in query or 'younger sibling' in query:
        print('Anuj\'s younger sibling is Ankit Thakur')
    elif query == 'your family members' in query or 'family members' in query:
        print('Anuj has total 5 family members including himself')
    elif query == 'your country' in query or 'country' in query:
        print('Anuj is from Nepal')
    else:
        print('Sorry, I don\'t understand that.')        
        
    