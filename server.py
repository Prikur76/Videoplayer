from livereload import Server


def rebuild():
    print('Site rebuilt')


server = Server()
server.watch('src/*.html', rebuild())
server.serve(root='.', default_filename='src/index.html')
