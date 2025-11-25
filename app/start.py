import subprocess
import sys

# Run alembic migrations
print("Running Alembic migrations...")
subprocess.run(["alembic", "upgrade", "head"], check=True)

# Start Flask app
print("Starting Flask app...")
subprocess.run(["python", "app.py"])