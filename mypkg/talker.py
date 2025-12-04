import rclpy
from rclpy.node import Node
<<<<<<< HEAD
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0


def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb)
=======
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.name == "藤田柚樹":
        response.age = 20
    else:
        response.age = 255

    return response


def main():
    srv = node.create_service(Query, "query", cb)
>>>>>>> 50ab9235fd936ad1dbe153e9e40368ba971e8b39
    rclpy.spin(node)
