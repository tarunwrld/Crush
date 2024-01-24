from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.properties import ObjectProperty
# from kivy.uix.screenmanager import Screen

# from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.modalview import ModalView
# from kivy.factory import Factory
# server imports
import socket
import threading
from kivymd.uix.label import MDLabel
# from kivy.clock import mainthread
from kivy.clock import Clock
import os

# CHAT_HISTORY_FILE = os.path.join('C:\\' , 'Users', 'hp', 'TarunCode', 'Python', 'crush', 'chat_history.txt')
# NICKNAME_HISTORY_FILE = os.path.join('C:\\' , 'Users', 'hp', 'TarunCode', 'Python', 'crush', 'nickname_history.txt')
current_directory = os.getcwd()  # Get the current working directory
filename = 'chat_history.txt'
CHAT_HISTORY_FILE = os.path.join(current_directory, filename)
filename = 'nickname_history.txt'
NICKNAME_HISTORY_FILE = os.path.join(current_directory, filename)



# from kivymd.uix.navigationdrawer import NavigationLayout
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

KV = '''
ScreenManager:
    HomeScreen:
    ChatScreen:
    MultichatScreen:
    SettingScreen:
    AccountScreen:
    HelpScreen:
    ErrorScreen:
    DevloperScreen:
    ContactScreen:
    BugScreen:
    PrivateScreen:
    ChatSelectScreen:
    JoinbyipScreen:

<HomeScreen>:
    name: 'home'
    nick_label: nick_label
    MDBoxLayout:
        orientation: "vertical"
        RelativeLayout:
            Image:
                source: "minimal2.jpg"
                allow_stretch: True
                keep_ratio: False
            MDLabel:
                id:nick_label
                text: "Hello: "
                font_style: "H6"
                halign: "center"
                pos_hint: {"center_y": 0.85, "center_x": 0.16}
                size_hint_y: None 
            MDIconButton:
                icon: "home-outline"
                # theme_icon_color: "Custom"
                # icon_color: 1,1,1,1
                size_hint: None, None
                size: dp(64), dp(64)
                pos_hint: {"center_y": 0.95, "center_x": 0.06}
                on_release: nav_drawer.set_state("toggle")

            MDIconButton:
                icon: "beaker-question-outline"
                # theme_icon_color: "Custom"
                # icon_color: 1,1,1,1
                size_hint: None, None
                size: dp(64), dp(64)
                pos_hint: {"center_y": 0.95, "center_x": 0.87}  # position the button on the left side
                on_press: 
                    root.manager.current = 'help'
                    root.manager.transition.direction = 'left' 

            MDIconButton:
                icon: "dots-vertical"
                # theme_icon_color: "Custom"
                # icon_color: 1,1,1,1
                size_hint: None, None
                size: dp(64), dp(64)
                pos_hint: {"center_y": 0.95, "center_x": 0.95}
                on_press: 
                    # root.manager.current = 'test'
                    root.manager.current = 'error'
                    root.manager.transition.direction = 'down'

   


    MDBoxLayout:
        padding:[dp(15),dp(15),dp(15),dp(35)]
        spacing:dp(25)
        ElementCard:
            size_hint_x: 0.2
            size_hint_y: 0.3
            on_press: 
                root.manager.current = 'sel'
                root.manager.transition.direction = 'left'
            Image:
                source: 'lomes.png'

        ElementCard:
            size_hint_x: 0.2
            size_hint_y: 0.3
            on_press: 
                root.manager.current = 'setting'
                root.manager.transition.direction = 'left'
            Image:
                source: 'set1.png'

    MDNavigationDrawer:
        id: nav_drawer
        MDBoxLayout:
            orientation: 'vertical'
            # spacing: '8dp'
            # padding: '8dp'

            Image: 
                source: 'crush2.png'
            MDLabel:
                text: 'C R U S H'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Profile'
                        on_press: 
                            root.manager.current = 'account'
                            root.manager.transition.direction = 'left'
                        IconLeftWidget:
                            icon: 'account-outline'
                    OneLineIconListItem:
                        text: 'About'
                        on_press: 
                            root.manager.current = 'help'
                            root.manager.transition.direction = 'left'
                        IconLeftWidget:
                            icon: "information-outline"
                    OneLineIconListItem:
                        text: 'Help'
                        on_press : 
                            root.manager.current = 'bug'
                            root.manager.transition.direction = 'left'
                        IconLeftWidget:
                            icon: "lightbulb-question-outline"
                    OneLineIconListItem:
                        text: 'Exit'
                        on_press : root.onp()
                        IconLeftWidget:
                            icon: "exit-to-app"

            # MDBoxLayout:
            #     Image:
            #         source: 'girl.gif'
                            
                            
                
<HelpScreen>:
    name: 'help'
    Image:
        source: 'bird.jpg'
        allow_stretch: True
        keep_ratio: False
        size_hint: (1, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    ScrollView:
        MDList:

            OneLineIconListItem:
                text: "Developer"
                on_press: 
                    root.manager.current = 'devlp'
                    root.manager.transition.direction = 'left'
                IconLeftWidget:
                    icon: "account"

            OneLineIconListItem:
                text: "Contact Us"
                on_press: 
                    root.manager.current = 'cont'
                    root.manager.transition.direction = 'left'
                IconLeftWidget:
                    icon: "email"

            OneLineIconListItem:
                text: "BUGS"
                on_press: 
                    root.manager.current = 'bug'
                    root.manager.transition.direction = 'left'
                IconLeftWidget:
                    icon: "bug-outline"

            OneLineIconListItem:
                text: "Version"
                IconLeftWidget:
                    icon: "information"

            OneLineIconListItem:
                text: "Website"
                IconLeftWidget:
                    icon: "web"


                
    MDRectangleFlatButton:
        text: 'Back to Home'
        icon: "arrow-left"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        md_bg_color: 0,0,0,0
        on_press : 
            root.manager.current = 'home'
            root.manager.transition.direction = 'right'


        
<AccountScreen>:
    name: "account"

    nickname_label:nickname_label
    profile: profile

    Image:
        source: 'petrol.jpg'
        allow_stretch: True
        keep_ratio: False
        size_hint: (1, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    # MDLabel:
    #     text: "This is Account Screen"
    #     hallign: "centre"

    MDIconButton:
        icon: "arrow-left"
        # theme_icon_color: "Custom"
        # icon_color: 1,1,1,1
        size_hint: None, None
        size: dp(64), dp(64)
        pos_hint: {"center_y": 0.95, "center_x": 0.05}
        on_press : 
            root.manager.current = 'home'
            root.manager.transition.direction = 'right'
   
    MDCard:
        md_bg_color: rgba(0, 0, 0, 0)
        size_hint: 0.8, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        # elevation: 10
        padding: dp(8)
        # radius: dp(20)

        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(16)

            # Profile picture
            MDFloatLayout:
                size_hint_y: None
                height: dp(200)

                MDIconButton:
                    icon: "camera"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    # on_release: app.change_profile_picture()

                # MDUserAvatar:
                #     id: profile_picture
                #     source: app.profile_picture
                #     size_hint: None, None
                #     size: dp(150), dp(150)
                #     pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        # Nickname label
            MDLabel:
                id: nickname_label
                text: "Nickname: "
                font_style: "H5"
                halign: "center"
                size_hint_y: None
                # height: self.texture_size[1]

            # Nickname field
            MDTextField:
                id : profile
                hint_text: "Enter your nickname"
                mode: "rectangle"
                icon_right: "account"
                # size_hint: 0.8, None
                # height: dp(48)
                max_text_length: 20
                # on_text_validate: app.submit_nickname(self.text)
            MDIconButton:
                id: send_btn
                icon: "account-edit"
                pos_hint: {"center_x": 0.8, "center_y": 0.6}
                md_bg_color: app.theme_cls.primary_color
                on_press: root.submit_nickname()




<ChatScreen>:
    name: 'chat'

    chat_text: chat_text
    message_text: message_text
    send_btn: send_btn
    # con_btn: con_btn

    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Global Chat"
            pos_hint: {"top": 1}
            elevation: 10
            left_action_items:
                [['arrow-left', lambda x: setattr(root.manager, 'current', 'sel')]]
            right_action_items:
                [["connection", lambda x: root.connection(), "Connect" ],["ghost-off",  lambda x: root.disconnect(), "Close the Connection"]]

        ScrollView:
            TextInput:
                id: chat_text
                multiline: True
                size_hint_y: None
                height: self.minimum_height
                disabled: True

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.2
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: message_text
                hint_text: "Type a message"
                size_hint_x: 0.8
                max_text_length: 150
                multiline: True

            MDIconButton:
                id: send_btn
                icon: "send"
                md_bg_color: app.theme_cls.primary_color
                on_press: root.send_message()

    # MDFloatingActionButton:
    #     id: con_btn
    #     icon: "account-network"
    #     md_bg_color: app.theme_cls.accent_color
    #     pos_hint: {'center_x': 0.9, 'center_y': 0.2}
    #     on_press : root.connection()

<PrivateScreen>:
    name: 'private'
    ip_address_input: ip_address_input
    port_input: port_input
    start_button: start_button
    pchat_text: pchat_text

    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)

        MDTopAppBar:
            title: "Server Configuration"
            pos_hint: {"top": 1}

        ScrollView:
            TextInput:
                id: pchat_text
                multiline: True
                size_hint_y: None
                height: "200dp"
                disabled: True
                background_color: app.theme_cls.divider_color
                foreground_color: app.theme_cls.text_color

        # MDToolbar:
        #     title: "Server Configuration"
        #     pos_hint: {"top": 1}

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)

            MDTextField:
                id: ip_address_input
                hint_text: "Enter IP Address"
                mode: "rectangle"
                # size_hint_x: None
                width: "300dp"

            MDTextField:
                id: port_input
                hint_text: "Enter Port"
                mode: "rectangle"
                # size_hint_x: None
                width: "300dp"

            BoxLayout:
                size_hint_y: None
                height: "50dp"
                spacing: dp(10)
                pos_hint: {"center_x": 0.5}

                MDRaisedButton:
                    id: start_button
                    text: "Start Server"
                    # size_hint_x: None
                    width: "150dp"
                    on_release: root.start_server()

                MDRaisedButton:
                    text: "Stop Server"
                    # size_hint_x: None
                    width: "150dp"
                    on_release: root.stop_server()
                MDRaisedButton:
                    text: "Back"
                    on_press: 
                        root.manager.current = 'setting'
                        root.manager.transition.direction = 'right'
                    # size_hint_x: None
                    width: "150dp"


<ChatSelectScreen>:
    name: 'sel'

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        
        MDTopAppBar:
            title: "Your Chats"
            pos_hint: {"top": 1}
            elevation: 1
            left_action_items:
                [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)

            MDSegmentedControl:
                pos_hint: {"center_x": .5}
                size_hint_y: None

                MDSegmentedControlItem:
                    text: "Chats"

                MDSegmentedControlItem:
                    text: "Social"

            ScrollView:
                MDList:
                    id: chat_list
                    # Content for "Chats" segment
                    OneLineIconListItem:
                        text: 'Global Server'
                        on_press: 
                            root.manager.current = 'chat'
                            root.manager.transition.direction = 'left'
                        IconLeftWidget:
                            icon: 'earth'

                    OneLineIconListItem:
                        text: 'Join by IP'
                        on_press: 
                            root.manager.current = 'join'
                            root.manager.transition.direction = 'left'
                        IconLeftWidget:
                            icon: 'ip-network'

        MDFloatingActionButton:
            icon: "plus"
            pos_hint: {"center_x": 0.9}
            on_release: root.add_item()


# <ChatSelectScreen>:
#     name: 'sel'
    
#     BoxLayout:
#         orientation: 'vertical'
#         spacing: dp(10)
#         MDSegmentedControl:
#             pos_hint: {"center_x": .5, "center_y": .5}
#             MDTopAppBar:
#                 title: "Your Chats"
#                 pos_hint: {"top": 1}
#                 elevation: 1
#                 left_action_items:
#                     [['arrow-left', lambda x: setattr(root.manager, 'current', 'home')]]


#             MDSegmentedControlItem:
#                 text: "Chats"        
#                 ScrollView:
#                     MDList:
#                         OneLineIconListItem:
#                             text: 'Global Server'
#                             on_press: 
#                                 root.manager.current = 'chat'
#                                 root.manager.transition.direction = 'left'
#                             IconLeftWidget:
#                                 icon: 'earth'
                        
#                         OneLineIconListItem:
#                             text: 'Join by IP'
#                             on_press: 
#                                 root.manager.current = 'join'
#                                 root.manager.transition.direction = 'left'
#                             IconLeftWidget:
#                                 icon: 'ip-network'



<SettingScreen>:
    name: 'setting'
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: 'Theme'
                # text_color: 1, 1, 1, 1 if app.theme_cls.theme_style == 'Dark' else 0, 0, 0, 1
                on_press : root.theme_change()
                IconLeftWidget:
                    icon: "theme-light-dark"
            OneLineIconListItem:
                text: 'Be a Host'
                on_press: 
                    root.manager.current = 'private'
                    root.manager.transition.direction = 'left'
                # text_color: 1, 1, 1, 1 if app.theme_cls.theme_style == 'Dark' else 0, 0, 0, 1
                IconLeftWidget:
                    icon: "server-network"
            OneLineIconListItem:
                text: 'Push Notifications'
                IconLeftWidget:
                    icon: 'bell'

                Switch:
                    # id: push_notification_switch
                    active: True
                    pos_hint: {'center_x': 0.85, 'center_y': 0.4}
                

    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        # md_bg_color: "red"
        on_press : 
            root.manager.current = 'home'
            root.manager.transition.direction = 'right'

<ErrorScreen>:
    name: 'error'
    Image:
        source: 'seterror.png'
        allow_stretch: True
        keep_ratio: False
        size_hint: (1, 1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    Image:
        source: 'scream.gif'
        pos_hint: {'center_x': 0.8, 'center_y': 0.3}
    MDRectangleFlatButton:
        text: 'back'
        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        md_bg_color: "red"
        on_press : 
            root.manager.current = 'home'
            root.manager.transition.direction = 'up'

<DevloperScreen>:
    name: 'devlp'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "From Devloper"
            pos_hint: {"top": 1}
            elevation: 1
            left_action_items:
                [['arrow-left', lambda x: setattr(root.manager, 'current', 'help')]]
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: "10dp"
                
                MDLabel:
                    text: "This messaging app was developed with the goal of providing a seamless and user-friendly experience for communication. With a range of features and a clean design, it aims to enhance your messaging experience."

                MDLabel:
                    text: "Key Features:"
                    font_style: "H6"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1] + dp(10)

                MDLabel:
                    text: "1. Real-time messaging: Stay connected with friends and family instantly."

                MDLabel:
                    text: "2. Group chats: Create groups and have conversations with multiple people."

                MDLabel:
                    text: "3. Multimedia sharing: Share photos, videos, and documents seamlessly."

                MDLabel:
                    text: "4. Emojis and stickers: Express yourself with a wide range of emojis and stickers."

                MDLabel:
                    text: "5. Notifications: Receive timely notifications for new messages."

                MDLabel:
                    text: "Happy messaging!"

<ContactScreen>:
    name: 'cont'
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: 'Contact Us'
            pos_hint: {"top": 1}
            elevation: 1
            left_action_items: 
                [['arrow-left', lambda x: setattr(root.manager, 'current', 'help')]]

        ScrollView:
            GridLayout:
                cols: 1
                spacing: dp(10)
                padding: dp(20)
                MDLabel:
                    text: "Email: gojochan31@gmail.com"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "Phone: no information available"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "Address: no information available"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "Social Media: no information available"
                    theme_text_color: "Secondary"

                MDLabel:
                    text: "Website: no information available"
                    theme_text_color: "Secondary"

<BugScreen>:
    name: 'bug'
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        MDTopAppBar:
            title: 'Bug'
            pos_hint: {"top": 1}
            elevation: 1
            left_action_items: 
                [['arrow-left', lambda x: setattr(root.manager, 'current', 'help')]]

        MDLabel:
            text: 'Known Bugs:'
            font_style: 'H6'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(10)

        MDLabel:
            text: '1. Connection should be made manually because it is a beta version.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(5)

        MDLabel:
            text: '2. Users are advised to click on the kill switch to break the connection before exiting the app.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(5)

        MDLabel:
            text: '3. The app might be slow.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(5)

        MDLabel:
            text: '4. Theme issue.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(5)

        MDLabel:
            text: '5. Text input field loses focus randomly.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(5)

        MDLabel:
            text: '6. Incorrect data displayed in the chart view.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(5)

        MDLabel:
            text: 'Please note that these bugs are being actively worked on for the next release.'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1] + dp(10)
    
        # MDRaisedButton:
        # text: 'Show Card'
        # on_release: app.show_card_popup()

<JoinbyipScreen>:
    name: 'join'
    con_grid: con_grid
    ip_input : ip_input
    portro_input: portro_input
    co_btn: co_btn
    soup_text: soup_text
    rest_text: rest_text
    send2_btn: send2_btn

    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Private Room"
            pos_hint: {"top": 1}
            elevation: 1
            left_action_items:
                [['arrow-left', lambda x: setattr(root.manager, 'current', 'sel')]]
            right_action_items:
                [["connection", "Connect" ],["ghost-off",  lambda x: root.disconnect2(), "Close the Connection"]]


        BoxLayout:
            id: con_grid
            orientation: 'horizontal'
            size_hint_y: None
            height: self.minimum_height
            padding: dp(16)
            spacing: dp(16)

            MDTextField:
                id: ip_input
                hint_text: "IP Address"
                required: True
                mode: "rectangle"
                # size_hint_x: None
                width: "200dp"
                helper_text_mode: "on_error"

            MDTextField:
                id: portro_input
                hint_text: "Port"
                input_filter: "int"
                required: True
                mode: "rectangle"
                # size_hint_x: None
                width: "200dp"
                helper_text_mode: "on_error"

            MDRaisedButton:
                id: co_btn
                text: "Connect"
                on_release: root.connect_to_server()


        ScrollView:
            TextInput:
                id: soup_text
                multiline: True
                size_hint_y: None
                height: "200dp"
                disabled: True
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.2
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: rest_text
                hint_text: "Type a message"
                size_hint_x: 0.8
                max_text_length: 150
                multiline: True

            MDIconButton:
                id: send2_btn
                icon: "send"
                md_bg_color: app.theme_cls.primary_color
                on_press: root.send_messages2()



<ElementCard@MDCard>:
    # md_bg_color:69/255,55/255,86/255,1
    md_bg_color: rgba(0, 0, 0, 0)
    padding:dp(15)
    spacing:dp(15)
    radius:dp(25)
    ripple_behavior: True

<ElementCard@MDCard>:
    # md_bg_color:69/255,55/255,86/255,1
    md_bg_color: rgba(0, 0, 0, 0) 
    padding:dp(15)
    spacing:dp(15)
    radius:dp(25)
    ripple_behavior: True
    # on_release: app.on_click()

    
'''

