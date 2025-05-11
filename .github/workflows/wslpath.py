import sys
import os


def windows_to_wsl_path(windows_path):
    """
    Convert a Windows path to a WSL path.

    :param windows_path: The Windows path to be converted.
    :return: The converted WSL path.
    """
    if ':' in windows_path:
        drive, rest = windows_path.split(':', 1)
        result = f"/mnt/{drive.lower()}/{rest.replace('\\\\', '/')}"
        return result
    else:
        raise ValueError("Invalid Windows path format")


if __name__ == "__main__":
    runner_temp_path = os.environ.get('RUNNER_TEMP', '/tmp')
    wsl_path = windows_to_wsl_path(runner_temp_path)
    print("wsl_path:", wsl_path)
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as f:
        f.write(f"wsl_path={wsl_path}")
    sys.exit(0)


