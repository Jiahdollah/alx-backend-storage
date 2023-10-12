-- write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- quantity in the table items can be negative.
-- context: Updating multiple tables for one action from your application can generate issue: network disconnection,
-- Crash, etc… to keep your data in a good shape, let MySQL do it for you!

CREATE TRIGGER decrease_items_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;