class HomeScreen(Screen):
    nick_label = ObjectProperty(None)  # Define nick_label as an ObjectProperty with a default value of None

    def on_enter(self, *args):
        if os.path.exists(NICKNAME_HISTORY_FILE):
            with open(NICKNAME_HISTORY_FILE, "r") as f:
                nickname = f.read().strip()
            if self.nick_label is not None:
                self.nick_label.text = f"Hello: {nickname}"  # Access nick_label if it's not None
        else:
            if self.nick_label is not None:
                self.nick_label.text = "Hello:"

    def submit_nickname(self):
        nickname = self.ids.profile.text
        with open(NICKNAME_HISTORY_FILE, "w") as f:
            f.write(nickname)

        if self.nick_label is not None:
            self.nick_label.text = f"Nickname: {nickname}"
    # def update_nick_label(self):
    #     with open(NICKNAME_HISTORY_FILE, "r") as f:
    #         nickname = f.read().strip()
    #     self.ids.nickname_label.text = f"HELLO {nickname}"

    def onp(self):
        Crush.get_running_app().stop()


class ChatScreen(Screen):

    def __init__(self, client=None, **kwargs):
        super().__init__(**kwargs)
        self.client = client
        # self.chat_text = None"

    def connection(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('212.ip.ply.gg', 10369))
            message = self.client.recv(2048).decode('utf-8')
            if message == 'NICK':
                with open(NICKNAME_HISTORY_FILE, "r") as f:
                    nickname = f.read().strip()
                self.client.send(nickname.encode('utf-8'))
                # self.client.send(f"Cheeku".encode('utf-8'))
            threading.Thread(target= self.receive).start()
            # thread = threading.Thread(target=self.receive)
            # thread.start() 
        except Exception as e:
            print(f"Error in connection: {e}")

    def on_pre_enter(self):
        try:
            with open(CHAT_HISTORY_FILE, 'r') as f:
                self.ids.chat_text.text = f.read()
        except FileNotFoundError:
            pass

    def send_message(self):
        try:
            if self.client:
                with open(NICKNAME_HISTORY_FILE, "r") as f:
                    nickname = f.read().strip()
                message = f"{nickname}: {self.ids.message_text.text}"
                message = self.ids.message_text.text
                self.client.send(message.encode("utf-8"))
                self.message_text.text = ""
        except Exception as e:
            print(f"Error in sending message: {e}")
    

    def append_message(self, message):

        nickname = ""
        with open(NICKNAME_HISTORY_FILE, "r") as f:
            nickname = f.read().strip()
        Clock.schedule_once(lambda dt: self.ids.chat_text.insert_text(f"{nickname}: {message}\n"), 0.1)

    def receive(self):
        self.stop_receive = False
        while not self.stop_receive:
            try:
                # print("checking receive function")
                message = self.client.recv(2048).decode("utf-8")
                if message:
                    # self.ids.chat_text.insert_text(f"Server: {message}\n")
                    self.append_message(message)
                    with open(CHAT_HISTORY_FILE, 'a') as f:
                        f.write(f" {message}\n")
            except socket.error as e:
                if e.errno == 10038:
                    break
                else:
                    print(f"Error in recv: {e}")
                    break
            except Exception as e:
                print(f"Error in receving: {e}")
                break
                # print(f"Error in recv: {e}")
                # stop = True
                # client.close()

    
    # def close(self):
    #     print("closed")
    #     if self.stop_receive(False):
    #         self.client.close()
    #         self.stop_receive = True
    def disconnect(self):
        if self.client is not None:
            self.client.close()
            print("Disconnected")
    # def update_chat_text(self, message):
        # self.ids.chat_text.text += message + "\n"
        # self.chat_text.text += message + "\n"
        # self.chat_text.cursor = (0, 0)



