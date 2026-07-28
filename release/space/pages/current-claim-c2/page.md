# C2 — Hellinger and total variation

## Exact corollary

Corollary 2.4 has the same compact-support and `delta>0` quantifiers as C1 and asserts

`H(f_pi,f_eta) <= max(C0, t^(-alpha(t))) t`,

where `t=TV(f_pi,f_eta)` and `alpha(t)=(2+delta)/log(max(log(1/t),e))`. This is the precise `TV^(1-o(1))` bound: the exponent correction decays as `1/log log(1/t)`.

## Approach 1 — broad direct sweep

The exact Hellinger bound is evaluated—not the weaker generic inequality `H²<=TV`—on the same `60` compact-support families and `420` cells:

| Quantity | Result |
| --- | ---: |
| exact-bound violations | `0 / 420` |
| maximum `H / [max(1,t^-alpha(t))t]` | `0.00378670` |
| observed `H/TV` range | `0.7584` to `1.9101` |
| TV range | `1.15577e-7` to `4.75248e-2` |

The fact that `H/TV` exceeds one supplies a real negative control against replacing the logarithmic exponent with a constant-factor linear claim. Every cell is in the [raw CSV](../../evidence/raw/scaled_direct/claim_1_2_raw.csv).

On the independent eight-amplitude small-TV path, TV reaches `6.505e-12`,
`H/TV` stabilizes near `1.041566`, and
`H/TV^(1-alpha(TV))` decreases to `2.566e-9`. Thus the required normalized
quantity becomes smaller—not merely non-violating—as TV approaches zero.

## Approach 2 — direct d=2 and d=3 mixtures

The new tensor route directly integrates the full densities of product mixing
laws in `d=2` and `d=3`, seven amplitudes per dimension. All `14/14` exact
Corollary 2.4 cells pass with `C0=1`; the maximum normalized Hellinger ratio is
`0.000650306`. The higher-order checker agrees within `5.739e-4`, and the
independent Hellinger product-affinity identity agrees to `5.315e-16`.

## Approach 3 — universal pointwise reduction and proof-kernel replay

For symbolic positive densities `x,y`, the independent verifier simplifies

`((x-y)²/y) / (sqrt(x)-sqrt(y))²`

to `(sqrt(x/y)+1)²`, establishing the pointwise Hellinger/chi-square implication before integration. The doubled-grid checker agrees to maximum relative error `2.135e-6`. Controls reject both a missing square and `alpha(t)=0`; failures exit nonzero.

This implication quantifies over every positive density pair; combining it
with the C1 universal certificate gives the corollary for all dimensions and
all compactly supported Gaussian mixing laws. It is not inferred from the
finite 1D or tensor cells.

The current source-complete proof replay expands the full C1 route, then
checks the pointwise density identity exactly and carries the all-dimensional
quantifier to the conclusion. It reports **zero unresolved** internal
dependencies. `check_source_complete_proof_replay.py` independently rebuilds
the identity and rejects the missing-square mutation.

## Reproduce and evidence

```bash
uv sync --frozen && uv run python repro/src/run_publication_gate.py
```

Seed `260203214`; one effective numerical core; HF `cpu-upgrade` for the uncertain first run; no GPU.

- [Scaled verifier source](../../evidence/src/repro/src/run_scaled_direct_evidence.py)
- [Three-route verifier](../../evidence/src/repro/src/run_three_route_evidence.py)
- [Three-route matrix](../../evidence/raw/three_route/route_matrix.json)
- [d=2/d=3 raw cells](../../evidence/raw/three_route/multidimensional_direct.csv)
- [Three-route checker](../../evidence/raw/three_route/independent_checker.json)
- [Complete result](../../evidence/raw/scaled_direct/result.json)
- [Independent checker](../../evidence/raw/scaled_direct/independent_checker.json)
- [Negative controls](../../evidence/raw/scaled_direct/negative_control.json)
- [Exact universal verifier](../../evidence/src/repro/src/verify_universal_reductions.py)
- [Universal certificate](../../evidence/raw/universal_reductions/result.json)
- [Proof-kernel generator](../../evidence/src/repro/src/verify_kernel_certificate.py)
- [Independent proof replay](../../evidence/src/repro/src/check_kernel_certificate.py)
- [Kernel certificate](../../evidence/raw/kernel_certificate/proof_certificate.json)
- [Kernel replay output](../../evidence/raw/kernel_certificate/independent_checker.json)
- [Source-complete generator](../../evidence/src/repro/src/verify_source_complete_proof_replay.py)
- [Independent source-complete checker](../../evidence/src/repro/src/check_source_complete_proof_replay.py)
- [Current proof transcript](../../evidence/raw/source_complete_proof_replay/proof_transcript.md)
- [Current proof object](../../evidence/raw/source_complete_proof_replay/proof_replay.json)
- [Claim contract](../../evidence/raw/scaled_direct/claim_contract.json)
- [Source audit](../../evidence/raw/scaled_direct/source_audit.md)
- [Method](../../evidence/raw/scaled_direct/method.md)
- [Limitations](../../evidence/raw/scaled_direct/limitations.md)
