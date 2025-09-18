# SLATE – Unified Agent Assets

The SLATE agent collective now separates **operational prompts** from the underlying **agent descriptions**. Use this document as the index for locating the latest guidance.

## Directory Layout
- `prompts/main_agents/` – assets for primary agents that own end-to-end workflow stages.
- `prompts/sub_agents/` – assets for supportive sub-agents that handle targeted tasks.
- Each agent directory contains two markdown files:
  - `*_description.md` – role overview, responsibilities, and collaboration context (legacy prompt content).
  - `*_prompt.md` – enhanced operational prompt designed for direct use as a system message.

## Main Agents
| # | Agent | Description File | Operational Prompt |
|---|-------|------------------|--------------------|
| 1 | Requirement Analyst | [`prompts/main_agents/1_requirement_analyst_description.md`](prompts/main_agents/1_requirement_analyst_description.md) | [`prompts/main_agents/1_requirement_analyst_prompt.md`](prompts/main_agents/1_requirement_analyst_prompt.md) |
| 2 | System Architect | [`prompts/main_agents/2_system_architect_description.md`](prompts/main_agents/2_system_architect_description.md) | [`prompts/main_agents/2_system_architect_prompt.md`](prompts/main_agents/2_system_architect_prompt.md) |
| 3 | Implementation Agent | [`prompts/main_agents/3_implementation_agent_description.md`](prompts/main_agents/3_implementation_agent_description.md) | [`prompts/main_agents/3_implementation_agent_prompt.md`](prompts/main_agents/3_implementation_agent_prompt.md) |
| 4 | Quality Assurance Agent | [`prompts/main_agents/4_quality_assurance_agent_description.md`](prompts/main_agents/4_quality_assurance_agent_description.md) | [`prompts/main_agents/4_quality_assurance_agent_prompt.md`](prompts/main_agents/4_quality_assurance_agent_prompt.md) |
| 5 | Code Reviewer | [`prompts/main_agents/5_code_reviewer_description.md`](prompts/main_agents/5_code_reviewer_description.md) | [`prompts/main_agents/5_code_reviewer_prompt.md`](prompts/main_agents/5_code_reviewer_prompt.md) |
| 6 | Validator | [`prompts/main_agents/6_validator_description.md`](prompts/main_agents/6_validator_description.md) | [`prompts/main_agents/6_validator_prompt.md`](prompts/main_agents/6_validator_prompt.md) |
| 7 | Security Agent | [`prompts/main_agents/7_security_agent_description.md`](prompts/main_agents/7_security_agent_description.md) | [`prompts/main_agents/7_security_agent_prompt.md`](prompts/main_agents/7_security_agent_prompt.md) |
| 8 | Documentation Agent | [`prompts/main_agents/8_documentation_agent_description.md`](prompts/main_agents/8_documentation_agent_description.md) | [`prompts/main_agents/8_documentation_agent_prompt.md`](prompts/main_agents/8_documentation_agent_prompt.md) |
| 9 | Deployment Orchestrator | [`prompts/main_agents/9_deployment_orchestrator_description.md`](prompts/main_agents/9_deployment_orchestrator_description.md) | [`prompts/main_agents/9_deployment_orchestrator_prompt.md`](prompts/main_agents/9_deployment_orchestrator_prompt.md) |
| 10 | Memory Manager | [`prompts/main_agents/10_memory_manager_description.md`](prompts/main_agents/10_memory_manager_description.md) | [`prompts/main_agents/10_memory_manager_prompt.md`](prompts/main_agents/10_memory_manager_prompt.md) |
| 11 | Knowledge Retriever | [`prompts/main_agents/11_knowledge_retriever_description.md`](prompts/main_agents/11_knowledge_retriever_description.md) | [`prompts/main_agents/11_knowledge_retriever_prompt.md`](prompts/main_agents/11_knowledge_retriever_prompt.md) |

