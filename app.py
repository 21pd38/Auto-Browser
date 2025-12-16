from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Test App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
        }
        .form-section {
            margin-bottom: 30px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin: 5px 0;
            border: 1px solid #ddd;
            border-radius: 3px;
        }
        button {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        #message {
            display: none;
            padding: 10px;
            margin-top: 10px;
            background: #d4edda;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h2>Demo Application</h2>
    
    <div class="form-section">
        <h3>Login</h3>
        <input type="text" id="username" placeholder="Username">
        <input type="password" id="password" placeholder="Password">
        <button id="login-btn">Login</button>
    </div>
    
    <div class="form-section">
        <h3>Send Message</h3>
        <textarea id="message-text" rows="4" placeholder="Enter your message"></textarea>
        <button id="send-btn">Send</button>
        <div id="message"></div>
    </div>

    <script>
        document.getElementById('login-btn').addEventListener('click', function() {
            const username = document.getElementById('username').value;
            if (username) {
                alert('Logged in as: ' + username);
            }
        });
        
        document.getElementById('send-btn').addEventListener('click', function() {
            const text = document.getElementById('message-text').value;
            const msgDiv = document.getElementById('message');
            if (text) {
                msgDiv.textContent = 'Message sent: ' + text;
                msgDiv.style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True, port=5000)