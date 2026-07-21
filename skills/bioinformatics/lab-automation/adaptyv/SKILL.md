---
name: adaptyv
description: "How to use the Adaptyv Bio Foundry API and Python SDK for protein experiment design, submission, and results retrieval. Use whenever the user mentions Adaptyv, Foundry API, protein binding assays, protein screening experiments, BLI/SPR assays, thermostability assays, or wants to submit protein sequences for experimental characterization."
---

# Adaptyv Bio Foundry API

Adaptyv Bio is a cloud lab that turns protein sequences into experimental data. Users submit amino acid sequences via API or UI; Adaptyv's automated lab runs assays (binding, thermostability, expression, fluorescence) and delivers results in ~21 days.

## Quick Start

**Base URL:** `https://foundry-api-public.adaptyvbio.com/api/v1`
**Authentication:** Bearer token in the `Authorization` header.

```bash
export FOUNDRY_API_TOKEN="abs0_..."
curl https://foundry-api-public.adaptyvbio.com/api/v1/targets?limit=3 \
  -H "Authorization: Bearer $FOUNDRY_API_TOKEN"
```

Store tokens in environment variables or `.env` files — never commit them to source control.

## Python SDK

Install: `pip install adaptyv-sdk`

**Environment variables:**
```bash
ADAPTYV_API_KEY=your_api_key
ADAPTYV_API_URL=https://foundry-api-public.adaptyvbio.com/api/v1
```

### Decorator Pattern

```python
from adaptyv import lab

@lab.experiment(target="PD-L1", experiment_type="screening", method="bli")
def design_binders():
    return {"design_a": "MVKVGVNG...", "design_b": "MKVLVAG..."}

result = design_binders()
print(f"Experiment: {result.experiment_url}")
```

### Client Pattern

```python
from adaptyv import FoundryClient

client = FoundryClient(api_key="...", base_url="https://foundry-api-public.adaptyvbio.com/api/v1")

targets = client.targets.list(search="EGFR", selfservice_only=True)
estimate = client.experiments.cost_estimate({...})
exp = client.experiments.create({...})
client.experiments.submit(exp.experiment_id)
results = client.experiments.get_results(exp.experiment_id)
```

## Experiment Types

| Type | Method | Measures | Requires Target |
|---|---|---|---|
| affinity | bli or spr | KD, kon, koff kinetics | Yes |
| screening | bli or spr | Yes/no binding | Yes |
| thermostability | — | Melting temperature (Tm) | No |
| expression | — | Expression yield | No |
| fluorescence | — | Fluorescence intensity | No |

## Experiment Lifecycle

Draft → WaitingForConfirmation → QuoteSent → WaitingForMaterials → InQueue → InProduction → DataAnalysis → InReview → Done

## Error Handling

All errors return:
```json
{
  "error": "Human-readable description",
  "request_id": "req_xxx"
}
```

Include `request_id` when contacting support.
