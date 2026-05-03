import os
import sys
import yaml

# code/backend ディレクトリを Python パスに追加して app モジュールを読み込めるようにする
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code', 'backend'))
sys.path.insert(0, backend_path)

from app.main import app

def main():
    # FastAPI から OpenAPI スキーマを生成
    openapi_schema = app.openapi()
    
    # docs ディレクトリに出力
    docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs'))
    os.makedirs(docs_dir, exist_ok=True)
    out_path = os.path.join(docs_dir, 'openapi.yaml')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        yaml.dump(openapi_schema, f, allow_unicode=True, sort_keys=False)
        
    print(f"Successfully generated OpenAPI specs at: {out_path}")

if __name__ == "__main__":
    main()
