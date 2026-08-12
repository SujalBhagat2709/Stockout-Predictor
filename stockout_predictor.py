"""
Stockout Predictor
------------------
File : stockout_predictor.py

Purpose
-------
Predicts when a product may run out of stock based on
current inventory, average daily sales, and supplier
lead time.

Features
--------
✔ Add Product
✔ Calculate Average Daily Sales
✔ Estimate Days Until Stockout
✔ Consider Supplier Lead Time
✔ Reorder Recommendation
✔ Stock Risk Level
✔ Inventory Summary
"""


class StockoutPredictor:

    def __init__(self):

        self.products = []

    # ----------------------------------
    # Calculate Average Daily Sales
    # ----------------------------------
    def average_daily_sales(self,
                            sales_history):

        if not sales_history:

            return 0

        return round(

            sum(sales_history) /
            len(sales_history),

            2

        )

    # ----------------------------------
    # Estimate Days Until Stockout
    # ----------------------------------
    def days_until_stockout(self,
                            current_stock,
                            daily_sales):

        if daily_sales <= 0:

            return None

        return round(

            current_stock /
            daily_sales,

            2

        )

    # ----------------------------------
    # Determine Risk Level
    # ----------------------------------
    def risk_level(self,
                   days_left,
                   lead_time):

        if days_left is None:

            return "No Sales Data"

        if days_left <= lead_time:

            return "Critical"

        elif days_left <= lead_time + 3:

            return "High"

        elif days_left <= lead_time + 7:

            return "Medium"

        return "Low"

    # ----------------------------------
    # Reorder Recommendation
    # ----------------------------------
    def reorder_recommendation(self,
                               days_left,
                               lead_time):

        if days_left is None:

            return "Monitor Sales"

        if days_left <= lead_time:

            return "Reorder Immediately"

        elif days_left <= lead_time + 3:

            return "Reorder Soon"

        return "No Immediate Reorder"

    # ----------------------------------
    # Analyze Product
    # ----------------------------------
    def analyze_product(self,
                        product_name,
                        current_stock,
                        sales_history,
                        lead_time):

        daily_sales = self.average_daily_sales(
            sales_history
        )

        days_left = self.days_until_stockout(

            current_stock,
            daily_sales

        )

        product = {

            "Product":
                product_name,

            "Current Stock":
                current_stock,

            "Average Daily Sales":
                daily_sales,

            "Supplier Lead Time":
                lead_time,

            "Estimated Days Until Stockout":
                days_left,

            "Risk Level":
                self.risk_level(
                    days_left,
                    lead_time
                ),

            "Recommendation":
                self.reorder_recommendation(
                    days_left,
                    lead_time
                )

        }

        self.products.append(product)

        return product

    # ----------------------------------
    # Highest Risk Product
    # ----------------------------------
    def highest_risk_product(self):

        if not self.products:

            return None

        priority = {

            "Critical": 4,
            "High": 3,
            "Medium": 2,
            "Low": 1,
            "No Sales Data": 0

        }

        return max(

            self.products,

            key=lambda product:
            (

                priority[
                    product["Risk Level"]
                ],

                -(
                    product[
                        "Estimated Days Until Stockout"
                    ]
                    or float("inf")
                )

            )

        )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        critical = 0
        high = 0
        medium = 0
        low = 0

        for product in self.products:

            level = product["Risk Level"]

            if level == "Critical":

                critical += 1

            elif level == "High":

                high += 1

            elif level == "Medium":

                medium += 1

            elif level == "Low":

                low += 1

        return {

            "Products Analyzed":
                len(self.products),

            "Critical":
                critical,

            "High":
                high,

            "Medium":
                medium,

            "Low":
                low

        }

    # ----------------------------------
    # Display Product
    # ----------------------------------
    def display_product(self,
                        product):

        print(
            "\n========== STOCKOUT ANALYSIS ==========\n"
        )

        for key, value in product.items():

            print(
                f"{key:<32}: {value}"
            )

    # ----------------------------------
    # Display Products
    # ----------------------------------
    def display_products(self):

        if not self.products:

            print(
                "\nNo products analyzed."
            )

            return

        print(
            "\n========== INVENTORY REPORT ==========\n"
        )

        for product in self.products:

            print(
                f"{product['Product']:<20} | "
                f"Stock: {product['Current Stock']:<8} | "
                f"Days Left: "
                f"{product['Estimated Days Until Stockout']} | "
                f"{product['Risk Level']}"
            )

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print(
            "\n========== INVENTORY SUMMARY ==========\n"
        )

        for key, value in report.items():

            print(
                f"{key:<22}: {value}"
            )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    predictor = StockoutPredictor()

    while True:

        print("\n1. Analyze Product")
        print("2. View Inventory Report")
        print("3. Highest Risk Product")
        print("4. Summary")
        print("5. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            product_name = input(
                "Product Name: "
            )

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
            )

            sales_history = [

                float(value)

                for value in
                sales_input.split()

            ]

            lead_time = float(
                input(
                    "Supplier Lead Time (days): "
                )
            )

            product = predictor.analyze_product(

                product_name,
                current_stock,
                sales_history,
                lead_time

            )

            predictor.display_product(
                product
            )

        elif choice == "2":

            predictor.display_products()

        elif choice == "3":

            product = predictor.highest_risk_product()

            if product:

                predictor.display_product(
                    product
                )

            else:

                print(
                    "\nNo products analyzed."
                )

        elif choice == "4":

            predictor.display_summary()

        elif choice == "5":

            print(
                "\nThank you for using Stockout Predictor."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )
