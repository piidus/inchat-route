import flet as ft
from components.utils import get_device_ip
from components.connection import Connection
import threading
class Message:
    '''message require self name and text and type'''
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


class ChatMessage(ft.Row):
    '''
    create chat message take raw message and design here!
    '''
    def __init__(self, message: Message, type = 'outgoing'):
        super().__init__()
        avatar = ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            )
        content = ft.Column(
                [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            )
        
        if type == 'outgoing':
            self.alignment = align=ft.MainAxisAlignment.END
            self.controls = [content, avatar]
        else:
            self.alignment = ft.MainAxisAlignment.START
            self.controls = [avatar, content]
        
        
        # self.controls = [
        #     ft.CircleAvatar(
        #         content=ft.Text(self.get_initials(message.user_name)),
        #         color=ft.colors.WHITE,
        #         bgcolor=self.get_avatar_color(message.user_name),
        #     ),
        #     ft.Column(
        #         [
        #             ft.Text(message.user_name, weight="bold"),
        #             ft.Text(message.text, selectable=True),
        #         ],
        #         tight=True,
        #         spacing=5,
        #     )
            
        # ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


class Conversion:
    '''
    __init__ and build function to create chat ui
    setup_chat_ui function to setup chat ui
    send_message_click function to send message
    get_device_ip function to get device ip
    join_chat_click function to join chat
    

    '''

    def __init__(self, page: ft.Page, **kwargs):
        self.page = page
        self.some_value = kwargs.get('some_value', 'Default Value')
        self.chat = ft.ListView(expand=True, spacing=10, auto_scroll=True, reverse=True) #whole chat area as a list view
        self.dialog = None
        self.new_message = None
        # self.device_ip = get_device_ip()['ip_address']
        self.receiver = None
    
    def did_mount(self):
        try:
            self.connection = Connection(user=self.page.session.get('user_name'))
            receive_thread = threading.Thread(target=self.receive_messages, args=(self.connection,))
            receive_thread.start()
            # self.connection.send('baba'.encode('utf-8'))
        except Exception as e:
            print('[ERROR IM DID MOUNT CONNECTION]', e)

    def build(self):
        self.page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH #stretch horizontally
        # self.page.title = f"Flet Chat - {self.some_value}"

        self.setup_chat_ui() # call to create chat ui

        return ft.Column(
            [
                ft.Container(
                    content=self.chat,
                    border=ft.border.all(1, ft.colors.OUTLINE),
                    border_radius=5,
                    padding=10,
                    expand=True,
                ),
                ft.Row(
                    [
                        self.new_message,
                        ft.IconButton(
                            icon=ft.icons.SEND_ROUNDED,
                            tooltip="Send message",
                            on_click=self.send_message_click,
                        ),
                    ]
                ),
            ],
            expand=True,
        )
    
    def setup_chat_ui(self):
        """
        Sets up the user interface for the chat application.

        This function is responsible for creating and configuring the necessary UI elements,
        including the dialog for entering the user's name and the text field for sending messages.
        It also sets up the event handlers for the UI elements.

        Parameters:
            self: The instance of the class that this function is a part of.

        Returns:
            None
        """

        # self.page.pubsub.subscribe(self.on_message) # subscribe to on_message event

        # A dialog asking for a user display name
        join_friend_name = ft.TextField(
            label="Enter your name of Friend",
            autofocus=True,
            on_submit=self.join_chat_click,
        )
        self.dialog = ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Welcome!" ),
            content=ft.Column([join_friend_name], width=300, height=70, tight=True),
            actions=[ft.ElevatedButton(text="Join chat", on_click=self.join_chat_click)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.overlay.append(self.dialog)

        # A new message entry form
        self.new_message = ft.TextField(
            hint_text="Write a message...",
            autofocus=True,
            # shift_enter=True,
            multiline=True,
            # min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
            on_submit=self.send_message_click,
        )

    def join_chat_click(self, e):
        """
        Handles the click event of the "Join chat" button.
        set receiver name to session
        """

        join_user_name = self.dialog.content.controls[0]
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            self.page.session.set("receiver_name", join_user_name.value)
            self.dialog.open = False
            self.new_message.prefix = ft.Text(f"You :: ")
            self.page.update()
    
    def send_message_click(self, e):
        """
        Handles the click event of the "Send message" button.

        Parameters:
            self: The instance of the class that this function is a part of.
            e: The event object associated with the click event.

        Returns:
            None
        """

        if self.new_message.value != "":
            receiver = self.page.session.get("receiver_name")
            
            self.connection.message_sent(receiver=receiver, message=self.new_message.value)
            self.on_message(message=Message(user_name=self.page.session.get("user_name"), text=self.new_message.value, message_type="chat_message"))
            self.new_message.value = ""
            self.new_message.focus()
            self.page.update()


    def on_message(self, message: Message):
        """
        Handles incoming messages and updates the chat UI accordingly.

        """

        if message.message_type == "chat_message":
            m = ChatMessage(message, type='outgoing')

        elif message.message_type == "receive_chat":
            m = ChatMessage(message, type='incoming')

        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
        self.chat.controls.insert(0, m)
        self.page.update()
    def receive_messages(self , client_socket):
        while True:
            try:
                message = client_socket.receive()
                usr, msg = message.split(": ")
                self.on_message(message=Message(user_name=usr, text=msg, message_type="receive_chat"))
                print(f"[RECEIVED MESSAGE] {message}")
            except Exception as e:
                print(f"[ERROR] Receiving message failed: {e}")
                break

