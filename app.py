from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Myntra Demo</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f5f5f5;
            }

            .header {
                background: #ff3f6c;
                color: white;
                padding: 20px;
                text-align: center;
            }

            .container {
                text-align: center;
                padding: 50px 20px;
            }

            h1 {
                font-size: 40px;
            }

            .products {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
            }

            .product {
                background: white;
                padding: 25px;
                width: 180px;
                border-radius: 10px;
                box-shadow: 0 2px 8px #ccc;
            }

            .price {
                font-weight: bold;
                color: #ff3f6c;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>Myntra</h1>
            <p>Fashion for Everyone</p>
        </div>

        <div class="container">

            <h2>Welcome to Myntra Demo</h2>

            <div class="products">

                <div class="product">
                    <h3>T-Shirt</h3>
                    <p>Men's Casual T-Shirt</p>
                    <p class="price">₹599</p>
                </div>

                <div class="product">
                    <h3>Jeans</h3>
                    <p>Men's Regular Jeans</p>
                    <p class="price">₹1,299</p>
                </div>

                <div class="product">
                    <h3>Shoes</h3>
                    <p>Running Shoes</p>
                    <p class="price">₹1,999</p>
                </div>

                <div class="product">
                    <h3>Handbag</h3>
                    <p>Women's Handbag</p>
                    <p class="price">₹899</p>
                </div>

            </div>

            <br>

            <p>Application is running successfully 🚀</p>

        </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "UP"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)