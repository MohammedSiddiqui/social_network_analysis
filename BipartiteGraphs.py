
# coding: utf-8

# In[18]:


import networkx as nx
from networkx.algorithms import bipartite
import matplotlib as plt
get_ipython().magic(u'matplotlib notebook')
B = nx.Graph()
B.add_edges_from([('A',1), ('B',1),('C',1),('D',1),('H',1), ('B', 2), ('C', 2), ('D', 2), ('E', 2), ('G', 2), ('E', 3), ('F', 3), ('H', 3), ('J', 3), ('E', 4), ('I', 4), ('J', 4) ])
nx.bipartite.is_bipartite(B)


# In[15]:


#nx.draw(B)


# In[16]:


bipartite.sets(B)


# In[9]:


left, right = nx.bipartite.sets(B)


# In[10]:


list(left)


# In[11]:


list(right)


# In[25]:


pos = {}

# Update position for node from each group
pos.update((node, (1, index1)) for index1, node in enumerate(left))
pos.update((node, (2, index2)) for index2, node in enumerate(right))

#nx.draw(B, pos=pos)


# In[27]:


P = bipartite.projected_graph(B, left)
#nx.draw(P)


# In[29]:


P = bipartite.projected_graph(B, right)
#nx.draw(P)


# In[66]:


P = bipartite.weighted_projected_graph(B, left)

#nx.draw_spectral(P, with_labels=True)


# In[58]:


P.edges(data= True)


# In[48]:


B.edges(data= True)


# In[74]:


pos=nx.spring_layout(P)
nx.draw(P,pos)
# specifiy edge labels explicitly
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in P.edges(data=True)])
nx.draw_networkx_edge_labels(P,pos,edge_labels=edge_labels)


# In[73]:


pos=nx.spring_layout(P)
#nx.draw(P,pos)

#nx.draw_networkx_edge_labels(P,pos)

