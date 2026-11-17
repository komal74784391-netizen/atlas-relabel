"""Budget accounting for annotation rounds."""


class BudgetLedger:
    def __init__(self, total: int):
        self.total = total
        self.spent = 0

    def charge(self, labels: int) -> None:
        if self.spent + labels > self.total:
            raise ValueError("budget exceeded")
        self.spent += labels