class SettingScreen(Screen):
    def theme_change(self):
        app = MDApp.get_running_app()
        if app.theme_cls.theme_style == "Dark":
            app.theme_cls.theme_style = "Light"
            app.theme_cls.theme_style_switch_animation = True
            app.theme_cls.theme_style_switch_animation_duration = 0.8
        else:
            app.theme_cls.theme_style = "Dark"
            app.theme_cls.theme_style_switch_animation = True
            app.theme_cls.theme_style_switch_animation_duration = 0.8
        self.update_text_color()

    def update_text_color(self):
        app = MDApp.get_running_app()
        text_color = (1, 1, 1, 1) if app.theme_cls.theme_style == "Dark" else (0, 0, 0, 1)

        for widget in app.root.walk():
            if isinstance(widget, Label):
                widget.text_color = text_color


class AccountScreen(Screen):


    def on_enter(self, *args):
        if os.path.exists(NICKNAME_HISTORY_FILE):
            with open(NICKNAME_HISTORY_FILE, "r") as f:
                nickname = f.read().strip()
            self.ids.nickname_label.text = f"Nickname: {nickname}"
        else:
            self.ids.nickname_label.text = "Nickname:"

    def submit_nickname(self):
        nickname = self.ids.profile.text
        with open(NICKNAME_HISTORY_FILE, "w") as f:
            f.write(nickname)

        self.ids.nickname_label.text = f"Nickname: {nickname}"

