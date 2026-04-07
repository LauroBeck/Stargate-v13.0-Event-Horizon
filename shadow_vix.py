import matplotlib.pyplot as plt

def generate_visual_audit(brent, vix):
    # Calculate Shadow VIX Projection
    projection = vix * (brent / 110.0) ** 1.3
    
    # Generate Risk Chart
    plt.figure(figsize=(8, 4), facecolor='#0a0a0a')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')
    plt.bar(['Current VIX', 'Shadow VIX'], [vix, projection], color=['#00ff00', 'red'])
    plt.title(f"Volatility Expansion Model ($Brent: {brent})", color='white')
    plt.tick_params(colors='white')
    
    plt.savefig('vol_projection.png')
    print(f"[PYTHON 3.15] Shadow Projection: {projection:.2f} | Image: vol_projection.png")

if __name__ == "__main__":
    generate_visual_audit(144.0, 26.79)
