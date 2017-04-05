import csv

class TreeNode:
  def __init__(self,value):
    self.left=None;
    self.right=None;
    self.data=value;

class Tree:
  def __init__(self):
    self.root=None;
  def addNode(self,node,value):
    if(node==None):
      self.root=TreeNode(value);
    elif value==node.data:
      a=0
    else:
      if(value<node.data):
        if(node.left==None):
          node.left=TreeNode(value)
        else:
          self.addNode(node.left,value);
      else:
         if(node.right==None):
           node.right=TreeNode(value)
         else:
           self.addNode(node.right,value)
  def printInorder(self,node):
     if(node!=None):
       self.printInorder(node.left)
       print(node.data)
       self.printInorder(node.right)
  def printPostOrder(self,node):
    if(node!=None):
      self.printPostOrder(node.left)
      self.printPostOrder(node.right)
      print(node.data)
 
fp=open("../Video_Games_Sales_as_at_22_Dec_2016.csv","rt")
reader=csv.reader(fp)
testTree=Tree()
count=0
c=0
for line in reader:
  if (c==0):
    c=1
    continue
  testTree.addNode(testTree.root,int(float(line[2])))
  count+=1
  if count==100:
    break
print("Inorder::")
testTree.printInorder(testTree.root)
print("PostOrder::")
testTree.printPostOrder(testTree.root)