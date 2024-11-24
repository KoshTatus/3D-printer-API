import threading
import time

from schemas.order_schemas import OrderModel


class PrinterQueue:
    def __init__(self):
        self.orders = []
        self.active_order = None
        self.queue_lock = threading.Lock()
        self.worker_thread = threading.Thread(target=self._process_orders)
        self.worker_thread.daemon = True
        self.worker_thread.start()

    def add_order(self, order: OrderModel):
        with self.queue_lock:
            if order.state in {0, 2, 3, 4}:
                self.orders.append(order)
                self.orders.sort(key=lambda o: o.createdAt)

    def approve_order(self, order_id: int):
        with self.queue_lock:
            if self.active_order and self.active_order.order_id == order_id:
                self.active_order.state = 3
                self.active_order = None

    def _process_orders(self):
        while True:
            with self.queue_lock:
                if not self.active_order and self.orders:
                    self.active_order = self.orders.pop(0)

            if self.active_order:
                self._update_progress(self.active_order)

            time.sleep(5)

    def _update_progress(self, order: OrderModel):
        if order.progress < 100:
            order.progress += 10
        if order.progress >= 100:
            order.state = 3
            self.active_order = None