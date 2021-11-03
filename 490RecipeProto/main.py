from website import create_app

app = create_app()

#run everytime change is made
if __name__ == '__main__':
    app.run(debug=True)