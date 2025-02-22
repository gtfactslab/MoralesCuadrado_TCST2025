import rclpy

from . zHardwareCBFFig8VertTall import HardwareCBFFig8VertTall
from . BlimpMPCNode import BlimpMPCNode

import sys

def main(args=sys.argv):
    print('Algorithm: feedback linearization with CBFS; trajectory: fig8 vertical tall')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.025#0.05
        controller = HardwareCBFFig8VertTall(dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
