import datetime

def log_to_file(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):

            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            result = func(*args, **kwargs)


            with open(file_name, 'a') as file:
                file.write(f"{current_time} - Function '{func.__name__}' executed with result: {result}\n")

            return result

        return wrapper

    return decorator


@log_to_file('C:\\Users\\Yarik\\Desktop\\group_17112023\\log.txt')
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)