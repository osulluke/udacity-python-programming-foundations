import webbrowser, time

print("The program started at "+time.ctime())
for x in range(0,3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("The program ended at "+time.ctime())
