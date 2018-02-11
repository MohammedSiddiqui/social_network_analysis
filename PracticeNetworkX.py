
# coding: utf-8

# In[5]:



import networkx as nx
import numpy as np
import pandas as pd

get_ipython().magic(u'matplotlib notebook')

G1=nx.Graph()
G1.add_edges_from([(0,1),(0,2),(0,3),(0,5),
                   (1,3),(1,6),(3,4),(4,5),
                    (4,7),(5,8),(8,9)])
#nx.draw_circular(G1)


# In[6]:


G2=nx.Graph()
G2.add_edges_from([(0, 1, {'weight': 4}),
 (0, 2, {'weight': 3}),
 (0, 3, {'weight': 2}),
 (0, 5, {'weight': 6}),
 (1, 3, {'weight': 2}),
 (1, 6, {'weight': 5}),
 (3, 4, {'weight': 3}),
 (5, 4, {'weight': 1}),
 (5, 8, {'weight': 6}),
 (4, 7, {'weight': 2}),
 (8, 9, {'weight': 1})])


#nx.draw_networkx(G2)
#nx.draw_shell(G2, with_labels=True)
nx.draw_spectral(G2, with_labels=True)
#nx.draw_circular(G2, with_labels=True)
#nx.draw_shell(G2, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')


# In[38]:


G2=nx.Graph()
G2.add_edges_from([(0, 1, {'weight': 4}),
 (0, 2, {'weight': 3}),
 (0, 3, {'weight': 2}),
 (0, 5, {'weight': 6}),
 (1, 3, {'weight': 2}),
 (1, 6, {'weight': 5}),
 (3, 4, {'weight': 3}),
 (5, 4, {'weight': 1}),
 (5, 8, {'weight': 6}),
 (4, 7, {'weight': 2}),
 (8, 9, {'weight': 1})])


elarge = [(u, v) for (u, v, d) in G2.edges(data=True) if d['weight'] > 3]
esmall = [(u, v) for (u, v, d) in G2.edges(data=True) if d['weight'] <= 3]

pos = nx.spring_layout(G2)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G2, pos, node_size=700)

# edges
nx.draw_networkx_edges(G2, pos, edgelist=elarge,
                       width=6)
nx.draw_networkx_edges(G2, pos, edgelist=esmall,
                       width=6, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G2, pos, font_size=20, font_family='sans-serif')




# In[29]:


for G in nx.generate_adjlist(G1):
    print(G)    


# In[41]:


G1.edges()


# In[42]:


nx.write_adjlist(G1,"test.adjlist")


# In[9]:


G2 = nx.read_adjlist('test.adjlist')
G2.edges()


# In[33]:


G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])


# In[34]:


G_mat


# In[35]:


G3 = nx.Graph(G_mat)
G3.edges()


# In[40]:


G4=nx.write_edgelist(G3, "test.txt")


# In[37]:


G5 = nx.read_edgelist('test.txt', create_using=nx.Graph(), nodetype=int)
print nx.info(G5)
#nx.draw_networkx(G5)

