import Lake
open Lake DSL

package «goldbach-distributed-consciousness» where
  version := v!"1.0.0"
  keywords := #["mathematics", "number-theory", "goldbach", "distributed-consciousness"]
  description := "Goldbach Conjecture verification through Distributed Consciousness methodology"

lean_lib «GoldbachConjecture» where
  -- Main library containing our formalization

@[default_target]
lean_exe «goldbach» where
  root := `Main
  -- Executable for running verification

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

