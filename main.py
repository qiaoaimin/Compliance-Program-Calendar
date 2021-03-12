from website import create_app

app = create_app()

# @app.route('/')
# def hello_world():
#    return 'Hello world from Qiaoaimin! THis is {}'.format(__name__)

if __name__ == '__main__':
    app.run(debug=True)
