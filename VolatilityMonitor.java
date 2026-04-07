import java.util.List;

public class VolatilityMonitor {
    public record Pivot(String asset, double price, double change) {}

    public static void main(String[] args) {
        var msft = new Pivot("MSFT", 370.79, -0.56);
        var vix = new Pivot("VIX", 26.79, 10.84);

        System.out.println("[Java 26 Stargate Node]");
        
        List.of(msft, vix).forEach(p -> {
            // Using a switch expression to handle pattern matching scope correctly
            switch (p) {
                case Pivot(String name, double val, double delta) when delta > 5.0 ->
                    System.out.printf("CRITICAL VOLATILITY: %s at %.2f (%+.2f%%)%n", name, val, delta);
                case Pivot(String name, double val, double delta) ->
                    System.out.printf("Tracking %s: %.2f (%+.2f%%)%n", name, val, delta);
            }
        });
    }
}
