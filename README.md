# A Schur 6-colouring of [1, 538]

A paper and a Lean 4 check of this statement: the integers 1 to 538 have a colouring with 6 colours and no monochromatic x + y = z, with x = y allowed. So S(6) ≥ 538, where S(k) is the largest n such that [1, n] has such a colouring with k colours.

```lean
theorem schur_six_538 :
    ∃ c : Nat → Fin 6, ∀ x y : Nat, 1 ≤ x → 1 ≤ y → x + y ≤ 538 →
      ¬ (c x = c y ∧ c y = c (x + y))
```

To cite this work, use the DOI [10.5281/zenodo.23937655](https://doi.org/10.5281/zenodo.23937655) or `CITATION.cff`.

## Files

| File | Content |
|---|---|
| `paper/schur-six-538.pdf` | The paper. Its source is `paper/schur-six-538.md`; pandoc makes `paper/schur-six-538.tex` from it, and pdfLaTeX makes the PDF from the `.tex` file. |
| `lean/SchurSix538.lean` | The theorem and its proof. Imports Lean core only. |
| `lean/Challenge.lean` | The statement alone, with `sorry`, for the comparator. |
| `lean/comparator.json` | The comparator configuration. |
| `lean/formalization.yaml` | The metadata of the formalization. |
| `schur6-538.word` | The colouring: letter i is the colour of the integer i. 538 letters and one final newline. |
| `schur6-538-b.word` | A second colouring in the same format. The Lean theorem does not use this word. |
| `check_recursive_bounds.py` | Builds the partitions behind S(8) ≥ 5382, S(11) ≥ 204588 and S(13) ≥ 2045882 from the word, with the published templates, and checks them directly. |

## Check it

```sh
cd lean
lake build
```

The toolchain is in `lean/lean-toolchain` (Lean v4.35.0-rc3). The build prints the axioms of four theorems, among them `schur_six_538`. For `schur_six_538` they are `propext` and `Quot.sound`. The proof file has no `sorry` and no `native_decide`.

The numeral `word538` in the Lean file has the same digits as `schur6-538.word`. The workflow `.github/workflows/lean.yml` compares them.

To check the partitions of the bounds for S(8), S(11) and S(13), run `python3 check_recursive_bounds.py` in the repository root. It needs no packages.

## License

[CC BY 4.0](LICENSE).
