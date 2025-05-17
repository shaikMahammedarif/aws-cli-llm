import subprocess

def execute_aws_command(command):
    try:
        print(f"🟡 Running: {command}")
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"❌ Error: {e.stderr}"
