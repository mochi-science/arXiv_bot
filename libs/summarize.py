import pandas as pd
from openai import OpenAI
import pandas as pd

def get_summary_by_gpt(api_key: str, df_papers: pd.DataFrame) -> dict:
    """論文の内容を要約したものを返す

    Args:
        api_key (str): OpenAI API キー
        df_papers (pd.DataFrame): 論文データ

    Returns:
        dict: レスポンスデータ（jsonをdictに変換したもの）
    """

    client = OpenAI(api_key=api_key)

    # リクエストのプロンプトを作成する
    prompt = "論文の概要を日本語でそれぞれ要約して。要約文のみ出力。"
    prompt += "出力例：pythonのlist形式。"
    prompt += str(df_papers["Abstract"][:2].to_list())

    # OpenAI API にリクエストを送信する
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": "読者の興味を引く要素を強調"}, # 何かを知るにはまず興味をそそられることが重要
            {"role": "user", "content": prompt}
        ]
    )

    response = completion.choices[0].message.to_dict()

    return response