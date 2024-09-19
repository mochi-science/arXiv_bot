from libs.fetch_arxiv import fetch_papers_from_arxiv

def main():
    # arXiv APIを使用して論文を取得し、CSVファイルに保存
    print(fetch_papers_from_arxiv())

if __name__ == "__main__":
    main()