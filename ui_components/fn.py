import os, platform

def get_data_storage_path() -> str:
        current_system = platform.system()
        if current_system == 'Windows':
            storage_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Ta-Do')
        elif current_system == 'Linux':
            storage_path = os.path.join(os.environ['HOME'], '.local', 'share', 'Ta-Do')
        elif current_system == 'Darwin':  # mac os
            storage_path = os.path.join(os.environ['HOME'], 'Library', 'Ta-Do')
        return storage_path
