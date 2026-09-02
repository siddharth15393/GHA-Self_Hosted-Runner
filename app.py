from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Kastro DevOps Application</title>

        <style>

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                min-height: 100vh;
            }

            .navbar {
                padding: 20px 8%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background: rgba(15, 23, 42, 0.9);
                border-bottom: 1px solid rgba(255,255,255,0.1);
            }

            .logo {
                font-size: 24px;
                font-weight: bold;
            }

            .logo span {
                color: #38bdf8;
            }

            .status {
                background: #14532d;
                color: #86efac;
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 14px;
            }

            .hero {
                text-align: center;
                padding: 80px 20px 50px;
            }

            .hero h1 {
                font-size: 52px;
                margin-bottom: 20px;
            }

            .hero h1 span {
                color: #38bdf8;
            }

            .hero p {
                font-size: 20px;
                color: #cbd5e1;
                max-width: 700px;
                margin: auto;
                line-height: 1.6;
            }

            .container {
                max-width: 1100px;
                margin: auto;
                padding: 20px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }

            .card {
                background: rgba(30, 41, 59, 0.85);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 25px;
                text-align: center;
                transition: transform 0.3s ease;
            }

            .card:hover {
                transform: translateY(-8px);
            }

            .icon {
                font-size: 38px;
                margin-bottom: 15px;
            }

            .card h3 {
                margin-bottom: 10px;
                color: #f8fafc;
            }

            .card p {
                color: #94a3b8;
            }

            .deployment {
                margin-top: 40px;
                padding: 30px;
                background: rgba(15, 23, 42, 0.8);
                border-radius: 15px;
                border: 1px solid rgba(56, 189, 248, 0.2);
            }

            .deployment h2 {
                margin-bottom: 20px;
                color: #38bdf8;
            }

            .pipeline {
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 15px;
            }

            .step {
                background: #1e293b;
                padding: 15px 20px;
                border-radius: 10px;
                text-align: center;
                flex: 1;
                min-width: 130px;
            }

            .step strong {
                display: block;
                margin-bottom: 5px;
            }

            .step small {
                color: #94a3b8;
            }

            .arrow {
                color: #38bdf8;
                font-size: 25px;
            }

            .footer {
                text-align: center;
                padding: 40px 20px;
                color: #64748b;
            }

            .health {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 25px;
                background: #166534;
                border-radius: 8px;
                color: #bbf7d0;
            }

            @media (max-width: 700px) {

                .hero h1 {
                    font-size: 36px;
                }

                .pipeline {
                    flex-direction: column;
                }

                .arrow {
                    transform: rotate(90deg);
                }

            }

        </style>

    </head>

    <body>

        <nav class="navbar">

            <div class="logo">
                Kastro<span>DevOps</span>
            </div>

            <div class="status">
                ● Application Online
            </div>

        </nav>


        <section class="hero">

            <h1>
                Python <span>Docker</span> Application
            </h1>

            <p>
                A containerized Flask application deployed automatically
                using Docker and GitHub Actions.
            </p>

            <div class="health">
                ✓ Application is Healthy
            </div>

        </section>


        <div class="container">

            <div class="cards">

                <div class="card">

                    <div class="icon">🐍</div>

                    <h3>Python</h3>

                    <p>
                        Python 3.11 application
                        running with Flask.
                    </p>

                </div>


                <div class="card">

                    <div class="icon">🌐</div>

                    <h3>Flask</h3>

                    <p>
                        Lightweight Python web
                        application framework.
                    </p>

                </div>


                <div class="card">

                    <div class="icon">🐳</div>

                    <h3>Docker</h3>

                    <p>
                        Application packaged and
                        deployed as a container.
                    </p>

                </div>


                <div class="card">

                    <div class="icon">⚙️</div>

                    <h3>GitHub Actions</h3>

                    <p>
                        Automated CI/CD deployment
                        using a self-hosted runner.
                    </p>

                </div>

            </div>


            <div class="deployment">

                <h2>🚀 Deployment Pipeline</h2>

                <div class="pipeline">

                    <div class="step">
                        <strong>Git Push</strong>
                        <small>Source Code</small>
                    </div>

                    <div class="arrow">→</div>

                    <div class="step">
                        <strong>GitHub Actions</strong>
                        <small>CI/CD</small>
                    </div>

                    <div class="arrow">→</div>

                    <div class="step">
                        <strong>Docker Build</strong>
                        <small>Image</small>
                    </div>

                    <div class="arrow">→</div>

                    <div class="step">
                        <strong>Container</strong>
                        <small>Deployment</small>
                    </div>

                </div>

            </div>

        </div>


        <footer class="footer">

            <p>
                Kastro DevOps • Python • Flask • Docker • GitHub Actions
            </p>

            <p style="margin-top: 10px;">
                © 2026 Kastro Application
            </p>

        </footer>

    </body>

    </html>
    """


@app.route("/health")
def health():

    return {
        "status": "UP",
        "application": "kastro-python-app",
        "framework": "Flask",
        "container": "Docker",
        "ci_cd": "GitHub Actions",
        "runner": "Self-hosted"
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
