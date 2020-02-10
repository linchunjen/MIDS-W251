# Homework 6_Curtis Lin

## Summary of HW6

### 1.Runtime: 

#### A. Model training
> Epoch = 1:
- V100: 1h 52min 22s 
- P100: 6h 4min 30s

> Epoch = 2: 
- V100: 3h 54min 6s
- P100: 12h 14min 41s

#### B. Model validation

> Epoch = 1:
- V100: 15min 50s
- P100: 1h 45s

> Epoch = 2: 
- V100: 15min 55s
- P100: 1h 46s

### 2. AUC score (SEED = 1234)

> Epoch = 1:
- V100: 0.96990
- P100: 0.97000

> Epoch = 2: 
- V100: 0.45412
- P100: 0.45413

### 3. Conclusion 

- V100 has better training performance in the comparison to P100. The runtime of model training with V100 is ~3x faster than it of P100. The runtime of model validation with V100 is ~7x faster than it of P100.
- With 1 epoch, the AUC score of V100 and P100 showed good improvement in the comparison of AUC score in HW4.
- With 2 epoch, the training model was overfitted. Therefore, the AUC score with 2 epochs was decreased.    


