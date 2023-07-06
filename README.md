# Octopus electricity agile cost check

Background: Checking electricity prices every day is annoying

Aims: Auto-check your daily agile plan price and send all prices to a WhatsApp group or person

Step 1: Go to https://octopus.energy/dashboard/new/accounts/personal-details/api-access
        Under the Authentication section, Copy your API key

Step 2: Run setup.py
        1. Enter your API key 
        2. Enter WhatsApp contact or group id
          i. Contact [country code + phone number]: E.g. +1 xxxxxxxxx
          ii. Group id (check remarks if you can't find your group id)

Step 3: (Optional) 
        Set up schedule task for automation
        Mac
        

Remarks:
1. How to find Group id: Go to Whatsapp -> Group info -> capture your share link suffix
   E.g. https://chat.whatsapp.com/abcdefghijkl, abcdefghijkl is your group id
