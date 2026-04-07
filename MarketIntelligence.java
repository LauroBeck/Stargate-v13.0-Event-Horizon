public class MarketIntelligence {
    public record Session(String ticker, double price, double change) {}

    public static void main(String[] args) {
        var cvx = new Session("CVX", 201.265, 1.21);

        // Utilizing Java 26 Pattern Matching
        if (cvx instanceof Session(String t, double p, double c)) {
            System.out.printf("[Java 26] %s: $%.3f (Delta: %+.2f%%)%n", t, p, c);
        }
    }
}
