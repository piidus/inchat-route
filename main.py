import flet as ft
from components.page_control import PageControl
from components.utils import get_device_ip

def main(page: ft.Page):
    # Get the some_value (e.g., IP address) and pass it to the PageControl
    some_value = "Your IP Address or some_value"
    page.window.always_on_top = True
    ip_address = get_device_ip()
    controller = PageControl(page, some_value="Some Value")
    page.add(controller.build())
    try:
        page_url = str(page.url).split(':')[1]
        if page_url != '//localhost':
            # Handle link request
            route, *params = page.url.split("?")
            controller.change_page(route, **ip_address)  # Pass the dictionary as keyword arguments
        else:
            controller.change_page("/page1", **ip_address)  # Pass the dictionary as keyword arguments
    except Exception as e:
        print(e)

    
    # controller.change_page("/page1", **ip_address)  # Pass the dictionary as keyword arguments

    # controller = PageControl(page, some_value)
    # page.add(controller.build())
    # # page_control = PageControl(page)

    # # Route to the initial page
    # # controller.change_page("/page1")
    #  # Get the device's IP address
    # ip_address = get_device_ip()
    # try:
    #     # chek it a localhost
    #     page_url = str(page.url).split(':')[1]
    #     if page_url != '//localhost':
    #         # Handle link request
    #         route, *params = page.url.split("?")
    #         controller.change_page(route, *params)
    #     else:
    #         controller.change_page("/page1", **ip_address)
    # except Exception as e:
    #     print(e)

ft.app(target=main)
