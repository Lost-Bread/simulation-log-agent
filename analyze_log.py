from pathlib import Path

project_folder = Path(__file__).parent
log_file = project_folder / "data" / "simulation_log.txt"
lines = log_file.read_text(encoding="utf-8").splitlines()

warnings = [line for line in lines if "WARNING" in line]
errors = [line for line in lines if "ERROR" in line]
status = "ERROR" if errors else "WARNING" if warnings else "NORMAL"

warning_text = "\n".join(f"- {line}" for line in warnings) or "None"
error_text = "\n".join(f"- {line}" for line in errors) or "None"

print("=== Simulation Log Report ===")
print(f"Overall status: {status}")
print(f"Log lines read: {len(lines)}")
print(f"\nWarnings found:\n{warning_text}")
print(f"\nErrors found:\n{error_text}")
