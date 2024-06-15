select customer.full_name as customer_name, manager.full_name as manager_name from customer
inner join manager on customer.manager_id = manager.manager_id
where c