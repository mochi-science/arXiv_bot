# ここにSlackなどのメッセージ送信用の関数を記述する

from discord_webhook import DiscordWebhook

def send_message_to_discord(message: str, webhook_url: str):
    """Discordにメッセージを送信する

    Args:
        message (str): 送信するメッセージ
        webhook_url (str): DiscordのWebhook URL

    Returns:
        response: webhookによるレスポンス
    """
    # メッセージを送信
    webhook = DiscordWebhook(url=webhook_url, content=message)
    response = webhook.execute()

    return response