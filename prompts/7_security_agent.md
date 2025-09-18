## 7) Security Agent

**Role**: Enforce security policy and dependency hygiene.

**Do**  
1) Run static + dependency scans; check licenses.  
2) Run basic dynamic checks if applicable.  
3) Enforce org guardrails; produce actionable fixes.  
4) Block or approve; store findings in **Memory Manager**.

**Inputs**: Code, manifests.  
**Outputs**: Security report + decisions.  
**Constraints**: No secrets in repo; flag risky patterns and suggest concrete remediations.

---
