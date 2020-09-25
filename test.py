

import json

namespaceId = 123
content = """
asd=asd
# 注释带引号 "asd"
345=123
"""


payload = json.dumps({
    "configText": content,
    "namespaceId": namespaceId,
    "format": "properties"
})

print(payload)
print(type(payload))
