#include <iostream>
#include <string>
#include <expected>

struct MarketSnapshot {
    std::string ticker;
    double price;
    double bid;
    double ask;
    long volume;
};

std::expected<MarketSnapshot, std::string> get_cvx_telemetry() {
    // Session Data: 2026-04-07 14:45:19
    MarketSnapshot cvx{"CVX", 201.265, 201.25, 201.28, 8618520};
    if (cvx.volume < 0) return std::unexpected("Data Integrity Failure");
    return cvx;
}

int main() {
    auto result = get_cvx_telemetry();
    if (result) {
        std::cout << "[C++26 Engine] " << result->ticker 
                  << " Price: $" << result->price << std::endl;
    }
    return 0;
}
