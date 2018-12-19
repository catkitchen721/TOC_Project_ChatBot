from transitions.extensions import GraphMachine
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from send_msg import send_text_message, send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        self.target_page_no_num_string = "https://m.click108.com.tw/astro/index.php?astroNum="
        self.ptt_page_string = "https://www.ptt.cc/bbs/Beauty/index.html"
        self.pttroot = "https://www.ptt.cc"

    def get_titles(self, page_string):

        r = Request(page_string)
        r.add_header("user-agent", "Mozilla/5.0")

        result = []
        returnurls = []
        page = urlopen(r)
        soup = BeautifulSoup(page, 'html.parser')

        divs = soup.find_all('div', 'r-ent')
        for d in divs:
            # 取得文章連結及標題
            if d.select('.title'):  # 有超連結，表示文章存在，未被刪除
                t = d.select('.title')[0]
            result.append(t)

        for d in result:
            if d.find('a'):
                picurl = d.find('a')['href']
                returnurls.append(picurl)

        return returnurls

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

    def is_going_to_subUser(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '查其他'
        return False

    def is_going_to_beautyState(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '圖呢'
        return False

    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '幫助'
        return False

    def on_enter_subUser(self, event):
        print("subuser")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "還想查點什麼呢～\n"
                                      + "[可用指令]\n"
                                      + "  -> 查星座\n"
                                      + "  -> 圖呢\n"
                                      + "  -> 幫助")

    def on_enter_beautyState(self, event):
        print("這不是來了嗎～")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "這不是來了嗎～")
        send_image_message(sender_id, "https://i.imgur.com/6Ej1jNd.jpg")

        # count = 0
        #
        # for half_entryurl in self.get_titles(self.ptt_page_string):
        #
        #     send_text_message(sender_id, half_entryurl)
        #     entryurl = self.pttroot + half_entryurl
        #
        #     r = Request(entryurl)
        #     r.add_header("user-agent", "Mozilla/5.0")
        #
        #     page = urlopen(r)
        #     soup = BeautifulSoup(page, 'html.parser')
        #
        #     d = soup.find(id='main-content')
        #     all_a = d.find_all('a')
        #
        #     for a in all_a:
        #         picurl = a.text
        #         if picurl[0:20] == 'https://i.imgur.com/':
        #             print(picurl)
        #             send_image_message(sender_id, picurl)
        #             break

        self.go_back(event)

    def on_enter_help(self, event):
        print("幫助")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "[幫助]\n"
                          + "* 查星座\n    查詢當日星座運勢\n"
                          + "* 圖呢\n    潮男正妹的圖呢???\n"
                          + "* 幫助\n"
                          + "p.s: 進入[查星座]後，可不斷輸入星座，直到輸入[查其他]跳轉回去上一層")

        self.go_back(event)

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

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_taurusState(self, event):
        print("分析金牛座...")

        target_page_string = self.target_page_no_num_string + "2"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_geminiState(self, event):
        print("分析雙子座...")

        target_page_string = self.target_page_no_num_string + "3"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_cancerState(self, event):
        print("分析巨蟹座...")

        target_page_string = self.target_page_no_num_string + "4"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_leoState(self, event):
        print("分析獅子座...")

        target_page_string = self.target_page_no_num_string + "5"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_virgoState(self, event):
        print("分析處女座...")

        target_page_string = self.target_page_no_num_string + "6"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_libraState(self, event):
        print("分析天秤座...")

        target_page_string = self.target_page_no_num_string + "7"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_scorpioState(self, event):
        print("分析天蠍座...")

        target_page_string = self.target_page_no_num_string + "8"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_sagittariusState(self, event):
        print("分析射手座...")

        target_page_string = self.target_page_no_num_string + "9"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_capricornState(self, event):
        print("分析魔羯座...")

        target_page_string = self.target_page_no_num_string + "10"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_aquariusState(self, event):
        print("分析水瓶座...")

        target_page_string = self.target_page_no_num_string + "11"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_piscesState(self, event):
        print("分析雙魚座...")

        target_page_string = self.target_page_no_num_string + "12"
        target_page = urlopen(target_page_string)
        soup = BeautifulSoup(target_page, "html.parser")

        name_box = soup.find(id="astroDailyData_all")
        name = name_box.text.strip()
        print(name)

        sender_id = event['sender']['id']
        send_text_message(sender_id, name)
        send_text_message(sender_id, "[可用指令]\n"
                          + "  -> 查其他\n"
                          + "  -> （繼續輸入星座）")

        self.go_back(event)

    def on_enter_backState(self, event):
        print("進入循環模式")

    def on_exit_astroState(self, event):
        print('離開astroState')

    def on_exit_ariesState(self, event):
        print('離開ariesState')

    def on_exit_taurusState(self, event):
        print('離開taurusState')

    def on_exit_geminiState(self, event):
        print('離開geminiState')

    def on_exit_cancerState(self, event):
        print('離開cancerState')

    def on_exit_leoState(self, event):
        print('離開leoState')

    def on_exit_virgoState(self, event):
        print('離開virgoState')

    def on_exit_libraState(self, event):
        print('離開libraState')

    def on_exit_scorpioState(self, event):
        print('離開scorpioState')

    def on_exit_sagittariusState(self, event):
        print('離開sagittariusState')

    def on_exit_capricornState(self, event):
        print('離開capricornState')

    def on_exit_aquariusState(self, event):
        print('離開aquariusState')

    def on_exit_piscesState(self, event):
        print('離開piscesState')

    def on_exit_backState(self, event):
        print('離開backState')

    def on_exit_beautyState(self, event):
        print('離開beautyState')



