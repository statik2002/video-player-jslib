from livereload import Server, shell
server = Server()
server.watch('/*.*', shell('make html', cwd='docs'))
server.serve(root='/_build/html')