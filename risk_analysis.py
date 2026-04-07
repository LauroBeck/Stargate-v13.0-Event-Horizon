import dataclasses

@dataclasses.dataclass(frozen=True)
class MarketState:
    ticker: str
    last: float
    vol: int

def run_telemetry():
    cvx = MarketState("CVX", 201.265, 8618520)
    print(f"[Python 3.15] Tracking {cvx.ticker} | Vol: {cvx.vol:,}")

if __name__ == "__main__":
    run_telemetry()
