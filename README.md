# genpark-hamming-secded-error-correction-code-skill

Agent Skill implementing **Hamming (7, 4) linear block coding and Extended SECDED (8, 4)** for single error correction and double error detection.

## Architectural Overview
```mermaid
flowchart TD
    Data["4-bit Data Vector"] --> Parity["Compute 3 Parity Bits (Hamming 7,4)"]
    Parity --> Ext["Add 8th Overall Parity Bit (SECDED)"]
    Ext --> Channel["Transmission Channel (Noise / Bit Flips)"]
    Channel --> Syn["Compute 3-bit Syndrome + Overall Parity Check"]
    Syn --> Decision{"Error State"}
    Decision -- "Syn=0, P=OK" --> Valid["No Error"]
    Decision -- "Syn!=0, P=Fail" --> Single["Single Error Corrected"]
    Decision -- "Syn!=0, P=OK" --> Double["Double Error Detected (Uncorrectable)"]
```
