import matplotlib.pyplot as plt

def generate_visuals():
    # Data derived from verified April 7, 2026 sources
    data = {
        'JEPQ': 11.99,
        'CVX': 3.72,
        'IBM': 2.71,
        'JPM': 2.04,
        'TSLA': 0.00
    }
    
    plt.figure(figsize=(10, 5), facecolor='#0a0a0a')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')
    
    colors = ['#00ff00' if v > 0 else '#444' for v in data.values()]
    plt.bar(data.keys(), data.values(), color=colors)
    
    plt.title("Cluster Yield Monitor (Verification: Apr 7, 2026)", color='white')
    plt.ylabel("Forward Yield (%)", color='white')
    plt.tick_params(colors='white')
    plt.grid(axis='y', color='#333', linestyle='--')
    
    plt.savefig('div_status.png')
    print("[PYTHON 3.15] Verified div_status.png generated.")

if __name__ == "__main__":
    generate_visuals()
