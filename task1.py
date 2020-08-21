import pyttsx3
import os
import webbrowser
print("!!! Welcome to my Task !!!\n")
print("!  Write exit or stop to come out  !\n")
pyttsx3.speak("What can I do for you sir?")
while True :
    get = input("What do you want MASTER:")

    if (("donot" in get) or ("dont" in get)):
          print("Sorry, we cannot process your request, Please try again!!")
          pyttsx3.speak("Sorry, we cannot process your request, dont be smart, Please try again!!")
    else:
          if (("run" in get) or ("open" in get) or ("execute" in get )) and ("chrome" in get):
            pyttsx3.speak("opening chrome browser")
            print("Opened Browser")
            os.system("chrome")

          elif (("run" in get) or ("open" in get) or ("execute" in get )) and ("browser" in get or ("firefox" in get ) or ("default" in get )):
            pyttsx3.speak("opening default browser firefox")
            print("Opened Browser")
            os.system("firefox")

          elif ("open" in get) and (("linkedin" in get) or ("profile" in get)):
            pyttsx3.speak("opening your linkedin profile")
            print("Opened Linkedin Profile")
            webbrowser.open_new_tab('https://www.linkedin.com/in/akhilesh-jain-a871531ab/')

          elif (("not in " in get) or ("i want" in get)) and (("good mood" in get) or ("listen" in get) or ("music" in get)):
            pyttsx3.speak(" i will make your mood  good sir, listen to your favorite music on youtube-music,")
            print("Opened Browser")
            webbrowser.open_new_tab('https://music.youtube.com/search?q=maroon+5')

          elif (("tell" in get)or ("who" in get)) and (("mentor" in get) or ("trainer" in get) or ("taught" in get) or ("sir" in get)):
            pyttsx3.speak("opening your mentor's linkedin profile")
            print("Opened Linkedin Profile")
            webbrowser.open_new_tab('https://www.linkedin.com/in/vimaldaga/?originalSubdomain=in')

          elif (("open" in get) or ("run" in get) or ("python" in get) or ("practice python" in get)) and (("ide" in get)):
            pyttsx3.speak("opening your i,d,e, and see your browser for your i,d,e , and start practicing python")
            print("Opened Browser")
            os.system("jupyter notebook")

          elif (("open" in get) or ("run" in get)) and (("media" in get) or ("player" in get) ):
            pyttsx3.speak("opening your Windows Media Player, but remember your playlist is empty")
            print("Opened Windows Media Player")
            os.system("wmplayer")

          elif ("exit" in get) or ("stop" in get):
            pyttsx3.speak("Exiting your task and, Have a Good Day, See you later, Bye")
            print("\nExiting...\nThanks for your Effort and Time!!!\nHave a Good Day !!!\nBYE!!!\n")
            break

          else: 
            pyttsx3.speak("Sorry for inconvenience, Please try something else")
            print("Sorry for inconvenience, Please try something else\n")
print("\nMORE OPTIONS COMING SOON, THANK YOU FOR WATCHING\n")
print("I have learned this concept in my IIEC RISE - Specialist in Python training\nunder the mentorship of VIMAL DAGA Sir")