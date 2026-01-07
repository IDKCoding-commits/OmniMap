from nicegui import ui

with ui.header(elevated=True):
    ui.label("OmniMap").style('font-size: 1.6em')


map_url = ("https://static0.polygonimages.com/wordpress/wp-content/uploads/chorus/uploads/chorus_asset/file/10071659/Zelda_Breath_of_the_Wild_all_shrines_map_Champions_Ballad_DLC.0.jpg?q=50&fit=crop&w=825&dpr=1.5")
ui.run(port=8081)
