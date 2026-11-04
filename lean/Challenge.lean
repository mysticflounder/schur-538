/-
Copyright (c) 2026 Adam McKenna.
Released under the Creative Commons Attribution 4.0 International license
(CC-BY-4.0) as described in the file LICENSE.
Authors: Adam McKenna
-/
module

/-!
# Comparator challenge: a Schur 6-colouring of `[1, 538]`

This file imports Lean core only. It states the main theorem of `SchurSix538`
with `sorry`, so that a reader can read the claim here.

The statement: there is `c : Nat → Fin 6` such that no `x`, `y`, `x + y` in
`[1, 538]` have one colour, with `x = y` allowed. So `[1, 538]` is the union of
six sum-free sets, and `S(6) ≥ 538` for the Schur number `S(6)`.
-/

namespace SchurWitness538

/-- There is a colouring of the natural numbers with 6 colours such that no `x`,
`y`, `x + y` in `[1, 538]` have one colour. The case `x = y` is included. -/
public theorem schur_six_538 :
    ∃ c : Nat → Fin 6, ∀ x y : Nat, 1 ≤ x → 1 ≤ y → x + y ≤ 538 →
      ¬ (c x = c y ∧ c y = c (x + y)) := by
  sorry

end SchurWitness538
