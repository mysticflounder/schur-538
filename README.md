# A Schur 6-colouring of [1, 538]

A Lean 4 check of this statement: the integers 1 to 538 have a colouring with 6 colours and no monochromatic x + y = z, with x = y allowed. So S(6) ≥ 538, where S(k) is the largest n such that [1, n] has such a colouring with k colours.

```lean
theorem schur_six_538 :
    ∃ c : Nat → Fin 6, ∀ x y : Nat, 1 ≤ x → 1 ≤ y → x + y ≤ 538 →
      ¬ (c x = c y ∧ c y = c (x + y))
```

## Files

| File | Content |
|---|---|
| `lean/SchurSix538.lean` | The theorem and its proof. Imports Lean core only. |
| `schur6-538.word` | The colouring: letter i is the colour of the integer i. 538 letters and one final newline. |
| `schur6-538-b.word` | A second colouring in the same format. The Lean theorem does not use this word. |

## Check it

```sh
cd lean
lake build
```

The toolchain is in `lean/lean-toolchain` (Lean v4.33.1). The build prints the axioms of each theorem. For `schur_six_538` they are `propext`, `Classical.choice` and `Quot.sound`. The file has no `sorry` and no `native_decide`.

The numeral `word538` in the Lean file has the same digits as `schur6-538.word`. The workflow `.github/workflows/lean.yml` compares them.

## License

[CC BY 4.0](LICENSE).
