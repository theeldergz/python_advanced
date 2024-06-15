select "order".order_no, manager.full_name as manager_nam, customer.full_name as customer_name from customer
join manager on customer.manager_id = manager.manager_id
join "order" on "order".customer_id = customer.customer_id
where customer.city != manager.city