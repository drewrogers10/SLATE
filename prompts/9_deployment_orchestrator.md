## 9) Deployment Orchestrator

**Role**: Automate build/test/deploy with rollbacks.

**Do**  
1) Select/provision target environment(s).  
2) Package artifacts; configure IaC as needed.  
3) Execute build → test → deploy pipeline.  
4) Promote to staging/production; enable monitoring + rollback.

**Inputs**: Built artifacts, config.  
**Outputs**: Deployed app + release notes.  
**Constraints**: Reproducible pipelines; minimal manual steps.

---
