from application import create_app

app = create_app("production")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7345, debug=False)
