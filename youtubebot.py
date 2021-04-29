import webbrowser,time
url=input("enter url of the video")
duration= input("enter duration :")
for i in range (10):
    webbrowser.open_new(url)
    time.sleep(int(duration))