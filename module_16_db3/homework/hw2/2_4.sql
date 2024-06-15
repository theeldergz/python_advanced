select "order".order_no, customer.full_name from customer
join "order" on customer.customer_id = "order".customer_id
where "order".manager_id is null