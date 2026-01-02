# PJ-base Python Webアプリ テンプレート

FastAPI と Vue.js を組み合わせたシンプルな Web アプリの雛形です。コードとドキュメントを明確に分離し、Mermaid を用いたサンプル資料を同梱しているため、新規プロジェクトの立ち上げを効率化できます。

## ディレクトリ構成

```text
├── docs/                     # Mermaid を含むドキュメント群
└── code/
    ├── backend/              # FastAPI バックエンド
    └── frontend/             # Vue.js (Vite) フロントエンド
```

## バックエンド（FastAPI）

- ソースは `code/backend` 配下に配置
- `/api/v1/messages/echo` へ POST されたメッセージをそのまま返却
- `.env` でアプリ名や API プレフィックスを設定可能

### セットアップと起動（Backend）

```powershell
cd code/backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

起動後は `http://127.0.0.1:8000` で API を確認できます。`/health` でヘルスチェックが可能です。

## フロントエンド（Vue.js + Vite）

- ソースは `code/frontend` 配下に配置
- 「PJ-base」というタイトルの青系デザインを採用
- フォームから入力した文章を API に送信し、レスポンスを表示

### セットアップと起動（Frontend）

```powershell
cd code/frontend
npm install
npm run dev
```

開発サーバーは `http://127.0.0.1:5173` で起動します。`.env` に `VITE_API_BASE_URL` を設定することでバックエンド接続先を変更できます（デフォルトは `http://127.0.0.1:8000`）。

## ドキュメント

- 機能仕様書: `docs/機能仕様書.md`
- API仕様書: `docs/API仕様書.md`
- 詳細設計書（エコー機能）: `docs/詳細設計書-エコー機能.md`

各ドキュメントは Markdown 形式で Mermaid 記法を使用しています。

### API仕様書の運用について

API仕様書は `docs/openapi.yaml` を正本として管理しています。`docs/API仕様書.md` は閲覧用として自動生成されます。

#### 開発環境のセットアップ(Gitフック)

本プロジェクトではドキュメントの自動更新のためにGitフックを使用しています。
リポジトリをクローンした後、**開発を開始する前に一度だけ**以下のスクリプトを実行してください。

```powershell
# 仮想環境が有効な状態で実行
python scripts/setup_hooks.py
```

#### 更新フロー

1. `docs/openapi.yaml` を編集
2. `git add docs/openapi.yaml`
3. `git commit`
   - 自動的に `docs/API仕様書.md` が更新され、コミットに含まれます。
