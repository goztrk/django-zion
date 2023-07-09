# Python Standard Library
import json
import os

# ZION Shared Library Imports
from zion.apps.vite.conf import settings


def resolve_assets():
    if not os.path.exists(settings.ZION_VITE_MANIFEST_PATH) or not os.path.isdir(
        settings.ZION_VITE_MANIFEST_PATH
    ):
        raise ValueError(
            "ZION_VITE_MANIFEST_PATH must exist and be a folder. "
            f"Given: {settings.ZION_VITE_MANIFEST_PATH}"
        )

    manifest_dev_file = os.path.join(
        settings.ZION_VITE_MANIFEST_PATH, settings.ZION_VITE_MANIFEST_DEV_FILE
    )
    manifest_file = os.path.join(
        settings.ZION_VITE_MANIFEST_PATH, settings.ZION_VITE_MANIFEST_FILE
    )

    if os.path.exists(manifest_dev_file):
        with open(manifest_dev_file, "r") as f:
            manifest_dev = json.load(f)
        urls = {
            file: f"{manifest_dev['url']}{file}"
            for file in manifest_dev["inputs"].values()
        }
    elif os.path.exists(manifest_file):
        with open(manifest_file, "r") as f:
            manifest = json.load(f)
        urls = {
            file["src"]: f"{settings.ZION_VITE_URL_PATH}/{file['file']}"
            for file in manifest.values()
        }
    else:
        raise RuntimeError("Manifest files are not found!")

    return urls
