# Test-vs-train/validation similarity check

Descriptive check computed after scoring, not used for any selection. Test n=176; texts compared lower-cased. Token Jaccard uses word tokens (`\w+`). This measures surface similarity only; it is not proof that test scenarios are independent of training scenarios.

| reference split | n | pairs compared | exact duplicates | max SequenceMatcher ratio (test id, ref id) | pairs > 0.7 | pairs > 0.8 | max token Jaccard (test id, ref id) |
|---|---|---|---|---|---|---|---|
| train | 207 | 36432 | none | 0.69 (te-165 vs tr-087) | 0 | 0 | 0.50 (te-062 vs tr-079) |
| validation | 40 | 7040 | none | 0.68 (te-021 vs va-023) | 0 | 0 | 0.39 (te-054 vs va-016) |
| train + validation | 247 | 43472 | none | 0.69 (te-165 vs tr-087) | 0 | 0 | 0.50 (te-062 vs tr-079) |
