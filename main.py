from libs.fetch_arxiv import fetch_papers_from_arxiv
from libs.summarize import get_summary_by_gpt
from libs.to_message import send_message_to_discord

def main():
    # arXiv APIを使用して論文を取得し、CSVファイルに保存
    df_papers = fetch_papers_from_arxiv()
    

if __name__ == "__main__":
    main()