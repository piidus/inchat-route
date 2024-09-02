import flet as ft
from page_control import PageControl
from menu import AppMenu
from utils import get_device_ip  # Assuming get_device_ip is in a utils.py file

def main(page: ft.Page):

    page.window.width = 300
    page.window.always_on_top = True
    # Initialize the PageControl
    page_control = PageControl(page)
    app_menu = AppMenu(on_route_change=page_control.change_page)
    
    # Add the menu to the page
    page.add(app_menu.build())
    page.add(page_control.build())

    # Get the device's IP address
    ip_address = get_device_ip()
    try:
        # chek it a localhost
        page_url = str(page.url).split(':')[1]
        if page_url != '//localhost':
            # Handle link request
            route, *params = page.url.split("?")
            page_control.change_page(route, *params)
        else:
            page_control.change_page("/page1", ip_address)
    except Exception as e:
        print(e)

    # # Check if the app was opened via a link
    # if page.url != 'tcp://localhost:64771':
    #     print(page.url)
        
    # else:
    #     # Normal open, route to Page1 with device IP address
    #     page_control.change_page("/page1", ip_address)

ft.app(target=main)
