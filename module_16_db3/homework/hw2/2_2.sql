SELECT customer.full_name FROM customer
join "order" on customer.customer_id = "order".customer_id
where "order".customer_id is null



