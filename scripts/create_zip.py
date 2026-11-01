import os
import zipfile
import base64
import json

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ARTIFACT_DIR = '/.aistudio/artifacts/brain/d5720dbc-ed35-4678-8aae-8c683916ad38'

OUTPUT_ZIPS = [
    os.path.join(ROOT_DIR, 'public', 'kurd-chat-project.zip'),
    os.path.join(ROOT_DIR, 'public', 'KurdChat_Domino_Source_Code.zip'),
    os.path.join(ARTIFACT_DIR, 'kurd-chat-project.zip'),
    os.path.join(ARTIFACT_DIR, 'KurdChat_Domino_Source_Code.zip'),
]

EXCLUDE_DIRS = {
    'node_modules',
    '.git',
    '.aistudio',
    'dist',
    '.cache',
    '__pycache__',
}

EXCLUDE_EXTS = {
    '.zip',
    '.mp4',
}

# Create zip archives
for zip_path in OUTPUT_ZIPS:
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)
    print(f"Creating ZIP archive: {zip_path}")
    
    file_count = 0
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(ROOT_DIR):
            # Exclude folders
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in EXCLUDE_EXTS:
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ROOT_DIR)
                
                zipf.write(full_path, rel_path)
                file_count += 1

    file_size = os.path.getsize(zip_path)
    print(f"Packed {file_count} files into {zip_path} ({file_size} bytes)")

# Write metadata for artifact files
main_zip_artifact = os.path.join(ARTIFACT_DIR, 'kurd-chat-project.zip')
meta_path = main_zip_artifact + '.metadata.json'
meta_content = {
    "summary": "Complete Kurd Chat & Domino real project downloadable ZIP archive containing all source code, assets, audio, Kurdish translations, Domino multiplayer engine, and server files.",
    "userFacing": True,
    "requestFeedback": False
}
with open(meta_path, 'w', encoding='utf-8') as f:
    json.dump(meta_content, f, indent=2, ensure_ascii=False)
print(f"Created metadata: {meta_path}")

# Second zip metadata
meta_path2 = os.path.join(ARTIFACT_DIR, 'KurdChat_Domino_Source_Code.zip.metadata.json')
meta_content2 = {
    "summary": "Full official source code package for Kurd Chat & Domino Game with real-time Express backend, Kurdish voice chat, stories, and offline installation.",
    "userFacing": True,
    "requestFeedback": False
}
with open(meta_path2, 'w', encoding='utf-8') as f:
    json.dump(meta_content2, f, indent=2, ensure_ascii=False)

# Also generate Base64 string for offline html
with open(os.path.join(ROOT_DIR, 'public', 'kurd-chat-project.zip'), 'rb') as f:
    b64_str = base64.b64encode(f.read()).decode('utf-8')

b64_js_path = os.path.join(ROOT_DIR, 'scripts', 'zip_base64.js')
with open(b64_js_path, 'w', encoding='utf-8') as f:
    f.write(f'export const PROJECT_ZIP_BASE64 = "{b64_str}";\n')
print(f"Generated Base64 module: {b64_js_path} (length: {len(b64_str)})")

print("All ZIP archives and metadata generated successfully!")

