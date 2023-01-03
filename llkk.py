#Coding : utf-8

#Code by: MR Baloch

#Github : Baloch 

import random

import imp

from time import sleep

# List of user agents to choose from

USER_AGENTS = [

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',

    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',

    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',

    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',

]

logo =("""\033[1;92m

    #                                  

   # #    ####  ###### #    # #####    

  #   #  #    # #      ##   #   #      

 #     # #  \033[1;97m    #####  # #  #   #      

 ####### #  ### #  \033[1;93m    #  # #   #      

 #     # #    # #      #   ##   #      

 #     #  ####  ###### #    #   #      

                                       

""")

def generate_user_agent(num_user_agents):

    # Generate a list of random user agents

    user_agents = []

    

    for i in range(num_user_agents):

        user_agent = random.choice(USER_AGENTS)

        user_agents.append(user_agent)

    return user_agents

# Get the number of user agents to generate from the user

print(logo)

print(25*'-',25*'=')

num_user_agents = int(input('\n\033[1;97mEnter the number of user agents to generate: '))

for x in range(1,11):

    for i in ("\033[1;32m⠻", "\033[1;33m⠽", "\033[1;37m⠾", "⠷", "⠯", "⠟"):

        sleep(0.1)

        if x == 10:

            print('(Done ;) ' , end='')

            break

        else:

            print('Loading wait bro  ' +i, end = '\r')

# Generate the user agents

user_agents = generate_user_agent(num_user_agents)

# Print the user agents

for user_agent in user_agents:

    print(user_agent,'\n\t')

    # Open a file in write mode

f = open("/sdcard/ua.txt", "w")

for _ in range(num_user_agents):

	f.write(f"{user_agents}\n")

# Close the file

f.close()

print("\033[1;32myour file save on /sdcard/ua.txt")
