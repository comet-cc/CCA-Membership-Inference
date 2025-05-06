# CCA-Membership-Inference

This repository implements a **membership inference attack** (MIA) as part of the **artifact evaluation** for the paper:

> **An Early Experience with Confidential Computing Architecture for On-Device Model Protection**, , Sina Abdollahi, Mohammad Maheri, Sandra Siby, Marios Kogias, Hamed Haddadi --8th Workshop on System Software for Trusted Execution (SysTEX 2025)-- 
> [arXiv:2504.08508](https://arxiv.org/pdf/2504.08508) -- 

The attack code here builds on the base infrastructure provided in other projects and is used to assess information leakage in the context of **Arm CCA (Confidential Compute Architecture)** systems.

---

## 🔗 Related Repositories

### ▶️ Main Artifact Evaluation Infrastructure
This repository depends on core infrastructure implemented in:
- [**CCA-Evaluation**](https://github.com/comet-cc/CCA-Evaluation/tree/main)  
  Implements the main experiment framework, bootloader configuration, and Arm CCA software stack using Arm FVP and Shrinkwrap.

### 💡 Base Code Source
The MIA attack code is adapted from:
- [**TEESlice-artifact**](https://github.com/ziqi-zhang/TEESlice-artifact)  
  A prior work focusing on side-channel attacks on TEE systems.

---

## 🧪 Running the Experiments

To start the membership inference experiments, run:

```
./scripts/experiment.sh
```
