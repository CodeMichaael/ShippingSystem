from typing import List, Optional
import random

class System:

    def __init__(self, queue_name: Optional[str] = "Default Queue", max_queue_length: Optional[int] = 10) -> None:
        self.queue_name = queue_name
        self.max_length = max_queue_length
        self.queue_list = List[int]  
        self.queue = {}
        self.number = random.randint(99999, 99999)  

    def add_items(self, queue: str, item: List[str], id: Optional[int] = None) -> dict:
        if queue != self.queue_name or len(self.queue_list) >= self.max_length:
            return {"error": "Your queue name was not found or the queue is full"}

        elif queue == self.queue_name and self.max_length > len(self.queue_list):
            if id is None or id not in self.queue_list:
                new_id = self.number if id is None else id
                format_data = {"id": new_id, "shipping_items": item}  
                self.queue[new_id] = format_data
                self.queue_list.append(new_id)
                return {"success": f"Successfully added {new_id} to shipping queue"}
            else:
                return {"error": "ID already found in queue"}
        else:
            return {"error": "Unable to add item"}

    def remove_items(self, queue: str, id: int) -> dict:
        if queue == self.queue_name and id in self.queue_list:
            self.queue_list.remove(id)
            del self.queue[id]
            return {"success": f"Successfully removed {id} from shipping queue"}
        else:
            return {"error": "Item not found in the queue"}

    def get_items(self, queue: str, id: int) -> dict:
        if queue == self.queue_name and id in self.queue_list:
            return self.queue[id]["shipping_items"]
        else:
            return {"error": "Item not found in the queue"}

    def remove_items(self, queue: str, id: int):
        if queue == self.queue_name and id in self.queue_list:
            if len(self.queue_list) > 2:
                index = self.queue_list.index(id)
                self.queue_list.pop(index)

                # Shift the remaining items one position to the left
                for i in range(index, len(self.queue_list)):
                    self.queue_list[i - 1] = self.queue_list[i]

                # Remove the last item (now a duplicate) from the list
                self.queue_list.pop()

                # Retrieve and return the shipping_items associated with the removed item
                removed_item = self.queue.pop(id)
                return {"success": "Item removed from the queue", "removed_item": removed_item["shipping_items"]}

            else:
                # If the length of the queue is less than or equal to 2, just remove the item without shifting
                removed_item = self.queue.pop(id)
                return {"success": "Item removed from the queue", "removed_item": removed_item["shipping_items"]}

        else:
            return {"error": "Item not found in the queue"}
