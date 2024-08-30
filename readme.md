## Google Chat Export Parser

You can create a downloadable archive of your Google Chat history using Google Takeout. 

1. Sign in to Google Takeout (https://takeout.google.com ) with the same email you use to sign in to Google Chat

2. Deselect all Google products (there is a tick box to do that at the top of the list)

3. Select Google Chat

4. Click Next

5. Select your archive settings (the defaults are usually fine)

6. Create your archive.

7. Download and extract the archive

8. Run `python gchatparser.py <messages.json>` for whatever chat you wish to convert. ✨