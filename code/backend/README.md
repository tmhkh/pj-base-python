# バックエンド（FastAPI）

## 概要

- `/api/v1/messages/echo` のエコー API を 1 件提供
- `.env` 経由でアプリ名や API プレフィックスを変更可能
- フロントエンド開発用に CORS を緩めた設定を同梱

## ローカル開発手順

1. 仮想環境を作成し有効化する
2. `pip install -r requirements.txt` で依存パッケージを導入
3. `uvicorn app.main:app --reload` で API を起動

### 主な環境変数

| 変数名 | 既定値 | 説明 |
| --- | --- | --- |
| `APP_NAME` | `PJ-base Backend` | アプリケーション名 |
| `APP_ENV` | `development` | 実行環境ラベル |
| `API_V1_PREFIX` | `/api/v1` | API ルートのベースパス |

### テスト

ユニットテストを追加する場合は `tests/` ディレクトリを作成して配置してください。
