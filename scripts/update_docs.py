import yaml
import os
import sys

def generate_mermaid(openapi_data):
    lines = ["classDiagram"]
    
    # Schemas
    schemas = openapi_data.get("components", {}).get("schemas", {})
    for name, schema in schemas.items():
        lines.append(f"  class {name} {{")
        properties = schema.get("properties", {})
        for prop_name, prop_details in properties.items():
            prop_type = prop_details.get("type", "any")
            lines.append(f"    +{prop_type} {prop_name}")
        lines.append("  }")

    # Paths (Endpoints)
    paths = openapi_data.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            operation_id = details.get("operationId", f"{method}_{path.replace('/', '_')}")
            # Clean up operation_id for class name
            class_name = "".join(x.title() for x in operation_id.split("_")) + "Endpoint"
            
            lines.append(f"  class {class_name} {{")
            lines.append(f"    +{method.upper()} {path}")
            
            # Request Body
            request_body = details.get("requestBody", {})
            req_schema_ref = ""
            if request_body:
                content = request_body.get("content", {})
                json_content = content.get("application/json", {})
                schema_ref = json_content.get("schema", {}).get("$ref", "")
                if schema_ref:
                    req_schema_name = schema_ref.split("/")[-1]
                    lines.append(f"    +Request {req_schema_name}")
                    req_schema_ref = req_schema_name

            # Responses
            responses = details.get("responses", {})
            res_schema_ref = ""
            success_res = responses.get("200", {})
            if success_res:
                content = success_res.get("content", {})
                json_content = content.get("application/json", {})
                schema_ref = json_content.get("schema", {}).get("$ref", "")
                if schema_ref:
                    res_schema_name = schema_ref.split("/")[-1]
                    lines.append(f"    +Response {res_schema_name}")
                    res_schema_ref = res_schema_name
            
            desc = details.get("description", "")
            if desc:
                # Truncate description if too long
                short_desc = (desc[:30] + '..') if len(desc) > 30 else desc
                lines.append(f"    +Description \"{short_desc}\"")
            
            lines.append("  }")

            # Relationships
            if req_schema_ref:
                lines.append(f"  {class_name} --> {req_schema_ref}")
            if res_schema_ref:
                lines.append(f"  {class_name} --> {res_schema_ref}")

    return "\n".join(lines)

def update_markdown(md_path, mermaid_content):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- MERMAID-START -->"
    end_marker = "<!-- MERMAID-END -->"

    if start_marker not in content or end_marker not in content:
        print(f"Error: Markers not found in {md_path}")
        return

    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    new_content = content[:start_idx] + "\n```mermaid\n" + mermaid_content + "\n```\n" + content[end_idx:]
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Successfully updated {md_path}")

def main():
    # Paths relative to workspace root
    openapi_path = os.path.join("docs", "openapi.yaml")
    md_path = os.path.join("docs", "API仕様書.md")

    if not os.path.exists(openapi_path):
        print(f"Error: {openapi_path} not found")
        return

    with open(openapi_path, "r", encoding="utf-8") as f:
        openapi_data = yaml.safe_load(f)

    mermaid_content = generate_mermaid(openapi_data)
    update_markdown(md_path, mermaid_content)

if __name__ == "__main__":
    main()
