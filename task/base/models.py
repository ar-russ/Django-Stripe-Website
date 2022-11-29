from django.db import models


class Order(models.Model):
    items_id = models.TextField(blank=True)
    total_cost = models.IntegerField(default=0) # In cents
    
    
    def add_item(self, item):
        self.items_id += str(item.id) + ','
        self.total_cost += item.price
        self.save()

    
    def delete_item(self, item):
        self.items_id = self.items_id.replace(str(item.id) + ',', '')
        self.total_cost -= item.price
        self.save()
    
    
    def get_as_list(self):
            return [int(i) for i in self.items_id.split(',') if i.isdigit()]
    
    
    def get_items_in_order(self):
        item_list = []
        for item_id in self.get_as_list():
            item = Item.objects.get(id=item_id)
            item_list.append(item)
        return item_list

    
    def get_total_cost_in_dollars(self):
        return self.total_cost / 100
    
    
    def clear(self):
        self.items_id = ''
        self.total_cost = 0
        self.save()


class Item(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0) # In cents
    
    
    def __str__(self) -> str:
        return self.name
    
    
    def get_price_in_dollars(self) -> int:
        return self.price / 100