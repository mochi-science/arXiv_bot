# 使用するライブラリのインポート
import arxiv
import pandas as pd
import os

def fetch_papers_from_arxiv(search_query=None, max_results=3, csv_filename = "datas/arxiv_papers.csv") -> pd.DataFrame:
    """
    arXiv APIを使用して論文を取得し、CSVファイルに保存する関数

    Parameters:
        search_query (dict{"thema": "query"}): 検索クエリ
            ex) queries = {
                    "LLM": 'cat:cs.CL OR cat:cs.AI AND "large language model"',
                    "Machine Learning": 'cat:cs.LG OR cat:stat.ML AND "machine learning"',
                    "XAI": 'cat:cs.AI OR cat:cs.LG AND "explainable AI"'
                }
        max_results (int): 取得する論文の最大数
        csv_filename (str): 保存するCSVファイル名

    Returns:
        DataFrame: 新しい論文情報を含むDataFrame
    """
    if search_query is None:
        # テーマごとのクエリ
        queries = {
            "LLM": 'cat:cs.CL OR cat:cs.AI AND "large language model"',
            "Machine Learning": 'cat:cs.LG OR cat:stat.ML AND "machine learning"',
            "XAI": 'cat:cs.AI OR cat:cs.LG AND "explainable AI"'
        }
    
    # 新しく取得した論文の情報を格納するリスト
    new_papers_list = []

    # 既存のCSVファイルを読み込む（存在すれば）
    if os.path.exists(csv_filename):
        existing_papers_df = pd.read_csv(csv_filename)
    else:
        # CSVが存在しない場合は空のDataFrameを作成
        existing_papers_df = pd.DataFrame(columns=["Title", "Authors", "Published", "URL", "Abstract", "PDF"])

    # 既存のURL一覧を取得
    existing_urls = existing_papers_df["URL"].tolist()

    # 各クエリで論文を取得し、既存のデータと比較
    for theme, query in queries.items():
        search = arxiv.Search(
            query=query,
            max_results=max_results,  # 各テーマで取得する最大論文数
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        for result in search.results():
            # 論文情報を辞書にまとめる
            paper_info = {
                "Title": result.title,
                "Theme": theme,
                "Authors": ', '.join([author.name for author in result.authors]),
                "Published": str(result.published),
                "URL": result.entry_id,
                "Abstract": result.summary,
                "PDF": result.pdf_url
            }

            # 既存の論文リストにないか、または更新されている場合はリストに追加
            if paper_info["URL"] not in existing_urls or paper_info["Published"] != existing_papers_df.loc[existing_papers_df["URL"] == paper_info["URL"], "Published"].values[0]:
                new_papers_list.append(paper_info)

    # 新しい論文があれば処理
    if new_papers_list:
        # 新しい論文のDataFrameを作成
        new_papers_df = pd.DataFrame(new_papers_list)

        # 既存の論文と新しい論文を結合
        updated_papers_df = pd.concat([existing_papers_df, new_papers_df], ignore_index=True)

        # CSVファイルに上書き保存
        updated_papers_df.to_csv(csv_filename, index=False)

        # print(f"{len(new_papers_list)} 件の新しい論文を追加しました。")

    return new_papers_df
