import sys, webbrowser, time
from datetime import datetime

# Opens a url in a new browser window at the specified time
# If a new window can't be opened, will attempt a new tab then attempt to use an existing window in that order.
# Accurate to within 1 minute
# Enter arguments as "url hour minute" in 24-hour format to bypass menu.

def main():
    if len(sys.argv) < 4:
        print "This program opens a URL in a new browser window at the specified time (accurate to the minute)."
        print ""
        print "Please specify a URL."
        url = raw_input("Url: ")
        print ""
        print "Please specify a future time in 24-hour format."
        print "For example, 4:30 PM would be expressed as follows:"
        print "Hour: 16"
        print "Minute: 30"
        print ""
        hour = input("Hour: ")
        minute = input("Minute: ")
    else:
        url = str(sys.argv[1])
        hour = int(sys.argv[2])
        minute = int(sys.argv[3])
    test_var = True
    while True:
        if int(datetime.now().strftime("%H")) == hour and int(datetime.now().strftime("%M")) == minute:
            webbrowser.open_new(url)
            print "Done!"
            break
        elif test_var:
            print "Waiting..."
            test_var = False
            time.sleep(60)
        else:
            time.sleep(60)
    quit()
         
if __name__ == '__main__':
    main()