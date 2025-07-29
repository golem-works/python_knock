### pip install networkx でnetworkxをインストールしてください
### pip install matplotlib でmatplotlibをインストールしてください
### このコードはネットワークを可視化したものです。

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# ノードの追加
G.add_node("A")
G.add_node("B")

# エッジの追加(コメントアウトすると通信不可)
G.add_edge("A", "B")


def send_msg(graph, source, target):
    if not graph.has_node(source) or not graph.has_node(target):
        print("ノードが存在しません。")
        return
    
    if not graph.has_edge(source, target):
        print(f"{source} から {target} へのエッジが存在しません。")
        return
    message = input("メッセージを入力してください: ")
    print(f"{source} から {target} へメッセージを送信: {message}")

send_msg(G, "A", "B")

# ネットワークの可視化
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_color='black', font_weight='bold')
plt.title("Network Visualization")
plt.show()