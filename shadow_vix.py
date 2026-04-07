def calculate_risk_regime(brent, vix):
    # Modeling non-linear VIX expansion relative to Brent record peak
    shadow_projection = vix * (brent / 110.0) ** 1.3
    print(f"[PYTHON 3.15] Projected Shadow VIX: {shadow_projection:.2f}")
    if shadow_projection > 30:
        print(">> REGIME: CRITICAL STRESS.")

if __name__ == "__main__":
    calculate_risk_regime(144.0, 26.79)
