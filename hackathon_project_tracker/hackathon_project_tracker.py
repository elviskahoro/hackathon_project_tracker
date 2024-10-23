import reflex as rx

from .app_style import Style as AppStyle
from .pages.project_tracker.page import index
from .pages.project_tracker.state import State

APP_STYLE: AppStyle = AppStyle()


app = rx.App(
    style=APP_STYLE.dark,
    theme=rx.theme(
        has_background=True,
        radius="large",
        accent_color="teal",
    ),
)
app.add_page(
    component=index(
        placeholder_function=State.placeholder_function,
    ),
    route="/",
    on_load=State.on_load,
)
