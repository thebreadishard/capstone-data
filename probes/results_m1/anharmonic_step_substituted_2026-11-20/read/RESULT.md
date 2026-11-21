# The anharmonic step against its label — one substituted molecule

Registration: `GoalGathering/notes/PreRegistration_2026-11-20_Anharmonic_Step_Substituted_Molecule.md`, part B. Run `probes/results_m1/pipeline_benzonitrile_anharmonic_v3_2026-11-19/benzonitrile`; label `probes/results_m1/anharmonic_step_substituted_2026-11-20/g_label/gvpt2_g/benzonitrile.json` (geometry 0.0005 bohr rms from the run's after rotation).

**Outcome: beyond the bar.** At least one family is beyond its bar on this molecule: evidence that the bar understates the step's error here. The default does not change by this run; the certificate's sentence about what the bars rest on gains the measured number for a substituted molecule; and the question whether the bars need a substituted target goes to the author with that number (a new target is label compute). No bar changes.

| family | bands under the bar | rms of step − label (cm⁻¹) | printed bar (cm⁻¹) | 95 % line at this n (cm⁻¹) | statement | every stepped band: n, rms |
|---|---|---|---|---|---|---|
| CH-oop | 6 | 3.79 | 8.38 | 12.14 | within the bar | 6, 3.79 |
| other | 3 | 3.91 | 3.84 | — | no statement | 4, 3.70 |
| ring-ip | 12 | 4.43 | 3.37 | 4.46 | consistent with the bar at this n | 12, 4.43 |
| CH-stretch | 5 | 17.76 | 6.21 | 9.24 | beyond the bar | 5, 17.76 |

The statement is read on the bands printed with a step and the family's bar, at least 4 of them; the rms is compared as printed, to 2 decimals. The line is the rms that n independent errors with the bar as their standard deviation stay under 95% of the time; with three families judged, about one run in seven shows a 'beyond' when every bar is right, and errors within a molecule are not independent, so the line is approximate and, if anything, too narrow. One molecule cannot establish a bar. The printed steps are the record's, rounded to 0.1 cm⁻¹.

## Bands printed harmonic, and what the label says for them

| ω (cm⁻¹) | why no step | label Δ (cm⁻¹) | label outside VPT2's domain |
|---|---|---|---|
| 167.5 | unmeasured | -1.2 | no |
| 189.7 | unmeasured | 2.1 | no |
| 410.9 | unmeasured | -7.0 | no |
| 422.0 | unmeasured | -6.8 | no |
| 467.9 | unmeasured | -4.8 | no |
| 2386.3 | unmeasured | -34.0 | no |

## Bands whose printed family differs from the label mode's

None.

## Every band

| ω (cm⁻¹) | family | step Δ | label Δ | step − label | label ω | overlap | outside the rms because |
|---|---|---|---|---|---|---|---|
| 167.5 | other | — | -1.2 | — | 147.3 | 0.997 | no step: unmeasured |
| 189.7 | other | — | 2.1 | — | 164.5 | 0.997 | no step: unmeasured |
| 410.9 | other | — | -7.0 | — | 392.6 | 0.997 | no step: unmeasured |
| 422.0 | other | — | -6.8 | — | 411.0 | 0.999 | no step: unmeasured |
| 467.9 | other | — | -4.8 | — | 465.9 | 1.000 | no step: unmeasured |
| 576.1 | other | -5.0 | -2.9 | -2.1 | 559.9 | 0.994 |  |
| 582.4 | other | -8.3 | -11.3 | 3.0 | 572.7 | 0.997 | stepped without the family's bar (its error is not measured) |
| 643.8 | other | -6.4 | -5.2 | -1.2 | 638.0 | 0.996 |  |
| 716.6 | CH-oop | -10.7 | -10.3 | -0.4 | 704.4 | 0.996 |  |
| 782.1 | other | -8.6 | -14.9 | 6.3 | 774.7 | 1.000 |  |
| 792.9 | CH-oop | -12.5 | -12.7 | 0.2 | 778.8 | 0.997 |  |
| 879.5 | CH-oop | -8.8 | -14.7 | 5.9 | 861.8 | 1.000 |  |
| 965.5 | CH-oop | -10.3 | -14.1 | 3.8 | 942.0 | 0.998 |  |
| 1007.1 | CH-oop | -11.9 | -6.3 | -5.6 | 976.8 | 1.000 |  |
| 1025.8 | ring-ip | -14.9 | -13.1 | -1.8 | 1017.5 | 0.998 |  |
| 1036.0 | CH-oop | -13.7 | -16.0 | 2.3 | 1008.0 | 0.997 |  |
| 1065.6 | ring-ip | -17.1 | -17.7 | 0.6 | 1056.0 | 0.998 |  |
| 1120.8 | ring-ip | -16.0 | -28.4 | 12.4 | 1112.9 | 0.996 |  |
| 1190.7 | ring-ip | -12.7 | -11.3 | -1.4 | 1197.1 | 0.974 |  |
| 1215.1 | ring-ip | -16.1 | -16.1 | -0.0 | 1211.5 | 0.958 |  |
| 1247.0 | ring-ip | -20.3 | -22.8 | 2.5 | 1227.7 | 0.957 |  |
| 1307.2 | ring-ip | -25.7 | -31.7 | 6.0 | 1339.5 | 0.859 |  |
| 1364.6 | ring-ip | -25.1 | -19.7 | -5.4 | 1368.1 | 0.879 |  |
| 1504.6 | ring-ip | -28.7 | -27.9 | -0.8 | 1492.3 | 0.997 |  |
| 1555.2 | ring-ip | -31.0 | -32.2 | 1.2 | 1541.1 | 0.998 |  |
| 1665.7 | ring-ip | -38.3 | -37.6 | -0.7 | 1633.6 | 0.999 |  |
| 1698.3 | ring-ip | -38.4 | -40.1 | 1.7 | 1660.4 | 0.999 |  |
| 2386.3 | other | — | -34.0 | — | 2345.9 | 1.000 | no step: unmeasured |
| 3233.8 | CH-stretch | -146.3 | -172.8 | 26.5 | 3194.4 | 0.997 |  |
| 3245.2 | CH-stretch | -134.5 | -127.4 | -7.1 | 3204.7 | 0.998 |  |
| 3252.3 | CH-stretch | -135.1 | -148.4 | 13.3 | 3213.3 | 0.998 |  |
| 3262.1 | CH-stretch | -121.8 | -147.1 | 25.3 | 3222.9 | 0.998 |  |
| 3264.8 | CH-stretch | -138.5 | -140.3 | 1.8 | 3225.7 | 0.998 |  |
