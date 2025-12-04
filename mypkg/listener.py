import rclpy
from rclpy.node import Node
<<<<<<< HEAD
from std_msgs.msg import Int16
=======
from person_msgs.srv import Query
>>>>>>> 50ab9235fd936ad1dbe153e9e40368ba971e8b39


rclpy.init()
node = Node("listener")


<<<<<<< HEAD
def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

def main():
    pub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
=======
def main():
    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "藤田柚樹"
    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("age: {}".format(response.age))

            break

    node.destroy_node()
    rclpy.shutdown()
>>>>>>> 50ab9235fd936ad1dbe153e9e40368ba971e8b39
