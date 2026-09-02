from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Kastro Python Application</title>
        </head>

        <body>
            <h1>Hello from Kastro Python Application!</h1>

            <h2>Application Information</h2>

            <ul>
                <li>Language: Python</li>
                <li>Framework: Flask</li>
                <li>Container: Docker</li>
                <li>CI/CD: GitHub Actions</li>
                <li>Runner: Self-hosted</li>
            </ul>

            <p>Application deployed successfully.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "kastro-python-app"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
