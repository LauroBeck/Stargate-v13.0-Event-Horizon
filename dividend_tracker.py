import matplotlib.pyplot as plt

def sync_target_cluster():
    # Verified Market Telemetry: April 7, 2026
    cluster_data = {
        'JEPQ': {'yield': 11.99, 'status': 'High Yield Lead', 'color': '#00ff00'},
        'CVX':  {'yield': 3.72,  'status': 'Value Anchor',   'color': '#008000'},
        'IBM':  {'yield': 2.71,  'status': 'Steady Growth',  'color': '#0000ff'},
        'JPM':  {'yield': 2.04,  'status': 'Sector Strength','color': '#ffffff'},
        'TSLA': {'yield': 0.00,  'status': 'Pure Momentum',  'color': '#ff0000'}
    }

    tickers = list(cluster_data.keys())
    yields = [d['yield'] for d in cluster_data.values()]
    colors = [d['color'] for d in cluster_data.values()]

    plt.figure(figsize=(10, 5), facecolor='#0a0a0a')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')
    
    bars = plt.bar(tickers, yields, color=colors, edgecolor='white', linewidth=0.5)
    
    # Label yields on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f"{yval}%", 
                 ha='center', va='bottom', color='white', fontsize=10, fontweight='bold')

    plt.title("Stargate v13.0: Cluster Yield Integrity (Apr 7, 2026)", color='white', fontsize=14)
    plt.ylabel("Forward Dividend Yield (%)", color='white')
    plt.tick_params(colors='white')
    plt.ylim(0, 15) # Buffer for JEPQ lead
    plt.grid(axis='y', color='#333', linestyle='--', alpha=0.5)
    
    plt.savefig('div_status.png', dpi=300)
    print("[PYTHON 3.15] Cluster Telemetry Assets Generated: div_status.png")

if __name__ == "__main__":
    sync_target_cluster()
