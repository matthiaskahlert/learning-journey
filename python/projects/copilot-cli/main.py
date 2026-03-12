import asyncio
import os
import sys
from copilot import CopilotClient, PermissionHandler
from copilot.generated.session_events import SessionEventType


async def main():
    cli_url = os.getenv("COPILOT_CLI_URL")
    client_options = {"cli_url": cli_url} if cli_url else None
    client = CopilotClient(client_options)
    await client.start()

    try:
        session = await client.create_session(
            {
                "model": "gpt-4.1",
                "streaming": True,
                "on_permission_request": PermissionHandler.approve_all,
            }
        )

        def handle_event(event):
            if event.type == SessionEventType.ASSISTANT_MESSAGE_DELTA:
                sys.stdout.write(event.data.delta_content)
                sys.stdout.flush()
            if event.type == SessionEventType.SESSION_IDLE:
                print()

        session.on(handle_event)

        await session.send_and_wait({"prompt": "Tell me a short joke"}, timeout=120)
    finally:
        await client.stop()


asyncio.run(main())