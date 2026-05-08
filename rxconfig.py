import reflex as rx
from decouple import config

DATABASE_URL = config('DATABASE_URL')

config = rx.Config(
    app_name="appNotes",
    db_url='DATABASE_URL',
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin()
    ]
)