# Parfume_Prices_Tracker
This is a simple application designed to retrieve and store prices and data of men's fragrances from the most popular beauty retailer websites. The application scrapes individual web pages to extract information such as product names, capacities, and other relevant data.

---
# Table of contents
1. [How it works](#how-it-works)
2. [Example Input/Output](#example-inputoutput)
3. [Libraries Used](#libraries-used)
4. [Getting Started](#getting-started)
5. [Automating the process](#automating-the-process)
6. [TODO](#todo)
---
## How it works
First you need to create an Excel, where you want store of the collected data. Then the only thing you have to do is going the website of your favourite product and copy the link. After pasting it to the correct place in the app you just need to push the button.

![Basic app view](Images/Zrzut%20ekranu%202023-05-26%20125647.png)

![Pasting the links](Images/Zrzut%20ekranu%202023-05-26%20130127.png)
![Wrong links](Images/Zrzut%20ekranu%202023-05-26%20130600.png)
![GREEN=OK RED=WRONG LNK](Images/Zrzut%20ekranu%202023-05-26%20130631.png)

---

## Example Input/Output
![Input](Images/Zrzut%20ekranu%202023-05-26%20142524.png)
![Output](Images/Zrzut%20ekranu%202023-05-26%20142737.png)


---
## Libraries Used
- Kivy
- Openpyxl
- BeautifulSoup4

---
## Getting Started
* be aware some websites could change their html so might not work anymore
* you can start collecting your data as soon as you start the app
* requires installating additional libraries mentioned above

---
## Automating the process
There are many different ways you can automate collecting the data. Two most obvious one's are:
* you can prepare a script in Linux to exec one of the site-getters files every day or every hour for example
* you can add some variation of the following code:
```python

    def on_start(self):
        threading.Thread(target=self.schedule_task).start()

    def schedule_task(self):
        now = datetime.datetime.now()
        target_time = datetime.datetime(now.year, now.month, now.day, 20, 0, 0)
        if now > target_time:
            target_time += datetime.timedelta(days=1)
        time_delta = target_time - now
        seconds = time_delta.total_seconds()
        threading.Timer(seconds, self.run_task).start()

    def run_task(self):
        # Here you can place which data getter you want to use
        print("I am automatically data collecting")

```

---
## TODO
* add more websites
* also I am preparing a version of the app that will be colecting data automatically, you will just need to paste a link or a screenshot with your fragrance. It will be pusblished soon
* add fmale fragrance handling

---
