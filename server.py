from livereload import Server


def rebuild():
    print('Site rebuilt')


server = Server()
server.watch('dist/templates/*.html', rebuild())
server.serve(root='.', default_filename='dist/templates/index.html')