## Sub-Agents
| # | Sub-Agent | Description File | Operational Prompt |
|---|-----------|------------------|--------------------|
| 12 | Clarifying Questions | [`prompts/sub_agents/12_clarifying_questions_sub_description.md`](prompts/sub_agents/12_clarifying_questions_sub_description.md) | [`prompts/sub_agents/12_clarifying_questions_sub_prompt.md`](prompts/sub_agents/12_clarifying_questions_sub_prompt.md) |
| 13 | Web Search | [`prompts/sub_agents/13_web_search_sub_description.md`](prompts/sub_agents/13_web_search_sub_description.md) | [`prompts/sub_agents/13_web_search_sub_prompt.md`](prompts/sub_agents/13_web_search_sub_prompt.md) |
| 14 | Internal Search | [`prompts/sub_agents/14_internal_search_sub_description.md`](prompts/sub_agents/14_internal_search_sub_description.md) | [`prompts/sub_agents/14_internal_search_sub_prompt.md`](prompts/sub_agents/14_internal_search_sub_prompt.md) |
| 15 | Document Retrieval | [`prompts/sub_agents/15_document_retrieval_sub_description.md`](prompts/sub_agents/15_document_retrieval_sub_description.md) | [`prompts/sub_agents/15_document_retrieval_sub_prompt.md`](prompts/sub_agents/15_document_retrieval_sub_prompt.md) |
| 16 | Summarization | [`prompts/sub_agents/16_summarization_sub_description.md`](prompts/sub_agents/16_summarization_sub_description.md) | [`prompts/sub_agents/16_summarization_sub_prompt.md`](prompts/sub_agents/16_summarization_sub_prompt.md) |
| 17 | Interpreter | [`prompts/sub_agents/17_interpreter_sub_description.md`](prompts/sub_agents/17_interpreter_sub_description.md) | [`prompts/sub_agents/17_interpreter_sub_prompt.md`](prompts/sub_agents/17_interpreter_sub_prompt.md) |
| 18 | Reflection | [`prompts/sub_agents/18_reflection_sub_description.md`](prompts/sub_agents/18_reflection_sub_description.md) | [`prompts/sub_agents/18_reflection_sub_prompt.md`](prompts/sub_agents/18_reflection_sub_prompt.md) |
| 19 | Library Search | [`prompts/sub_agents/19_library_search_sub_description.md`](prompts/sub_agents/19_library_search_sub_description.md) | [`prompts/sub_agents/19_library_search_sub_prompt.md`](prompts/sub_agents/19_library_search_sub_prompt.md) |
| 20 | Static Analysis | [`prompts/sub_agents/20_static_analysis_sub_description.md`](prompts/sub_agents/20_static_analysis_sub_description.md) | [`prompts/sub_agents/20_static_analysis_sub_prompt.md`](prompts/sub_agents/20_static_analysis_sub_prompt.md) |
| 21 | Vulnerability Scanner | [`prompts/sub_agents/21_vulnerability_scanner_sub_description.md`](prompts/sub_agents/21_vulnerability_scanner_sub_description.md) | [`prompts/sub_agents/21_vulnerability_scanner_sub_prompt.md`](prompts/sub_agents/21_vulnerability_scanner_sub_prompt.md) |
| 22 | Relevance Filter | [`prompts/sub_agents/22_relevance_filter_sub_description.md`](prompts/sub_agents/22_relevance_filter_sub_description.md) | [`prompts/sub_agents/22_relevance_filter_sub_prompt.md`](prompts/sub_agents/22_relevance_filter_sub_prompt.md) |

## Usage Tips
- **Start with the description** when onboarding a new agent or revisiting responsibilities.
- **Load the operational prompt** verbatim into the agent’s system prompt or configuration.
- **Coordinate via Memory Manager** so that decisions and updates remain discoverable across the workflow.
- **Leverage sub-agents on demand** to unblock research, execution, and analysis tasks without overwhelming main agents.

For historical context or previous versions of the prompts, refer to the git history of the description files.
