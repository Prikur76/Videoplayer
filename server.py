from livereload import Server


def rebuild():
    print('Site rebuilt')


server = Server()
server.watch('*.html', rebuild())
server.serve(root='.', default_filename='index.html')
