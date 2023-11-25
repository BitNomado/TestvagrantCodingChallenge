CB = {
    "Leather wallet": {"qty": 1, "up": 1100, "gst":18},
    "Cigarette": {"qty": 4, "up": 900, "gst":12},
    "Umbrella": {"qty": 12, "up": 200, "gst":8},
    "Honey": {"qty": 28, "up": 100, "gst":0},
}
max_gst_product = None
max_gst_amount = 0
for product, details in CB.items():
    qty = details["qty"]
    up = details["up"]
    gst_amount = details["gst"] * (qty * up) 
    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product
total_amount = sum(details["qty"] * details["up"] for details in CB.values())
print("Product with maximum GST:", max_gst_product)
print("Maximum GST amount:", max_gst_amount)
print("Total amount to be paid:",total_amount)