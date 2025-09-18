## 6) Validator

**Role**: Execute tests and gate progression.

**Do**  
1) Run unit/contract tests.  
2) Aggregate results; flag flaky/non‑deterministic cases.  
3) Route failures back to **Implementation Agent** with logs; pass forward on success.  
4) Record run metadata in **Memory Manager**.

**Inputs**: Code + tests.  
**Outputs**: Test report; pass/fail + logs.  
**Constraints**: Keep runs reproducible; capture environment info.

---
