#!/usr/bin/env python3
"""Generate 10,000 candidate insecure source locations. Do not deploy output."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "security_fixtures"
FILES = 1000

def patterns(i):
    return [
        f'password_{i} = "test-password-{i}"  # hard-coded credential candidate\n',
        f'query_{i} = "SELECT * FROM accounts WHERE id = " + str(user_id_{i})  # SQL injection candidate\n',
        f'command_{i} = "echo " + str(user_input_{i})  # command construction candidate\n',
        f'__import__("subprocess").run(command_{i}, shell=True)  # shell=True candidate\n',
        f'weak_hash_{i} = __import__("hashlib").md5(str(value_{i}).encode()).hexdigest()  # weak hash candidate\n',
        f'token_{i} = str(__import__("random").randint(100000, 999999))  # predictable token candidate\n',
        f'data_{i} = __import__("pickle").loads(serialized_{i})  # unsafe deserialization candidate\n',
        f'config_{i} = __import__("yaml").load(yaml_text_{i}, Loader=__import__("yaml").Loader)  # unsafe YAML candidate\n',
        f'path_{i} = "/tmp/" + str(user_file_{i})  # temp path candidate\n',
        f'assert "{i}" == str(input_{i})  # assertion validation candidate\n',
    ]

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for old in ROOT.glob("fixture_*.py"):
        old.unlink()
    for file_index in range(FILES):
        lines = ['"""Generated insecure scanner-QA fixture. Do not deploy."""\n']
        for j, line in enumerate(patterns(file_index * 10)):
            lines.append(line)
        (ROOT / f"fixture_{file_index:04d}.py").write_text("".join(lines))
    print(f"Generated {FILES} files and {FILES * 10} candidate locations.")

if __name__ == "__main__":
    main()
