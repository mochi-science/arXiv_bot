from libs.fetch_arxiv import fetch_papers_from_arxiv
from libs.summarize import get_summary_by_gpt
from libs.to_message import send_message_to_discord
from datetime import datetime
from ast import literal_eval
import json


def main():
    webhookurl = json.load(open("webhook_url.json"))["URL"]
    today = datetime.today().strftime('%Y-%m-%d')

    # arXiv APIを使用して論文を取得し、CSVファイルに保存
    df_papers = fetch_papers_from_arxiv()
    if df_papers.empty:
        send_message_to_discord(f"## {today} 新しい論文はありませんでした。", webhookurl)

    # OpenAI APIを使用して論文の要約を取得
    key = json.load(open("openai_apikey.json"))["KEY"]
    res = get_summary_by_gpt(api_key=key, df_papers=df_papers)

    # 要約をデータフレームに追加
    summary_text = res["content"]
    # 要約文のみを取得（時々余計なメッセージがついてくる）
    summary_text = summary_text[summary_text.index("["):summary_text.index("]")+1]
    summary_list = literal_eval(summary_text)
    df_papers["Summary"] = summary_list

    # Discordにメッセージを送信
    message = f"## {today} の最新論文をお送ります。"
    for i, row in enumerate(df_papers.iterrows()):
        # Discordにメッセージ制限があるため、3つの論文ごとにメッセージを送信
        if i % 3 == 0:
            send_message_to_discord(message, webhookurl)
            message = ""
        row = row[1]
        message += f"\n### タイトル: {row['Title']}\n**検索条件: {row['Theme']}**\nURL: <{row['URL']}>\nPDF: <{row['PDF']}>\n要約: {row['Summary']}"
    # 最後のメッセージを送信
    send_message_to_discord(message, webhookurl)

if __name__ == "__main__":
    main()