from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form.get("user_text")

        if user_text.strip() == "":
            return render_template("index.html", error="Please enter some text.")

        # Perform sentiment analysis
        blob = TextBlob(user_text)
        polarity = round(blob.sentiment.polarity, 3)   # Range: -1 to +1
        subjectivity = round(blob.sentiment.subjectivity, 3)  # Range: 0 to 1

        # Determine sentiment
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return render_template("result.html",
                               text=user_text,
                               sentiment=sentiment,
                               polarity=polarity,
                               subjectivity=subjectivity)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
