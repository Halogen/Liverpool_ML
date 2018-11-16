Project implementing the user interface layer of SWSLHD 'Smart Healthcare: Elective Surgery'. 
Connects to Google Data Studio (via BigQuery) for core data visualisation.

This code shows uses the [Flask](http://flask.pocoo.org/) framework to 
handle user interactivity and is intended to be deployed on Google App Engine.

Before running or deploying this application, install the dependencies using:
    pip install -t lib -r requirements.txt
    
Command to run locally:

    python main.py 
    
Command to deploy to App Engine (from within the Google Cloud Shell or SDK):

    gcloud app deploy
    
    

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/m-lutze/swslhd/README.md

