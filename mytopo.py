from mininet.topo import Topo, Node
class MyTopo(Topo):
    "Simple topolopy example."

    def __init__(self, enable_all = True):
        "Create custom topo."
        super(MyTopo,self).__init__()

        #set Node IDs for hosts and switchs
        leftHost1 = 1
        leftHost2 = 2
        leftSwitch = 3
        rightSwitch = 4
        rightHost1 = 5
        rightHost2 = 6
        
        #Add nodes
        self.add_node(leftSwitch, Node(is_switch=True))
        self.add_node(rightSwitch, Node(is_switch=True))
        self.add_node(leftHost1, Node(is_switch=False))
        self.add_node(rightHost1, Node(is_switch=False))
        self.add_node(leftHost2, Node(is_switch=False))
        self.add_node(rightHost2, Node(is_switch=False))

        #Add edges
        self.add_edge(leftHost1, leftSwitch)
        self.add_edge(leftHost2, leftSwitch)
        self.add_edge(leftSwitch, rightSwitch)
        self.add_edge(rightSwitch, rightHost1)
        self.add_edge(rightSwitch, rightHost2)
        
        #Consider all switches and host 'on'
        self.enable_all()

topos = {'mytopo':(lambda: MyTopo())}
