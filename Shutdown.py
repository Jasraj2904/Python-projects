import os

def shutdown(confirm):
    if confirm.lower() == "yes":
        print("The system is shutting down...")
       # For Windows
        os.system("shutdown /s /t 1")
        
        # For Linux / Mac
        # os.system("sudo shutdown now")
    else:
        print("Shutdown cancelled.")
        
shutdown("yes")
shutdown("no")