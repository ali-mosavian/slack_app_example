import os
from pathlib import Path
from typing import Any
from typing import Annotated

import typer
import certifi
from slack_bolt import App
from slack_bolt import Say
from slack_bolt.adapter.socket_mode import SocketModeHandler


@typer.run
def main(
    app_token: Annotated[str, typer.Option(envvar='slack_app_token', help='The Slack app token')],
    bot_token: Annotated[str, typer.Option(envvar='slack_bot_token', help='The Slack bot token')],
) -> None:
    os.environ['SSL_CERT_FILE'] = certifi.where()
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
    os.environ['SSL_CERT_DIR'] = Path(certifi.where()).parent.as_posix()

    app = App(token=bot_token)

    @app.message('hello')
    @app.event('app_mention')
    def handle(event: dict[str, Any], say: Say) -> None:
        print(event)
        user_id = event.get('user', 'unknown user')

        say(
            text=f'Hello, <@{user_id}>!',
            thread_ts=event.get('ts'), 
            channel=event.get('channel')
        )

    handler = SocketModeHandler(app, app_token=app_token)
    handler.start()


# Start the app
if __name__ == '__main__':
    main()
