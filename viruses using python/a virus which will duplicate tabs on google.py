import webbrowser,random,time
websites = ["www.google.com","www.instagram.com","www.youtube.com","www.twitter.com"]
while True:
    tabs = random.choice(websites)
    webbrowser.open(tabs , new = 1)
    time.sleep(0.5)