class MultichatScreen(Screen):
    pass

class ContentNavigationDrawer():
    pass
class HelpScreen(Screen):
    pass

class ErrorScreen(Screen):
    pass
class DevloperScreen(Screen):
    pass
class ContactScreen(Screen):
    pass
class BugScreen(Screen):
    pass
class ChatSelectScreen(Screen):

    item_count = 0


    def add_item(self):
        self.item_count += 1
        item_text = f"Room {self.item_count}"
        new_item = OneLineIconListItem(text=item_text)
        new_item.add_widget(IconLeftWidget(icon="human-capacity-increase"))
        new_item.bind(on_release=self.goto_next_screen)
        self.ids.chat_list.add_widget(new_item)

    def goto_next_screen(self, item):
        next_screen = JoinbyipScreen(name=f'join{self.item_count}')
        if hasattr(next_screen.ids, 'item_label'):
            next_screen.ids.item_label.text = item.text
        self.manager.add_widget(next_screen)
        self.manager.current = next_screen.name

    # def goto_next_screen(self, item):
    #     next_screen = JoinbyipScreen(name='join')
    #     if hasattr(next_screen.ids, 'item_label'):
    #         next_screen.ids.item_label.text = item.text
    #     self.manager.add_widget(next_screen)
    #     self.manager.current = 'join'



