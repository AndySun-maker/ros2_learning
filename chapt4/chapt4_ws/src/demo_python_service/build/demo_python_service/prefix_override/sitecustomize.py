import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fishros/chapt4/chapt4_ws/src/demo_python_service/install/demo_python_service'
