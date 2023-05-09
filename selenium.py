from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import matplotlib as mpl
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager
import japanize_matplotlib

font_manager.fontManager.addfont("ipaexg.ttf")
mpl.rc('font', family="IPAexGothic")

url = "https://www.stat.go.jp/dss/"

driver = webdriver.Chrome("C:/Program Files/chromedriver_win32/chromedriver.exe")
driver.get(url)

nodes = []
edges = []

title = driver.title
nodes.append(title)

links = driver.find_elements_by_tag_name("a")
for link in links:
    href = link.get_attribute("href")
    if href is not None and href.startswith(url):
        edges.append((title, link.text))

for link in links:
    href = link.get_attribute("href")
    if href is not None and href.startswith(url):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(href)
        new_title = driver.title
        nodes.append(new_title)
        edges.append((title, new_title))
        title = new_title
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

offset = 0.1
pos = nx.spring_layout(G, seed=42, k=0.35, pos=None, fixed=None, iterations=150, threshold=1e-4, weight='weight', scale=1, center=None, dim=2)
label_pos = {key: (value[0], value[1] + offset) for key, value in pos.items()}

nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="white")
nx.draw_networkx_edges(G, pos, edge_color="black", width=1.5, arrowsize=20, arrowstyle='-|>', connectionstyle='arc3,rad=0.2')
nx.draw_networkx_labels(G, label_pos, font_size=14, font_family="IPAexGothic")

# 遷移数をタイトルとして追加
plt.title(f"全画面遷移数: {len(nodes)}", fontsize=20)

plt.axis("off")
plt.tight_layout()
plt.show()

driver.quit()
