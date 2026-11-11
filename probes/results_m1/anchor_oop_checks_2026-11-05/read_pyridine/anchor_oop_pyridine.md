# TASKS 184 (a): pyridine's composite against CCSD(T)/cc-pVTZ out of plane

Corrected-ω rms (cm⁻¹) of the carried composite against the truth (composite with its out-of-plane block from CC/TZ):

| ring-ip | CH-stretch | CH-oop | other | all |
|---|---|---|---|---|
| 0.21 | 0.00 | 6.62 | 3.12 | 3.35 |

**Verdict (registered line, CH-oop): holds.** Rows' symmetry spread 5.4e-06 a.u.; composite's out-of-plane–in-plane coupling 9.4e-18 a.u.

CH-oop rms of truth − s·candidate on pyridine, s from the other ten anchors (descriptive, one molecule):

| candidate | against the composite | against CC/TZ |
|---|---|---|
| wb97x | 13.87 | 20.08 |
| mp2_dz | 9.93 | 16.36 |
| mp2_631gs | 8.15 | 14.28 |
