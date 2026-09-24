"""
Master Class 4 — The Java Bridge
Topic: Dataclasses vs. POJOs / Lombok

Run me directly:  python 09_dataclasses.py
"""

from dataclasses import dataclass, field


@dataclass
class TrainConfig:
    epochs: int
    lr: float = 0.01
    name: str = "run"
    tags: list = field(default_factory=list)   # safe way to default a mutable field


cfg = TrainConfig(epochs=10)
print(cfg)                          # __repr__ auto-generated
print("epochs:", cfg.epochs, "| lr:", cfg.lr)

cfg2 = TrainConfig(epochs=10)
print("cfg == cfg2:", cfg == cfg2)  # __eq__ auto-generated, compares field-by-field

cfg3 = TrainConfig(epochs=20, lr=0.05, name="experiment-1", tags=["baseline"])
print(cfg3)


# --- Without @dataclass, you'd hand-write all of this yourself ---
class TrainConfigManual:
    def __init__(self, epochs, lr=0.01, name="run"):
        self.epochs = epochs
        self.lr = lr
        self.name = name

    def __repr__(self):
        return f"TrainConfigManual(epochs={self.epochs}, lr={self.lr}, name={self.name!r})"

    def __eq__(self, other):
        if not isinstance(other, TrainConfigManual):
            return NotImplemented
        return (self.epochs, self.lr, self.name) == (other.epochs, other.lr, other.name)


manual = TrainConfigManual(10)
print("\nHand-written equivalent:", manual)


if __name__ == "__main__":
    print("\n--- Live demo talking points ---")
    print("Show TrainConfig's auto-generated __repr__ and __eq__ working for free,")
    print("then show TrainConfigManual doing the exact same thing by hand — this")
    print("is the boilerplate @dataclass (and Lombok's @Data in Java) save you.")
