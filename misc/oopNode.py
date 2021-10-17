#!/usr/bin/env python3
import rclpy
from rclpy import node
from rclpy.node import Node


class MyCustomNode(Node): # MODIFY NAME AS REQUIRED
    def __init__(self):
        super().__init__("node_name") # MODIFY NAME AS REQUIRED


def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode() # MODIFY NAME AS REQUIRED
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

