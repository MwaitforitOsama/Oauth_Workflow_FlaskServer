from flask import Flask, redirect, request, render_template,jsonify
import requests

app = Flask(__name__)

CLIENT_ID = "O3rIybaWYTNkqrYGbZMMsCgypBaaWjQ14z3odCLbSEc"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "https://89cc-39-42-138-20.ngrok-free.app/receive"  # Remove leading/trailing spaces


def get_auth_url():
    auth_url = "https://api.gomotive.com/oauth/authorize"
    scope = "companies.read"
    return f"{auth_url}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={scope}"

@app.route('/receive2')
def exchange_code_for_token():
    url = 'https://api.gomotive.com/oauth/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': "m8U24S8t9dmboLazJgmcOb4sNVa6GU-wAqHi5NLm5g8",
        'redirect_uri': "https://89cc-39-42-138-20.ngrok-free.app",
        'client_id': "O3rIybaWYTNkqrYGbZMMsCgypBaaWjQ14z3odCLbSEc",
        'client_secret': "bQGkPHbKT1Eg4FY8fqQhz1_gGMHra1o-CFCDHmZ9r_Q"
    }

    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    # You can do further processing with the JSON data if needed
    return jsonify(json_data)


@app.route('/hit_url')
def hit_url_endpoint():
    url_to_hit = get_auth_url()
    return url_to_hit


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/receive', methods=['GET', 'POST'])
def receive_json():
    if request.method == 'GET':
        return render_template('receive.html')
    elif request.method == 'POST':
        try:
            # Get JSON data from the request
            json_data = request.get_json()
            print(json_data)
            return jsonify({"received_data": json_data}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
