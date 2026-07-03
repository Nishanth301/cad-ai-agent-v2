from pathlib import Path


def get_mime_type(image_path: str) -> str:

    extension = Path(image_path).suffix.lower()

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    return mime_types.get(extension, "image/png")
