import csv
 
DATA_FILE = "data.csv"
 
 
# --------------------------------------------------------------------------
# STEP 1 & 2: Read and clean the data
# --------------------------------------------------------------------------
def load_and_clean_data(filename):
    """Reads the CSV file and returns a list of clean transaction dicts."""
    clean_rows = []
    total_rows = 0
    skipped_missing_customer = 0
    skipped_bad_quantity = 0
    skipped_bad_price = 0
 
    with open(filename, encoding="latin1") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1
 
            # Skip rows with no CustomerID
            if not row["CustomerID"] or row["CustomerID"].strip() == "":
                skipped_missing_customer += 1
                continue
 
            # Skip cancelled orders / returns (negative or zero quantity)
            try:
                quantity = int(row["Quantity"])
            except ValueError:
                skipped_bad_quantity += 1
                continue
            if quantity <= 0:
                skipped_bad_quantity += 1
                continue
 
            # Skip invalid prices
            try:
                unit_price = float(row["UnitPrice"])
            except ValueError:
                skipped_bad_price += 1
                continue
            if unit_price <= 0:
                skipped_bad_price += 1
                continue
 
            clean_rows.append({
                "InvoiceNo": row["InvoiceNo"],
                "StockCode": row["StockCode"],
                "Description": row["Description"].strip(),
                "Quantity": quantity,
                "UnitPrice": unit_price,
                "CustomerID": row["CustomerID"].strip(),
                "Country": row["Country"],
            })
 
    print("=" * 70)
    print("DATA CLEANING SUMMARY")
    print("=" * 70)
    print(f"Total rows read           : {total_rows}")
    print(f"Skipped (missing customer): {skipped_missing_customer}")
    print(f"Skipped (bad quantity)    : {skipped_bad_quantity}")
    print(f"Skipped (bad price)       : {skipped_bad_price}")
    print(f"Clean rows remaining      : {len(clean_rows)}")
    print()
 
    return clean_rows
 
 
# --------------------------------------------------------------------------
# STEP 3: Aggregate data using dictionaries
# --------------------------------------------------------------------------
def aggregate_data(rows):
    """Builds per-customer spend and per-product quantity/revenue totals."""
    customer_spend = {}          # CustomerID -> total amount spent
    product_quantity = {}        # StockCode -> total units sold
    product_revenue = {}         # StockCode -> total revenue
    product_name = {}            # StockCode -> Description (for display)
 
    for row in rows:
        line_total = row["Quantity"] * row["UnitPrice"]
 
        # Customer spend
        cust = row["CustomerID"]
        customer_spend[cust] = customer_spend.get(cust, 0) + line_total
 
        # Product quantity & revenue
        code = row["StockCode"]
        product_quantity[code] = product_quantity.get(code, 0) + row["Quantity"]
        product_revenue[code] = product_revenue.get(code, 0) + line_total
        product_name.setdefault(code, row["Description"])
 
    return customer_spend, product_quantity, product_revenue, product_name
 
 
# --------------------------------------------------------------------------
# STEP 4: Manual Linear Search based Top-K extraction (no sorted()/max())
# --------------------------------------------------------------------------
def find_top_k(data_dict, k=5):
    """
    Given a dictionary of {key: numeric_value}, returns the top-k
    (key, value) pairs ranked by value, highest first.
 
    Implemented using repeated LINEAR SEARCH:
    each pass scans every remaining item once to find the current maximum.
    """
    # Convert dict items to a list we can search through and mark as used
    items = list(data_dict.items())      # [(key, value), ...]
    used = [False] * len(items)          # tracks which items are already picked
    top_results = []
 
    for _ in range(min(k, len(items))):
        best_index = -1
        best_value = None
 
        # ----- LINEAR SEARCH for the maximum unused value -----
        for i in range(len(items)):
            if used[i]:
                continue
            current_value = items[i][1]
            if best_index == -1 or current_value > best_value:
                best_index = i
                best_value = current_value
        # --------------------------------------------------------
 
        used[best_index] = True
        top_results.append(items[best_index])
 
    return top_results
 
 
# --------------------------------------------------------------------------
# STEP 5: Reporting
# --------------------------------------------------------------------------
def print_report(top_customers, top_qty_products, top_rev_products, product_name):
    print("=" * 70)
    print("TOP 5 CUSTOMERS BY TOTAL SPEND")
    print("=" * 70)
    print(f"{'Rank':<6}{'CustomerID':<15}{'Total Spend':>15}")
    for rank, (cust_id, spend) in enumerate(top_customers, start=1):
        print(f"{rank:<6}{cust_id:<15}{spend:>15,.2f}")
 
    print()
    print("=" * 70)
    print("TOP 5 PRODUCTS BY QUANTITY SOLD")
    print("=" * 70)
    print(f"{'Rank':<6}{'StockCode':<12}{'Qty Sold':>10}   Description")
    for rank, (code, qty) in enumerate(top_qty_products, start=1):
        desc = product_name.get(code, "")[:40]
        print(f"{rank:<6}{code:<12}{qty:>10}   {desc}")
 
    print()
    print("=" * 70)
    print("TOP 5 PRODUCTS BY REVENUE GENERATED")
    print("=" * 70)
    print(f"{'Rank':<6}{'StockCode':<12}{'Revenue':>12}   Description")
    for rank, (code, rev) in enumerate(top_rev_products, start=1):
        desc = product_name.get(code, "")[:40]
        print(f"{rank:<6}{code:<12}{rev:>12,.2f}   {desc}")
 
 
# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------
def main():
    rows = load_and_clean_data(DATA_FILE)
    customer_spend, product_qty, product_rev, product_name = aggregate_data(rows)
 
    top_customers = find_top_k(customer_spend, k=5)
    top_qty_products = find_top_k(product_qty, k=5)
    top_rev_products = find_top_k(product_rev, k=5)
 
    print_report(top_customers, top_qty_products, top_rev_products, product_name)
 
 
if __name__ == "__main__":
    main()