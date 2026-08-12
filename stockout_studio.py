"""
Stockout Predictor Studio
-------------------------
Main interface for Stockout Predictor.
"""

from stockout_predictor import StockoutPredictor


class StockoutStudio:

    def __init__(self):

        self.predictor = StockoutPredictor()

    # ----------------------------------
    # Analyze Product
    # ----------------------------------
    def analyze_product(self):

        print(
            "\n========== STOCKOUT ANALYSIS ==========\n"
        )

        product_name = input(
            "Product Name: "
        ).strip()

        current_stock = float(
            input(
                "Current Stock: "
            )
        )

        print(
            "\nEnter recent daily sales."
        )

        sales_input = input(
            "Sales values separated by spaces: "
        ).strip()

        try:

            sales_history = [

                float(value)

                for value in sales_input.split()

            ]

        except ValueError:

            print(
                "\nInvalid sales values."
            )

            return

        lead_time = float(
            input(
                "Supplier Lead Time (days): "
            )
        )

        product = self.predictor.analyze_product(

            product_name,
            current_stock,
            sales_history,
            lead_time

        )

        print(
            "\nStockout prediction completed."
        )

        self.predictor.display_product(
            product
        )

    # ----------------------------------
    # Inventory Report
    # ----------------------------------
    def inventory_report(self):

        self.predictor.display_products()

    # ----------------------------------
    # Highest Risk Product
    # ----------------------------------
    def highest_risk(self):

        product = self.predictor.highest_risk_product()

        if product:

            print(
                "\n========== HIGHEST STOCKOUT RISK ==========\n"
            )

            self.predictor.display_product(
                product
            )

        else:

            print(
                "\nNo products analyzed."
            )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.predictor.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("             STOCKOUT PREDICTOR")
            print("=" * 60)

            print("1. Analyze Product")
            print("2. View Inventory Report")
            print("3. Highest Risk Product")
            print("4. Summary")
            print("5. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.analyze_product()

            elif choice == "2":

                self.inventory_report()

            elif choice == "3":

                self.highest_risk()

            elif choice == "4":

                self.summary()

            elif choice == "5":

                print(
                    "\nThank you for using Stockout Predictor."
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = StockoutStudio()

    studio.menu()
