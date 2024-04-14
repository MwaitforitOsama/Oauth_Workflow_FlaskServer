from flask import Flask, redirect, request, render_template,jsonify
import requests

app = Flask(__name__)

CLIENT_ID = "O3rIybaWYTNkqrYGbZMMsCgypBaaWjQ14z3odCLbSEc"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "https://43e8-39-42-138-20.ngrok-free.app/receive"  #Your NGROK URL HERE


def get_auth_url():
    auth_url = "https://api.gomotive.com/oauth/authorize"
    scope = "companies.read users.read users.manage vehicles.read vehicles.manage"
    return f"{auth_url}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={scope}"

@app.route('/hit_url')
def hit_url_endpoint():
    url_to_hit = get_auth_url()

    return url_to_hit


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/receive')
def receive_json():
    if request.method == 'POST' or 'GET':
        print(request.json())
        try:
            # Get JSON data from the request
            json_data = request.get_json()
            return jsonify({"received_data": json_data}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

# @app.route('/hit_url')
# def hit_url_endpoint():
#     url_to_hit = get_auth_url()
#     print(url_to_hit)
#     return redirect(url_to_hit)

# @app.route('/callback')
# def oauth_callback():
#     code = request.args.get('code')  # Extract the authorization code from the URL parameters

#     access_token = exchange_code_for_token(code)

#     if access_token:
#         return f"Authentication successful! Access Token: {access_token}"
#     else:
#         return "Authentication failed. Unable to obtain access token."

if __name__ == '__main__':
    app.run(debug=True)
