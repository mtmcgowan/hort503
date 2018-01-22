from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# Study Drills
# 1. Find out what the games Zork and Adventure were. Try to find a copy and play it.
# Bummer, I got eaten by a Grue....

# 2. Change the prompt variable to something else entirely.
prompt = 'Please input stuff: '
print("Are you lying to me {user_name}?")
computer = input(prompt)

# 3. Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.
# Ok

# 4. Make sure you understand how I combined........
# Ok, I understand