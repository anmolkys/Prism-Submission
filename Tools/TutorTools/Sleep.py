from langchain.tools import tool
import time

class Sleep():

    @tool
    def sleep():
        """
        Puts crew to sleep.
        """

        time.sleep(15 * 60)