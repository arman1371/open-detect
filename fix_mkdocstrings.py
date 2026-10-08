"""Fix mkdocstrings paths in docs."""
import os
import re

docs_dir = "/paperclip/instances/default/projects/c3154127-5c4c-40ce-a51e-e79b2d9ee076/0d32de91-f8a8-4216-8efe-ecfb65ffe6ce/open-detect/docs"

for root, dirs, files in os.walk(docs_dir):
    for fn in files:
        if fn.endswith('.md'):
            path = os.path.join(root, fn)
            with open(path) as f:
                content = f.read()
            # Fix mkdocstrings paths: ::: open-detect.X -> ::: open_detect.X
            content = re.sub(r':::`open-detect\.', ':::`open_detect.', content)
            content = re.sub(r':::: open-detect\.', ':::: open_detect.', content)
            with open(path, 'w') as f:
                f.write(content)
            print(f"Fixed {path}")

print("Done")
