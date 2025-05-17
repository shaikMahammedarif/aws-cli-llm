import subprocess
import os

def execute_aws_command(command):
    # Use the current environment's PATH so subprocess can find aws
    env = os.environ.copy()
    try:
        print(f"🟡 Running: {command}")
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                env=env)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"❌ Error: {e.stderr}"
