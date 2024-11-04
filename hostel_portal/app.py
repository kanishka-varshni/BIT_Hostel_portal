from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the BIT Hostel Portal!"

if __name__ == '__main__':
    app.run(port=5050)
    print("Running on port 5050...")