class PrivateScreen(Screen):
    def start_server(self):
        ip_address = self.ip_address_input.text
        port = self.port_input.text

        # Check if IP address and port are entered
        if not ip_address or not port:
            print("Please enter IP address and port.")
            return

        # Update the server configuration
        global HOST, PORT
        HOST = ip_address
        PORT = int(port)

        # Starting Server
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

    def stop_server(self):
        # Check if the server has been started
        if hasattr(self, 'server'):
            # Stop the server
            stop_thread = threading.Thread(target=self.stop_server_thread)
            stop_thread.start()

    def stop_server_thread(self):
        # Close the server socket
        if hasattr(self, 'server'):
            self.server.shutdown(socket.SHUT_RDWR)
            self.server.close()
            del self.server

    def run_server(self):
        # Starting Server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()

        # Lists For Clients and Their Nicknames
        clients = []
        nicknames = []

        # Sending Messages To All Connected Clients
        def broadcast(message):
            for client in clients:
                if isinstance(client, socket.socket):
                    client.send(message)

        # Handling Messages From Clients
        def handle_connection(client):
            stop = False
            while not stop:
                try:
                    # Check if the socket is still open
                    if client.fileno() == -1:
                        stop = True
                        break

                    # Broadcasting Messages
                    message = client.recv(1024)
                    broadcast(message)
                except:
                    # Removing And Closing Clients
                    index = clients.index(client)
                    clients.remove(client)
                    nickname = nicknames[index]
                    nicknames.remove(nickname)
                    broadcast(f"{nickname} left the chat!!".encode('utf-8'))
                    client.close()
                    stop = True

        # Start the server and handle client connections
        self.update_text( "#######################- ...SERVER IS RUNNING... -#######################\n")
        print("#######################- ...SERVER IS RUNNING... -#######################")
        while True:
            client, addr = server.accept()
            self.update_text("Connected with {}\n".format(str(addr)))

            client.send("NICK".encode('utf-8'))

            nickname = client.recv(2048).decode('utf-8')
            nicknames.append(nickname)
            clients.append(client)
            self.update_text( "Nickname is {}\n".format(nickname))

            broadcast("{} joined!".format(nickname).encode('ascii'))

            client.send("You are now connected!!".encode('utf-8'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=handle_connection, args=(client,))
            thread.start()
    def update_text(self, text):
        Clock.schedule_once(lambda dt: self.ids.pchat_text.insert_text(text))



    def disconnect(self):
        if self.client is not None:
            self.client.close()
            print("Disconnected")
    # def go_back(self):
    #     self.manager.current = 'main'

    
    # def __init__(self, host,port,server, **kwargs):
    #     super().__init__(**kwargs)
    # # def __init__(self, host,port,server):
    #     self.host = self.ip_address_input.text
    #     self.port = 8888
    #     self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.clients = []
    #     self.nicknames = []

    #     self.server.bind((host, port))
    #     self.server.listen()

    #     clients = []
    #     nicknames = []
    

    #     def broadcast(message):
    #         for client in clients:
    #             if isinstance(client, socket.socket):
    #                 client.send(message)

    #     def handle_connection(client):
    #         stop = False
    #         while not stop:
    #             try:
    #                 # Check if the socket is still open
    #                 if client.fileno() == -1:
    #                     stop = True
    #                     break
                    
    #                 # Broadcasting Messages
    #                 message = client.recv(1024)
    #                 broadcast(message)
    #             except:
    #                 # Removing And Closing Clients
    #                 index = clients.index(client)
    #                 clients.remove(client)
    #                 nickname = nicknames[index]
    #                 nicknames.remove(nickname)
    #                 broadcast(f"{nickname} left the chat!!".encode('utf-8'))
    #                 client.close()
    #                 stop = True

    #     def main():
    #         print("#######################- ...SERVER IS RUNNING... -#######################")
    #         while True:
    #             client, addr = server.accept()
    #             print("Connected with {}".format(str(addr)))
    #             # print(f"connected to {addr}")

    #             client.send("NICK".encode('utf-8'))

    #             nickname = client.recv(2048).decode('utf-8')
    #             nicknames.append(nickname)
    #             clients.append(client)
    #             print("Nickname is {}".format(nickname))
    #             # print(f"Nickname is {nickname}")

    #             broadcast("{} joined!".format(nickname).encode('ascii'))
    #             # broadcast(f"{nickname} joined the chat!!")

    #             client.send("You are now connected!!".encode('utf-8'))

    #             # Start Handling Thread For Client
    #             thread = threading.Thread(target=handle_connection, args=(client,))
    #             thread.start()



    # def start(self):
    #     self.server.bind((self.host, self.port))
    #     self.server.listen()
    #     print(f"#######################- ...SERVER IS RUNNING... -#######################")
    #     while True:
    #         client, addr = self.server.accept()
    #         print("Connected with {}".format(str(addr)))

    #         client.send("NICK".encode('utf-8'))
    #         nickname = client.recv(2048).decode('utf-8')
    #         self.nicknames.append(nickname)
    #         self.clients.append(client)
    #         print("Nickname is {}".format(nickname))

    #         self.broadcast("{} joined!".format(nickname).encode('ascii'))
    #         client.send("You are now connected!!".encode('utf-8'))

    #         thread = threading.Thread(target=self.handle_connection, args=(client,))
    #         thread.start()

    # def handle_connection(self, client):
    #     stop = False
    #     while not stop:
    #         try:
    #             if client.fileno() == -1:
    #                 stop = True
    #                 break
    #             message = client.recv(1024)
    #             self.broadcast(message)
    #         except:
    #             index = self.clients.index(client)
    #             self.clients.remove(client)
    #             nickname = self.nicknames[index]
    #             self.nicknames.remove(nickname)
    #             self.broadcast(f"{nickname} left the chat!!".encode('utf-8'))
    #             client.close()
    #             stop = True

    # def broadcast(self, message):
    #     for client in self.clients:
    #         if isinstance(client, socket.socket):
    #             client.send(message)


# class MyScreenManager(ScreenManager):
#     def switch_to_home_screen(self):
#         self.transition = SlideTransition(direction='right')
#         self.current = 'home'
    pass

class JoinbyipScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = client
        self.ip_input = None
        self.portro_input = None
        self.chat_text = None
        self.rest_text = None

    def connect_to_server(self):
        # ip = self.ids['ip_input'].text
        # port = self.ids['portro_input'].text

        ip = self.ids.ip_input.text
        port = self.ids.portro_input.text
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((ip, int(port)))
            message = self.client.recv(2048).decode('utf-8')
            if message == 'NICK':
                self.make_invisible(self.con_grid)
                # self.make_invisible(self.ip_input)
                # self.make_invisible(self.portro_input)
                # self.make_invisible(self.co_btn)
                with open(NICKNAME_HISTORY_FILE, "r") as f:
                    nickname = f.read().strip()
                self.client.send(nickname.encode('utf-8'))
            threading.Thread(target=self.receive2).start()
        except Exception as e:
            print(f"Error in connection: {e}")
    
    def make_invisible(self,widget):
        widget.visible = False
        widget.size_hint_x = None
        widget.size_hine_y = None
        widget.height = 0
        widget.width = 0
        # widget.text = ""
        # widget.capacity = 0
        widget.disabled = True
        widget.opacity = 0

    def send_messages2(self):
        try:
            if self.client:
                with open(NICKNAME_HISTORY_FILE, "r") as f:
                    nickname = f.read().strip()
                message = f"{nickname}: {self.ids.rest_text.text}"
                self.client.send(message.encode("utf-8"))
                self.ids.rest_text.text = ""
        except Exception as e:
            print(f"Error in sending message: {e}")

    # def append_message2(self, message):
    #     nickname = ""
    #     with open(NICKNAME_HISTORY_FILE, "r") as f:
    #         nickname = f.read().strip()
    #     self.ids['chat_text'].insert_text(f"{nickname}: {message}\n")

    def append_message2(self, message):
        nickname = ""
        with open(NICKNAME_HISTORY_FILE, "r") as f:
            nickname = f.read().strip()
        # Clock.schedule_once(lambda dt: self.ids['chat_text'].insert_text(f"{nickname}: {message}\n"), 0.1)
        # Clock.schedule_once(lambda dt: self.ids.chat_text.insert_text(f"{nickname}: {message}\n"), timeout=0.1)

        Clock.schedule_once(lambda dt: self.ids.soup_text.insert_text(f"{nickname}: {message}\n"), 0.1)

    
    def receive2(self):
        self.stop_receive2 = False
        while not self.stop_receive2:
            try:
                message = self.client.recv(2048).decode("utf-8")
                if message:
                    self.append_message2(message)
            except socket.error as e:
                if e.errno == 10038:
                    break
                else:
                    print(f"Error in recv: {e}")
                    break
            except Exception as e:
                print(f"Error in receiving: {e}")
                break

    def disconnect2(self):
        if self.client is not None:
            self.client.close()
            self.make_visible(self.con_grid)
            print("Disconnected")

    def make_visible(self,widget):
        widget.visible = True
        widget.size_hint_x = 1
        widget.size_hint_y = 0.2
        widget.height = 1
        widget.width = 1
        widget.opacity = 1
        widget.disabled = False


class Crush(MDApp):
    

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        # sm.add_widget(ChatScreen(name='chat', client=client))    
        sm.add_widget(ChatScreen(name='chat'))
        sm.add_widget(SettingScreen(name='setting'))
        sm.add_widget(HelpScreen(name='help'))
        sm.add_widget(AccountScreen(name='account'))
        sm.add_widget(ErrorScreen(name='error'))
        sm.add_widget(DevloperScreen(name='devlp'))
        sm.add_widget(ContactScreen(name='cont'))
        sm.add_widget(BugScreen(name='bug'))
        sm.add_widget(PrivateScreen(name='private'))
        sm.add_widget(ChatSelectScreen(name='sel'))
        sm.add_widget(JoinbyipScreen(name='join'))
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)
   

    
Crush().run()