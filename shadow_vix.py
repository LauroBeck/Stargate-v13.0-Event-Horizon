import matplotlib.pyplot as plt

def sync_assets(brent, vix):
    projection = vix * (brent / 110.0) ** 1.3
    plt.figure(figsize=(8, 4), facecolor='#0a0a0a')
    plt.bar(['Current', 'Shadow'], [vix, projection], color=['gray', 'red'])
    plt.title(f"Vol Projection ($Brent: {brent})", color='white')
    plt.savefig('vol_projection.png')
    
    with open("README.md", "w") as f:
        f.write(f"# Stargate v13.0\\n![Dashboard](stargate_dashboard.svg)\\n![Vol](vol_projection.png)\\n")

if __name__ == "__main__":
    sync_assets(144.0, 26.79)
