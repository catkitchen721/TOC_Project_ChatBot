from transitions.extensions import GraphMachine
from urllib.request import urlopen
from bs4 import BeautifulSoup

from send_msg import send_text_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        self.target_page_no_num_string = "https://m.click108.com.tw/astro/index.php?astroNum="

    def is_going_to_astroState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '查星座'
        return False

    def is_going_to_ariesState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '牡羊座'
        return False

    def is_going_to_taurusState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '金牛座'
        return False

    def is_going_to_geminiState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '雙子座'
        return False

    def is_going_to_cancerState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '巨蟹座'
        return False

    def is_going_to_leoState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '獅子座'
        return False

    def is_going_to_virgoState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '處女座'
        return False

    def is_going_to_libraState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '天秤座'
        return False

    def is_going_to_scorpioState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '天蠍座'
        return False

    def is_going_to_sagittariusState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '射手座'
        return False

    def is_going_to_capricornState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '魔羯座'
        return False

    def is_going_to_aquariusState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '水瓶座'
        return False

    def is_going_to_piscesState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '雙魚座'
        return False

    def on_enter_astroState(self, event):
        print("想查什麼星座呢？")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "想查什麼星座呢？")
        self.advance(event)

    def on_enter_ariesState(self, event):
        print("分析牡羊座...")

        target_page_string = self.target_page_no_num_string + "1"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_taurusState(self, event):
        print("分析金牛座...")

        target_page_string = self.target_page_no_num_string + "2"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_geminiState(self, event):
        print("分析雙子座...")

        target_page_string = self.target_page_no_num_string + "3"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_cancerState(self, event):
        print("分析巨蟹座...")

        target_page_string = self.target_page_no_num_string + "4"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_leoState(self, event):
        print("分析獅子座...")

        target_page_string = self.target_page_no_num_string + "5"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_virgoState(self, event):
        print("分析處女座...")

        target_page_string = self.target_page_no_num_string + "6"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_libraState(self, event):
        print("分析天秤座...")

        target_page_string = self.target_page_no_num_string + "7"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_scorpioState(self, event):
        print("分析天蠍座...")

        target_page_string = self.target_page_no_num_string + "8"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_sagittariusState(self, event):
        print("分析射手座...")

        target_page_string = self.target_page_no_num_string + "9"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_capricornState(self, event):
        print("分析魔羯座...")

        target_page_string = self.target_page_no_num_string + "10"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_aquariusState(self, event):
        print("分析水瓶座...")

        target_page_string = self.target_page_no_num_string + "11"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_enter_piscesState(self, event):
        print("分析雙魚座...")

        target_page_string = self.target_page_no_num_string + "12"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_career")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        self.go_back()

    def on_exit_astroState(self, event):
        print('離開astroState')

    def on_exit_cancerState(self):
        print('離開cancerState')

