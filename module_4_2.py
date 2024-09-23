def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()  # Я в области видимости функции test_function
# inner_function() # при вызове вне test_function(): name 'inner_function' is not defined.
