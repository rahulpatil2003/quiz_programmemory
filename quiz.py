import random

users = {}
quiz_data = {
    "C++": [
        {"q": "Which operator is used to access members of a class in C++?", "o": [".", "::", "->", ":"], "a": "."},
        {"q": "What is the purpose of a constructor in C++?", "o": ["To initialize objects", "To destroy objects", "To allocate memory", "To overload functions"], "a": "To initialize objects"},
        {"q": "Which of the following is a valid loop structure in C++?", "o": ["repeat-until", "for", "foreach", "loop-until"], "a": "for"},
        {"q": "Which access specifier allows access to class members only within the same class?", "o": ["public", "private", "protected", "default"], "a": "private"},
        {"q": "Which of these is a feature of C++?", "o": ["Encapsulation", "Garbage Collection", "Dynamic Typing", "None"], "a": "Encapsulation"}
    ],
    "Python": [
        {"q": "Which Python method can be used to convert a string to lowercase?", "o": ["lowercase()", "lower()", "downcase()", "to_lower()"], "a": "lower()"},
        {"q": "How do you start defining a function in Python?", "o": ["function name()", "def name:", "def name():", "define name():"], "a": "def name():"},
        {"q": "Which keyword is used to create a generator in Python?", "o": ["return", "yield", "gen", "create"], "a": "yield"},
        {"q": "What is the default value returned by a function that does not have a return statement?", "o": ["None", "0", "False", "Null"], "a": "None"},
        {"q": "Which of these data structures is mutable in Python?", "o": ["List", "Tuple", "String", "Set"], "a": "List"}
    ],
    "DSA": [
        {"q": "What is the best-case time complexity of quicksort?", "o": ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"], "a": "O(n log n)"},
        {"q": "Which data structure is ideal for implementing undo functionality?", "o": ["Queue", "Stack", "Heap", "Array"], "a": "Stack"},
        {"q": "What is the height of a full binary tree with 15 nodes?", "o": ["3", "4", "5", "6"], "a": "4"},
        {"q": "Which traversal technique visits nodes level by level?", "o": ["Inorder", "DFS", "BFS", "Preorder"], "a": "BFS"},
        {"q": "What is the time complexity of searching for an element in a hash table?", "o": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "a": "O(1)"}
    ]
}

def login():
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    if users.get(name) == password:
        print("Login successful!")
        return name
    print("Invalid username or password!")
    return None

def register():
    name = input("Enter username: ")
    if name in users:
        print("User already exists!")
        return False
    password = input("Enter password: ")
    users[name] = password
    print("Registration successful!")
    return True

def quiz(subject, username, quiz_data):
    print(f"\nStarting {subject} quiz!")
    score = 0
    max_questions = min(5, len(quiz_data[subject]))
    questions = random.sample(quiz_data[subject], max_questions)

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for idx, option in enumerate(q['o'], 1):
            print(f"{idx}. {option}")
        while True:
            try:
                ans = int(input("Your answer (1/2/3/4): "))
                if 1 <= ans <= len(q['o']):
                    if q['o'][ans - 1] == q['a']:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer was: {q['a']}")
                    break
                else:
                    print("Invalid choice! Please choose a valid option.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")

    print(f"\n{username}, your score is {score}/{max_questions}.")

def main():
    print("Welcome to the Quiz Application!")
    username = None

    while not username:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if register():
                continue
        elif choice == "2":
            username = login()
        elif choice == "3":
            print("Thank you!")
            return
        else:
            print("Invalid choice!")

    while True:
        print("\nSubjects:\n1. C++\n2. Python\n3. DSA")
        choice = input("Choose a subject (1-3): ")
        if choice == "1":
            quiz("C++", username, quiz_data)
        elif choice == "2":
            quiz("Python", username, quiz_data)
        elif choice == "3":
            quiz("DSA", username, quiz_data)
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue

        play_again = input("Do you want to take another quiz? (YES/NO): ").lower()
        if play_again != "yes":
            print("Thank you!")
            break

if __name__ == "__main__":
    main()
