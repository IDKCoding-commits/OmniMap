from nicegui import ui
from functions import handle_submit, clear_input, on_submit
from crawl4ai import *
import asyncio


#Displays simple header with name of app
with ui.header(elevated=True):
    ui.label("OmniMap").style('font-size: 1.6em')

#All of this is code for the input field
with ui.column().classes('w-full items-center'):
    input_area = ui.textarea("Input Game Title Here").props('rows=1').style('width: 300px')
    ui.button('Submit', on_click=lambda: on_submit(input_area))


ui.run(port=8081)
