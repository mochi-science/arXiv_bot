
# arXiv 論文通知ボット

このプロジェクトは、arXiv から論文を自動で取得し、Discord などのプラットフォームに通知を送信するボットです。

## 必要環境

このプロジェクトは Python 3.11.9 を使用しています。互換性を確保するため、`pyenv` を使って Python バージョンを管理し、`poetry` で依存関係を管理することを推奨します。

### 必要なツール
- `pyenv`（Python 3.11.9 の管理用）
- `poetry`（依存関係および仮想環境の管理用）

## セットアップ手順

1. **`pyenv` のインストール**  
   `pyenv` のインストール方法は [こちら](https://github.com/pyenv/pyenv#installation) を参照してください。インストール後、このプロジェクト用に Python 3.11.9 をインストールし、ローカルバージョンとして設定します。
   ```bash
   pyenv install 3.11.9
   pyenv local 3.11.9
   ```

2. **`poetry` のインストール**  
   `poetry` のインストール方法は [公式ドキュメント](https://python-poetry.org/docs/#installation) を参照してください。インストール後、次のコマンドでプロジェクトのセットアップを行います。
   ```bash
   poetry config virtualenvs.in-project true
   poetry install
   ```

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。