import base64
import os
from src.core import APP_ROOT


async def filter_obj(stmt, filter_data, model):
    filter_mapping = {}

    if not filter_data:
        return stmt

    for field in filter_data.__fields__:  # Iterate over the fields of the filter model
        value = getattr(filter_data, field)  # Get the value of the field
        if value is not None:
            if field == "name":
                filter_mapping[field] = model.name.ilike(f"%{value}%")
            else:
                filter_mapping[field] = getattr(model, field) == value
    # Apply filters
    for condition in filter_mapping.values():
        stmt = stmt.filter(condition)

    return stmt


async def base64_image_saver(img_folder: str, image_base64: base64, base_url: str, uuid: str):
    image_data = base64.b64decode(image_base64)

    file_name = f"{uuid}.png"
    file_path = APP_ROOT / f"media/{img_folder}/{file_name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(image_data)

    image_path = f"{base_url}media/{img_folder}/{file_name}"
    return image_path
