-- View sales table
SELECT * FROM sales;

-- View income table
SELECT * FROM income;

-- Join sales and income into housing table
SELECT sales."Sale Date", sales."City", sales."Zip Code",
	   sales."Year Built", sales."Bed", sales."Bath",
	   sales."Sale Price", sales."Square Feet", sales."Lot Size",
	   sales."$/SF", income."Zip Population", income."Zip SqMi", 
	   income."Zip Pop Density", income."Zip Mean HHI"
INTO housing
FROM sales
JOIN income ON sales."Zip Code" = income."Zip Code"
WHERE ("Year Built" > 1950)
AND ("Bed" < 10)
AND ("Sale Price" > 100000 AND "Sale Price" < 2000000)
AND ("Square Feet" > 500 AND "Square Feet" < 7000)
AND ("$/SF" > 125 AND "$/SF" < 450);

-- View housing table
SELECT * FROM housing;

-- Check total rows
SELECT COUNT(*) FROM housing;