import requests
import tkinter as tk

def getNews():
    api_key = "329bd053697746228e5ad0d494262032"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apikey={api_key}"
    news = requests.get(url).json()
    articles = news["articles"]
    my_articles = []
    my_news = ""
    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news += f"{i + 1}. {my_articles[i]}\n"

    # Update the label with the news
    label.config(text=my_news)

# Setting up the GUI
canvas = tk.Tk()
canvas.geometry("500x500")
canvas.title("News App")
canvas.configure(background="White")

button = tk.Button(canvas, font=24, text="Reload", bg="Black", fg="White", command=getNews)
button.pack(pady=20)

label = tk.Label(canvas, font=18, justify="left", bg="White")
label.pack(pady=20)

getNews()  # Get news when the app starts
canvas.mainloop()
