import time
from datetime import datetime as dt


def host_temp():
    # returns the relative path to the demo hosts file,
    # demo hosts file is in same directory with this file.
    return "hosts"

def host_path():
    # returns the abosulte path to the real hosts file
    return r"C:\Windows\System32\drivers\etc\hosts"

def redirect_path():

    return "127.0.0.1"

def domain_names():
    # Collects a string of domain urls,
    # splits it into a list type.
    domains = input(
        "If more than One domain is given," +
        " seperate it with a comma(,) delimiter.\n"
    ).split(",")

    return domains

def website_to_block(domain):
    # Removes some traces of whitespace using LC.
    domain_lists = [x.strip() for x in domain]

    # Checks if the user submitted an empty domain.
    if "" not in domain_lists:
        return domain_lists
    else:
        print("You need to pass in at least a domain url.")
        #updated the time of python exe, makes the above code
        #to be seen before python exe closes.
        time.sleep(5)
        # Stops the code from executing on the terminal
        quit()
website_to_block = website_to_block(domain_names())

def start_hour():

    try:
        #Using the walrus operator, start_hour variable is been checked on the condition
        #and sametime returned without explicitly calling the varaible

        if 23 >= (start_hour := int(
                input("range of working hours should be given as an" + 
                    " integer from 0...23\nStarting hours: "
            ).strip())) >= 0:
            pass
        else:
            print("working hours should be in the range of 0...23")
            #updated the time of python exe, makes the above code
            #to be seen before python exe closes.
            time.sleep(5)
            quit()
        
        # Using normal assignment operator with variable been called explicitly   
        # start_hour = int(input(
        #     "range of working hours should be given as an integer from 0...23" +
        #     "\nStarting hours: "
        # ).strip())
        # if 23 >= start_hour >= 0:
        #     start_hour = start_hour
    except ValueError:    
        start_hour = "Starting hours should be an instance of an integer."
    
    return start_hour

# Capturing what start_hour returns 
# will be need as a default argument 
# in check_date() function
starting_hour = start_hour()

def end_hour():

    try:
        if 23 >= (end_hour := int(
                input("range of working hours should be given as an "+ 
                    "integer from 0...23\nEnding hours: "
            ).strip())) >= 0:
            pass
       
        else:
            print("working hours should be in the range of 0...23")
            time.sleep(5)
            quit()

        # Using normal assignment operator with variable been called explicitly   
        # end_hour = int(input(
        #     "range of working hours should be given as an integer from 0...23" +
        #     "\nEnding hours: "
        # ).strip())

        # if 23 >= end_hour >= 0:
        #     end_hour = end_hour
        # else:
        #     print("working hours should be in the range of 0...23")
        #     quit()
                      
    except ValueError:
        end_hour = "Ending hours should be an instance of an integer."

    return end_hour
# Capturing what end_hour returns 
# will be need as a default argument 
# in check_date() function
ending_hour = end_hour()

# Using the variables(starting_hour, ending_hour) as a default args in the function.
# This helps in the webblocking_running_script() function. details will be shown.
def check_date(start_hour=starting_hour, end_hour=ending_hour):

    if isinstance(start_hour, int) and isinstance(end_hour, int):
        from_date = dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
        today_date = dt.now()
        to_date = dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
        return from_date < today_date < to_date
    else:
        print(f'Start:{start_hour} & End:{end_hour}')
        #updated the time of python exe, makes the above code
        #to be seen before python exe closes.
        time.sleep(8)
        quit()

def webblocking_running_script():
    while True:
        # Reason why there was a default args in the check_date() function
        # was at this, if you call the function with args, u will be pausing
        # the loop due to the input function in start_hour and end_hour functions.  
        if check_date():
            print("This is your working hours don't be distracted!")
            with open(host_path(), "r+") as file:
                content = file.read()
                for website in website_to_block:
                    if website not in content:
                        file.write(
                            redirect_path() + "    " + website + "\n"
                        )
        else:
            print("This is your free time enjoy it.")
            with open(host_path(), 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_to_block):
                        file.write(line)
                file.truncate()
        time.sleep(10)
webblocking_running_script()
