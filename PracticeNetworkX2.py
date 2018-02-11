
# coding: utf-8

# In[ ]:


import networkx as nx

fh=open("Email-EuAll.txt", 'rb')
G=nx.read_edgelist(fh)
fh.close()


# In[ ]:



G=nx.read_edgelist("Email-EuAll.txt",create_using=nx.DiGraph(),nodetype=int)


# In[ ]:


G.edges()


# In[ ]:


list(G.degree())


# In[ ]:


G1=nx.Graph()
G1=nx.read_edgelist("test.edgelist", nodetype=int)
G1.add_edge('11','12',Weight=3)
nx.write_edgelist(G1,"test.adjlist")



# In[ ]:


list(G1.degree())

