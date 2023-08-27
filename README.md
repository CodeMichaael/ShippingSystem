# ShippingSystem
Shipping System, an example of a classic shipping system.

### Example 1: Adding Items

```python
system = System()

# Add an item to the queue
add_result = system.add_items("Default Queue", ["item1"])
print(add_result)  # Should print: {"success": "Successfully added <id> to shipping queue"}

# Attempt to add an item with an existing ID
add_result = system.add_items("Default Queue", ["item2"], id=<existing_id>)
print(add_result)  # Should print: {"error": "ID already found in queue"}

# Attempt to add an item to a different queue
add_result = system.add_items("Another Queue", ["item3"])
print(add_result)  # Should print: {"error": "Your queue name was not found or the queue is full"}
```

### Example 2: Removing Items

```python
system = System()

# Add an item to the queue
system.add_items("Default Queue", ["item1"])

# Remove the added item
remove_result = system.remove_items("Default Queue", <id_of_added_item>)
print(remove_result)  # Should print: {"success": "Successfully removed <id> from shipping queue"}

# Attempt to remove an item not in the queue
remove_result = system.remove_items("Default Queue", <non_existing_id>)
print(remove_result)  # Should print: {"error": "Item not found in the queue"}

# Attempt to remove an item from a different queue
remove_result = system.remove_items("Another Queue", <id_of_added_item>)
print(remove_result)  # Should print: {"error": "Item not found in the queue"}
```

### Example 3: Getting Items

```python
system = System()

# Add an item to the queue
system.add_items("Default Queue", ["item1"])

# Get the items associated with the added item
get_result = system.get_items("Default Queue", <id_of_added_item>)
print(get_result)  # Should print: ["item1"]

# Attempt to get items of an item not in the queue
get_result = system.get_items("Default Queue", <non_existing_id>)
print(get_result)  # Should print: {"error": "Item not found in the queue"}

# Attempt to get items from a different queue
get_result = system.get_items("Another Queue", <id_of_added_item>)
print(get_result)  # Should print: {"error": "Item not found in the queue"}
```
