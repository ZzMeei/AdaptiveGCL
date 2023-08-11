# AdaptiveGCL

## Update: Please go to https://github.com/HKUDS/AdaGCL to view the latest relevant source code and datasets of AdaGCL, this repository is no longer valid.

This is the PyTorch implementation for AdaptiveGCL proposed in the paper **Adaptive Graph Contrastive Learning for Recommendation**.

## 1. Running environment

We develop our codes in the following environment:

- python==3.9.13
- numpy==1.23.1
- torch==1.11.0
- scipy==1.9.1

## 2. Datasets

| Dataset      | # User | # Item | # Interaction | Interaction Density |
| ------------ | ------ | ------ | ------------- | ------------------- |
| Last.FM      | 1,892  | 17,632 | 92,834        | 2.8 × $10^{-3}$     |
| Yelp         | 42,712 | 26,822 | 182,357       | 1.6 × $10^{-4}$     |
| BeerAdvocate | 10,456 | 13,845 | 1,381,094     | 9.5 × $10^{-3}$     |

## 3. How to run the codes

- Last.FM

```python
python Main.py --data lastfm --eps 1e-3 --gamma -0.95
```

- Yelp

```python
python Main.py --data yelp --eps 1e-3 --ssl_reg 1 --ib_reg 1e-2
```

- BeerAdvocate

```python
python Main.py --data beer --ib_reg 1 --eps 1e-3 --lambda0 1e-2
```

