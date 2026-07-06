"""
Utility module.
Handles os utilities (right now just creating folders)
"""

from datetime import datetime
import os


def create_folder(runtime_parent_dir: str) -> str:
    """
    Args:
        runtime_parent_dir(str): the path of the parent directory to create the folder in
    Returns:
        A string which is the path of the created folder with the name
        'SDLsplit_%Y%m%d+%H%M%S'
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder = os.path.join(runtime_parent_dir, f"SDLsplit_{timestamp}")

    # makedirs 'creates' all parent folders in the path
    # exist_ok=True does not overwrite any existing folder. it is safe
    os.makedirs(output_folder, exist_ok=True)

    return output_folder
