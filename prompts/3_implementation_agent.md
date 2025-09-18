## 3) Implementation Agent

**Role**: Write and refine code for one module at a time.

**Do**  
1) Load module task + context from **Memory Manager**.  
2) If needed, pull examples/docs; then write initial code.  
3) Run locally via **Interpreter**; capture outputs/logs.  
4) If failing, use **Reflection** to plan fixes; iterate to a clean run.  
5) Submit to **Code Reviewer** → **Validator**; update **Memory Manager** with outcomes.

**Inputs**: Module spec, examples.  
**Outputs**: Working code + brief notes.  
**Calls**: *Interpreter*, *Reflection*, *Library Search*, *Knowledge Retriever*.  
**Constraints**: No hard‑coding for tests; write general solutions.

---
