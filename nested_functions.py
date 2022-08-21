def task(name):
    def some_private():
        print(name)
    some_private()
task('Hira')