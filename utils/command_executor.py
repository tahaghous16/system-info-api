import subprocess


def run_command(command: list):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return {
            "success": True,
            "command": " ".join(command),
            "output": result.stdout.strip()
        }

    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "command": " ".join(command),
            "error": e.stderr.strip()
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }