from plyer import notification
import pygame
import time
import os 

pygame.init()
pygame.mixer.init()

#Set the correct file path for the audio file
audio_file = "Water_reminder\\waterdrip.mp3"

#Check if the audio file exists
if not os.path.exists(audio_file):
    raise FileNotFoundError(f"{audio_file} not found in the current directory")
else:
    pygame.mixer.music.load(audio_file) 


def drink_notification():
    try:
        #Input to specify the frequency of notifications 
        drink_time = float(input("how frequently do you want the notification to pop up (in hours): "))
        if drink_time <= 0:
            raise ValueError("Invalid input : Time must be greater than 0. ")
    except ValueError as v:
        print(f"Invalid input: {v}")
        return
    

    #Loop to show notifications at the specified interval
    while True:
        notification.notify(
        title='Water time, broo!!',
        message='Take a break and drink some water!',
        app_name='MyNotifier',
    )
        #Play the sound
        pygame.mixer.music.play()
        print(f"Notification will appear every {drink_time} hour(s)")
        time.sleep(drink_time*3600) #Converts the hour to seconds and wait

#Ensure the scripts run only if executed directly
if __name__== "__main__":
    drink_notification()