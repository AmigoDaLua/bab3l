"""
BAB3L is a simple antidistraction app:
just type your <url>, click "Go!" and 
read your text from the web without
annoyint ads or any other distraction.
All without leaving the terminal!
"""
import pyperclip
import requests
import html2text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Static, Input, TextArea, Label


def main():
    run_app()


"""Function that starts the App"""
def run_app():
    app = PROJECT()
    app.run()


"""Function that gets the text from <url>"""
def get_text_from_url(url):
    try:
        page = requests.get(url)
        if (page.status_code == 200):
            h = html2text.HTML2Text()
            h.mark_code = True
            h.strong_mark = "**"
            h.emphasis_mark = "**"
            h.pad_tables

            """Getting mardown text"""
            text_body = h.handle(page.text)
            return text_body
    except:
        return "Sadly, BAB3L can't access that url. Try another one! 👹"
    
"""Function that shows a error message if """
def exception_message(source):
    source.text = "Some weird exception happened with BAB3L... Try another <url>! 👹"
    

"""Classes for App"""
class BAB3L(Static):
    def compose(self) -> ComposeResult:
        """Top container"""
        with Horizontal(classes="container_top_panel"):
            yield Label("[BAB3L]", classes="label")
            yield Static(" is a simple tool to get the text you want from a html page.")
        """Main container"""
        with Horizontal(classes="container_main"):
            with Vertical(classes="container_url"):
                yield Input(placeholder="Enter <url> and click 'Go!'", id="url")
                yield Button("GO!", id="btn_go", variant="success")
                yield Button("COPY YOUR TEXT", id="btn_copy")
                yield Button("CLEAR URL FIELD", id="btn_clear", variant="warning")
                yield Button("QUIT", id="btn_exit", variant="error")
            yield TextArea(classes="output_box")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Button GO!"""
        if event.button.id == "btn_go":
            url = self.query_one("#url").value
        # There's is a URL?
            if (url != ""):
                try:
                    # Does the URL work?
                    text = get_text_from_url(url)
                    output_box = self.query_one(".output_box")
                    output_box.text = text
                except:
                    # No?
                    output_box = self.query_one(".output_box")
                    exception_message(output_box)
        
        """Button QUIT"""
        if event.button.id == "btn_exit":
            App.exit(self)

        """Button COPY"""
        if event.button.id == "btn_copy":
            output_box = self.query_one(".output_box")
            """They wrote something?"""
            if len(output_box.text) != 0:
                """Using <pyperclip> library to copy text to clipboard"""
                pyperclip.copy(output_box.text)
                pyperclip.paste()
        
        """Button CLEAR"""
        if event.button.id == "btn_clear":
            caixa_url = self.query_one("#url")
            caixa_url.value = ""

            
class PROJECT(App):
    """Defining styles path"""
    CSS_PATH = "styles.tcss"
    """Setting key bindings"""
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Composing the App"""
        yield Header(show_clock=True)
        yield Footer()
        yield BAB3L()

    def action_toggle_dark(self) -> None:
        """Action to toggle dark mode."""
        self.dark = not self.dark


"""Calling main() to start the program"""
if __name__ == "__main__":
    main()