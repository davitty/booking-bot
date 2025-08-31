import time
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency('USD')
        bot.select_place_to_go(input("Where you want to go: "))
        bot.select_dates(input("Check in Date: (yyyy/mm/dd) "),input("Check Out Date: (yyyy/mm/dd) "))
        bot.select_adults(int(input("How many people? : ")))
        bot.click_search()
        bot.apply_filters()
        bot.report_results()
        time.sleep(5)
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise