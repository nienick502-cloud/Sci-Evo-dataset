"""
reasoning_formatter.py - Trajectory temporal reordering for Reasoning Chain

Reorders the final trajectory from:
  prediction + paper_derivation + decision_summary
To:
  prediction (blind guess) -> decision_summary (reflection) -> paper_derivation (ground truth)

This creates a "try -> fail -> reflect -> correct answer" learning trajectory.
"""


class ReasoningFormatter:
    """Reorders and renumbers trajectory segments for learning-optimal output."""

    def format(
        self,
        prediction: list[dict],
        decision_summary: list[dict],
        paper_derivation: list[dict],
    ) -> list[dict]:
        """
        Reorder trajectory: prediction -> decision_summary -> paper_derivation.
        Renumber step_index sequentially from 1.

        Args:
            prediction: Steps from blind prediction phase
            decision_summary: Steps from error reflection phase
            paper_derivation: Steps from paper ground truth extraction

        Returns:
            Merged, renumbered trajectory list
        """
        merged = []
        merged.extend(prediction)
        merged.extend(decision_summary)
        merged.extend(paper_derivation)

        # Renumber step_index sequentially
        for i, step in enumerate(merged, start=1):
            step["step_index"] = i

        return merged
