# PI Security ~10K Stress-Test Repository

**QA fixture only.** This repository intentionally contains insecure patterns. Do not deploy it or expose it to the internet.

## Contents
- `app/sample_service.py`: representative Python security issues.
- `security_fixtures/`: 1,000 generated Python files with 10 candidate insecure locations each.
- `scripts/generate_fixtures.py`: reproducibly generates the corpus.
- `tests/`: minimal repository smoke test.

## Generate
```bash
python3 scripts/generate_fixtures.py
```
This creates 10,000 *candidate locations*, not guaranteed scanner findings. PI Security may detect fewer, deduplicate, or group them.

## QA workflow
1. Create a new GitHub repository and push this project.
2. Onboard it in staging and run the first Security scan.
3. Record actual findings, remediation count, and scan duration.
4. Push a harmless change to `app/README_marker.txt` on the same branch.
5. Trigger the next scan. Verify it completes, every finding is under a remediation, and existing groups are retained.
6. Record the second scan duration.
