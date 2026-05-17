from typing import Dict, Any


def metadata_serializer(data) -> Dict[str, Any]:
    return {
        "url": data["url"],
        "headers": data["headers"],
        "cookies": data["cookies"],
        "page_source": data["page_source"]
    }