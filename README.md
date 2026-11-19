# Companion materials for *Foundations of Sensitivity Analysis*

Companion code for ***Foundations of Sensitivity Analysis: From Local to Global
Sensitivity*** by Leon M. Arriola and James M. Hyman. In preparation for submission to the SIAM
*Computational Science and Engineering* series. The book has not been submitted, is not under
review, and has not been accepted for publication.

This repository replaces `machyman/arriola2026sa`. The code here was carried over from that repository
at commit `1d3528d` and matches manuscript version v1_28_0.

---

## What is here

**Nine Python notebooks**, one per chapter. Each recomputes examples from its chapter and asserts
selected results against fresh computation rather than merely printing them. Each runs end to end in
Google Colab with no local installation and no data files. Click a badge to open one directly.

| Chapter | Notebook | Run it |
|---|---|---|
| 1. Introduction and Overview | [`ch01_intro.ipynb`](software/python/ch01_intro.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch01_intro.ipynb) |
| 2. Measuring Local Sensitivity | [`ch02_local_sa.ipynb`](software/python/ch02_local_sa.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch02_local_sa.ipynb) |
| 3. Computing Sensitivity in Practice | [`ch03_computing.ipynb`](software/python/ch03_computing.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch03_computing.ipynb) |
| 4. Analytic Forward Sensitivity Analysis | [`ch04_analytic_forward_sensitivity_analysis.ipynb`](software/python/ch04_analytic_forward_sensitivity_analysis.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch04_analytic_forward_sensitivity_analysis.ipynb) |
| 5. The Adjoint in Linear Algebra | [`ch05_the_adjoint_in_linear_algebra.ipynb`](software/python/ch05_the_adjoint_in_linear_algebra.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch05_the_adjoint_in_linear_algebra.ipynb) |
| 6. The Adjoint for Dynamical Systems | [`ch06_adjoint_odes.ipynb`](software/python/ch06_adjoint_odes.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch06_adjoint_odes.ipynb) |
| 7. Adjoint Sensitivity in Practice | [`ch07_adjoint_practice.ipynb`](software/python/ch07_adjoint_practice.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch07_adjoint_practice.ipynb) |
| 8. Caveat Emptor, Limitations of Local Sensitivity Analysis | [`ch08_caveat_emptor.ipynb`](software/python/ch08_caveat_emptor.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch08_caveat_emptor.ipynb) |
| 9. Global Sensitivity Analysis and Sobol Indices | [`ch09_global_sa.ipynb`](software/python/ch09_global_sa.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/arriola2027sensitivity/blob/main/software/python/ch09_global_sa.ipynb) |

**The MATLAB reference library**, eighteen functions across four modules, with an automated test
suite. Each function corresponds directly to a concept or algorithm in the text.

| Module | Contents |
|---|---|
| [`software/matlab/core`](software/matlab/core) | the sensitivity index, the Jacobian, the SIR model and its nominal parameters, tornado plots |
| [`software/matlab/fse`](software/matlab/fse) | the augmented forward sensitivity system, its Jacobian, time-dependent indices |
| [`software/matlab/adjoint`](software/matlab/adjoint) | the SIR adjoint right-hand side and the adjoint solve |
| [`software/matlab/globalsa`](software/matlab/globalsa) | LHS, PRCC, Saltelli sampling, the Jansen estimator, Morris screening |

Automated tests are in [`software/matlab/tests`](software/matlab/tests). Changes are recorded in
[`CHANGELOG.md`](CHANGELOG.md).

**Worked solutions are not posted here.** A student study guide, with hints, check values, and a
follow-up question for each exercise, is in preparation. [MAC: say how instructors obtain solutions,
once that channel is settled.]

---

## Running the notebooks

Click any **Open in Colab** badge above. Nothing is installed locally and no account setup is
needed beyond a Google login.

Run the cells **in order**. Several notebooks build state across cells. For example,
`ch06_adjoint_odes.ipynb` computes the forward solve, the backward adjoint solve, and the
sensitivity integrals in successive cells, and the later verification and figure cells depend on
those results.

Dependencies are `numpy`, `scipy`, and `matplotlib`, all preinstalled in Colab.

## What the checks cover

Each notebook ends with assertions rather than printed output alone. Some check structural
identities that hold independently of solver tolerances. In `ch06`, for instance, the normalized
indices for the contact rate `c` and the transmission probability `β` must be equal, since the two
enter the model only through the product `cβ`. Others check numbers the book prints, at the
precision it prints them.

A notebook that runs to completion has passed its own assertions. That does not mean every number
quoted in its chapter has been checked; the assertions cover selected results.

---

## Citation

GitHub renders a **Cite this repository** button from `CITATION.cff`, in the sidebar on the
repository home page.

> Arriola, L. M. and Hyman, J. M. (2026). *Foundations of Sensitivity Analysis: From Local
> to Global Sensitivity*. Manuscript in preparation.
> https://github.com/machyman/arriola2027sensitivity

```bibtex
@unpublished{arriola2026foundations,
  author = {Arriola, Leon M. and Hyman, James M.},
  title  = {Foundations of Sensitivity Analysis: From Local to Global
            Sensitivity},
  note   = {Manuscript in preparation for submission to SIAM
            (Computational Science and Engineering series). Not submitted,
            not under review, not accepted. Details subject to change.},
  year   = {2026}
}
```

## Use of AI tools

Generative AI tools were used in preparing the book and these materials, including in writing and
testing the companion code and in checking numerical results against independent computation. The
book's Preface carries the full declaration and the verification that assistance was subject to.

## For maintainers: no solutions in this repository

Everything pushed to a public repository stays in its history, even after the file is deleted. Keep
worked solutions in a separate private repository, never in the folder this one is built from.
`tools/check_no_solutions.py` scans the repository for solution files and solution markup; the
workflow in `.github/workflows/no_solutions_check.yml` runs it on every push. It raises an alarm
after a push. It cannot stop one.

## License

Code in this repository is released under the MIT License. The text of the book and of any study
guide or solutions is not covered by that license; all rights in the text are reserved by the authors.
The book is in preparation for submission to SIAM and no publishing agreement is in place.

---

*Leon Arriola died before this book was finished. The work is his as much as anyone's.*
