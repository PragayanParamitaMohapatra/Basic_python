import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title="Please Drink Water",
            message=" you need to drink adequate amounts of water. "
                    "There are many different opinions on how much water you should be drinking every day. "
                    "Health authorities commonly recommend eight 8-ounce glasses,"
                    " which equals about 2 liters, or half a gallon",
            app_icon = "download.ico",
            timeout=2

        )
        time.sleep(60*60)
