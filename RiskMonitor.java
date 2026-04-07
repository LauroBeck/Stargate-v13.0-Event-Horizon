import java.nio.file.*;

public class RiskMonitor {
    public static void main(String[] args) throws Exception {
        String svg = """
            <svg width="500" height="270" xmlns="http://www.w3.org/2000/svg">
                <rect width="100%" height="100%" fill="#0a0a0a" />
                <text x="20" y="40" fill="#00ff00" font-family="monospace" font-size="20">STARGATE v13.0: EVENT HORIZON</text>
                <text x="20" y="80" fill="white" font-size="14">SPX: 6611.83 | VIX: 26.79</text>
                <text x="20" y="110" fill="#ff4500" font-size="16" font-weight="bold">BRENT: $144.00 (MODEL PEAK)</text>
                <text x="20" y="140" fill="#222" font-size="12">YIELD DATA (CVX): Nasdaq Visual Null (Apr 7)</text>
                <rect x="20" y="190" width="460" height="30" fill="#222" />
                <text x="30" y="211" fill="red" font-weight="bold">IRAN DEADLINE: 20:00 EST / 21:00 BRT</text>
                <circle cx="450" cy="211" r="6" fill="red"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></circle>
            </svg>
            """;
        Files.writeString(Paths.get("stargate_dashboard.svg"), svg);
        System.out.println("[JAVA 26] SVG Dashboard updated with Yield Null indicator.");
    }
}
