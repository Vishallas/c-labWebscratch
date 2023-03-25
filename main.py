import requests

print("C-programs")

path = [
  { "path": "./c-source/list-adt.c", "title": "List ADT Using Array" },
  { "path": "./c-source/sll.c", "title": "Singly Linked List" },
  { "path": "./c-source/dll.c", "title": "Doubly Linked List" },
  { "path": "./c-source/stack-array.c", "title": "Stack Using Array" },
  { "path": "./c-source/queue-array.c", "title": "Queue Using Array" },
  { "path": "./c-source/stack-linked.c", "title": "Stack Using Linked List" },
  { "path": "./c-source/queue-linked.c", "title": "Queue Using Linked List" },
  { "path": "./c-source/poly-adt.c", "title": "Polynomial ADT Using Array" },
  { "path": "./c-source/infix-postfix.c", "title": "Infix To Postfix Expression" },
  { "path": "./c-source/stack-postfix.c", "title": "Stack Operations For Evaluating Postfix Expressions" },
  { "path": "./c-source/binary-search-tree.c", "title": "Binary Search Tree" },
  { "path": "./c-source/avl-tree.c", "title": "AVL Tree" },
  { "path": "./c-source/priority-queue.c", "title": "Priority Queue Using Heaps" },
  { "path": "./c-source/dijkstra-shortpath.c", "title": "Dijkstra's Single Source Shortest Path" },
  { "path": "./c-source/floyd-warshall.c", "title": "Floyd Warshall Algorithm" },
  { "path": "./c-source/kruskal-algorithm.c", "title": "Kruskal's Algorithm" },
  { "path": "./c-source/prim-algorithm.c", "title": "Prim's Algorithm" },
  { "path": "./c-source/bfs-dfs.c", "title": "BFS And DFS On A Graph Represented Using Adjacency List" },
  { "path": "./c-source/topological.c", "title": "Topological Sorting" },
  { "path": "./c-source/insertion-sort.c", "title": "Insertion Sort" },
  { "path": "./c-source/selection-sort.c", "title": "Selection Sort" },
  { "path": "./c-source/quick-sort.c", "title": "Quick Sort" },
  { "path": "./c-source/merge-sort.c", "title": "Merge Sort" },
  { "path": "./c-source/linear-search.c", "title": "Linear Search" },
  { "path": "./c-source/binary-search.c", "title": "Binary Search" },
  { "path": "./c-source/hasing-probing.c", "title": "Hasing Using Linear And Quadratic Probing" }]

for idx,data in enumerate(path,1):
    print(idx,data["title"])

ch = int(input("Enter the choice "))

link = path[ch-1]["path"][1:]
filename = link[10:]

page = requests.get(f"https://ece-clab.netlify.app/{link}") 

#Writing the page data to the file
with open(filename,'wb') as f:
     f.write(page.content)

print("File copied")