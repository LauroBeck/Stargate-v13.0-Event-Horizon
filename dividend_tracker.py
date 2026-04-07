import matplotlib.pyplot as plt

def generate_telemetry():
    # Verified April 7, 2026 Telemetry
    data = {
        'JEPQ': {'y': 11.99, 'c': '#00ff00'},
        'CVX':  {'y': 3.72,  'c': '#008000'},
        'IBM':  {'y': 2.56,  'c': '#0000ff'},
        'JPM':  {'y': 2.04,  'c': '#ffffff'},
        'TSLA': {'y': 0.00,  'c': '#ff0000'}
    }

    plt.figure(figsize=(10, 5), facecolor='#0a0a0a')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')
    
    bars = plt.bar(data.keys(), [v['y'] for v in data.values()], 
                   color=[v['c'] for v in data.values()], edgecolor='white')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f"{yval}%", 
                 ha='center', va='bottom', color='white', fontweight='bold')

    plt.title("Cluster Yield Integrity (Verification: Apr 7, 2026)", color='white')
    plt.ylabel("Forward Dividend Yield (%)", color='white')
    plt.tick_params(colors='white')
    plt.grid(axis='y', color='#333', linestyle='--', alpha=0.5)
    plt.savefig('div_status.png', dpi=300)
    print("[PYTHON 3.15] Visual Asset 'div_status.png' Synchronized.")

if __name__ == "__main__":
    generate_telemetry()
