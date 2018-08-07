from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	player = ["Aya aka greatest sport player", "Your mom", "Eilon", "Shiraz"]
	likes_same_sport=True
	return render_template("index.html",
	player=player,
	likes_same_sport=likes_same_sport
	
	)

if __name__ == '__main__':
	app.run(debug = True)
