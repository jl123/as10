

import copy
def main():
   """ test main"""

   # instantiate a "data" tree of strings
   scene_tree = FhSdDataTree(str)

   print( "Starting tree empty? " +  str(scene_tree.empty()) )

   scene_tree.add_child_to_cur("room")

   # add three objects to the scene tree
   scene_tree.find("room")
   scene_tree.add_child_to_cur("Lily the canine")
   scene_tree.add_child_to_cur("Miguel the human")
   scene_tree.add_child_to_cur("table")

   # add some parts to Miguel
   scene_tree.find_in_cur_subtree("Miguel the human")
   scene_tree.add_child_to_cur("torso")

   # Miguel's arms
   scene_tree.find_in_cur_subtree("torso")
   scene_tree.add_child_to_cur("left arm")
   scene_tree.add_child_to_cur("right arm")

   # add things Miguel's left arm (only one in room)
   scene_tree.find("left arm")
   scene_tree.add_child_to_cur("left hand")

   # for variety, we won't label fingers left/right
   scene_tree.find_in_cur_subtree("left hand")
   scene_tree.add_child_to_cur("thumb")
   scene_tree.add_child_to_cur("index finger")
   scene_tree.add_child_to_cur("middle finger")
   scene_tree.add_child_to_cur("ring finger")
   scene_tree.add_child_to_cur("pinky")

   # add things Miguel's right arm (only one in room)
   scene_tree.find("right arm")
   scene_tree.add_child_to_cur("right hand")

   # for variety, we won't label fingers left/right
   scene_tree.find_in_cur_subtree("right hand")
   scene_tree.add_child_to_cur("thumb")
   scene_tree.add_child_to_cur("index finger")
   scene_tree.add_child_to_cur("middle finger")
   scene_tree.add_child_to_cur("ring finger")
   scene_tree.add_child_to_cur("pinky")

   # add some parts to Lily
   scene_tree.find("Lily the canine")
   scene_tree.add_child_to_cur("torso")

   # we are careful to add to Liliy's "torso" not Miguel's
   scene_tree.find_in_cur_subtree("torso")
   scene_tree.add_child_to_cur("right front paw")
   scene_tree.add_child_to_cur("left front paw")
   scene_tree.add_child_to_cur("right rear paw")
   scene_tree.add_child_to_cur("left rear paw")
   scene_tree.add_child_to_cur("spare mutant paw")
   scene_tree.add_child_to_cur("wagging tail")

   # add some parts to table
   scene_tree.find("table")
   scene_tree.add_child_to_cur("north east leg")
   scene_tree.add_child_to_cur("north west leg")
   scene_tree.add_child_to_cur("south east leg")
   scene_tree.add_child_to_cur("south west leg")

   print( "\n------------ Loaded Tree --------------- \n", scene_tree )

   # test of deep copy and soft deletion --------------------------
   my_copy = copy.deepcopy(scene_tree)

   # remove some real and imagined parts from original
   scene_tree.remove("spare mutant paw")
   scene_tree.remove("Miguel the human")
   scene_tree.remove("an imagined higgs boson")
   scene_tree.remove("torso")

   print( "\n----------- Virtual Tree ------------ \n", scene_tree )
   print( "\n----------- Physical Tree ------------ \n",
          scene_tree.str_physical() )

   print( "\n----------- Miguel and Torsso should be gone ------------ \n" )
   if scene_tree.find("Miguel the Human"):
      print( "bad" )
   else:
      print( "good" )

   if scene_tree.find("thumb"):
      print( "bad" )
   else:
      print( "good" )

   if scene_tree.find("torso"):
      print( "bad" )
   else:
      print( "good" )

   if scene_tree.find("Miguel the human"):
      print( my_copy.find("Miguel the human") )
      print( "bad" )
   else:
      print( "good" )

   print( "\n------- Testing Sizes (compare with above) ------ \n" )
   print( "\nvirtual (soft) size:", scene_tree.size() )
   print( "\nphysical (hard) size:", scene_tree.size_physical() )

   print( "\n------------ Collecting Garbage ------------ \n" )
   print( "found soft-deleted nodes?", scene_tree.collect_garbage() )
   print( "immediate collect again?", scene_tree.collect_garbage() )
   print( "-------- Hard Display after garb col ----------\n",
          scene_tree.str_physical() )

   print( "Semi-deleted tree empty? " +  str(scene_tree.empty()) )
   scene_tree.remove("room")
   print( "Completely-deleted tree empty? " +  str(scene_tree.empty()) )


   print( "\n------------ Cloned Tree? ------------ \n" )
   # remove and add some parts of copy and compare with original
   my_copy.remove("left rear paw")
   my_copy.find("Miguel the human")
   my_copy.add_child_to_cur("head")
   my_copy.find_in_cur_subtree("torso")
   my_copy.remove_at_cur()

   print( "\n----------- Virtual Tree ------------ \n", my_copy )
   print( "\n----------- Physical Tree ------------ \n",
          my_copy.str_physical() )

   print( "\n------------ Testing find() ------------ \n" )
   if my_copy.find("table"):
      print( "good" )
   else:
      print( "bad" )

   if my_copy.find("spare mutant paw"):
      print( "good" )
   else:
      print( "bad" )

   if my_copy.find("an imagined higgs boson"):
      print( "bad" )
   else:
      print( "good" )

   # will find Lily's torso
   if my_copy.find("torso"):
      print( "good" )
   else:
      print( "bad" )

   # won't find Miguels's torso
   my_copy.find("Miguel the Human")
   if my_copy.find_in_cur_subtree("torso"):
      print( "bad" )
   else:
      print( "good" )

   #  remove Lily, and search for torso  (should fail)
   my_copy.find("Lily the canine")
   my_copy.remove_at_cur()
   if my_copy.find("torso"):
      print( "bad" )
   else:
      print( "good" )

   if my_copy.find("pinky"):
      print( "bad" )
   else:
      print( "good" )
# END CLIENT main()  -------------------------------------------
# BEGIN CLASS FhTreeNode -------------------------------------------
class FhTreeNode:
   """ FhTreeNode class for a FhTree - not designed for 
       general clients, so no accessors or exception raising """

   # initializer ("constructor") method ------------------------
   def __init__(self,
                sib = None, first_child = None, prev = None,
                root = None):
      # instance attributes
      self.sib, self.first_child, self.prev, self.my_root \
         = sib, first_child, prev, root

   # stringizer ----------------------------------------------
   def __str__(self):
      return "(generic tree node)"

# END CLASS FhTreeNode -------------------------------------------
# BEGIN CLASS FhTree -------------------------------------------
# noinspection PyAttributeOutsideInit
class FhTree:
   """ FhTree is our base class for a data-filled general trees """

   # static constant helpers for stringizer
   BLANK_STRING = "                                    "
   BLANK_STR_LEN = len(BLANK_STRING)

   # constructor ------------------------------------------------
   def __init__(self):
      self.clear()

   # accessors --------------------------------------------------
   def empty(self):
      """ traditionally, is_empty() is just called empty() """
      return (self.size() == 0)

   def size(self):
      """ traditionally, get() for size is just siae() """
      return self.m_size

   # current pointer mutators --------------------------------------
   def reset_cur(self):
      self.current = self.m_root

   def set_cur(self, tree_node):
      if not self.valid_node_in_tree(tree_node):
         self.current = None
         return False
      # else
      self.current = tree_node
      return True

   # tree mutators --------------------------------------------------
   def clear(self):
      self.m_root = None
      self.m_size = 0
      self.reset_cur()

   def remove_node_rec(self, node_to_delete):
      """ node_to_delete points to node in tree to be removed
          (along w/entire subtree). deletes children recursively
          errors handled by caller (remove_at_cur()) """

      ntd = node_to_delete    # alias for shorter lines
      # remove all the children of this node (need loop unfortunately)
      while ntd.first_child:
         self.remove_node_rec(ntd.first_child)

      # we have a non-null prev pointer
      # either it has a left sib ...
      if ntd.prev.sib == node_to_delete:
         ntd.prev.sib = node_to_delete.sib
      # ... or it's the first_child of some parent
      else:
         ntd.prev.first_child = ntd.sib

      # deal with a possible right sib
      if ntd.sib != None:
         ntd.sib.prev = ntd.prev

      # node is now out of the tree (Python will g.c. if appropriate)
      # wipe the fields to prevent client from doing harm
      ntd.first_child, ntd.prev, ntd.sib, ntd.my_root \
         = None, None, None, None

      # finally, update tree size
      self.m_size -= 1

   def remove_at_cur(self):
      """ calls remove_node() passing cur, and resets cur
         handles all errors here to avoid repetition in rec call """

      ntd = self.current    # saves cur so we can reset early
      self.reset_cur()      # no matter what, we'll return fresh cur

      # bad current or empty tree
      if not self.valid_node_in_tree(ntd) or self.size() == 0:
         return False

      # deleting root?
      if ntd.prev == None:
         self.clear()
         return True

      # since we know this node is in tree, call will succeed
      self.remove_node_rec(ntd)
      return True

   def add_child_node_to_cur(self, to_add = None):
      """ 'push' node_to_add as new first child of parent.
           return None (error) or ref to newly created node
           expect parent == None IFF tree is empty """

      if not self.valid_node_to_add(to_add):
         return False

      # empty tree
      if self.m_size == 0:
         self.m_root = to_add
         self.m_root.my_root = self.m_root
         self.m_size = 1
         self.reset_cur()     # for empty tree we ignore what cur *was*
         return True

      if not self.valid_node_in_tree(self.current):
         return False

      # "push" new_node as the head of the sibling list; adjust all ptrs
      # notice "None": any "subtree: hanging off to_add, is trimmed

      cur = self.current   # for brevity...
      ta = to_add          # ... of next block

      ta.sib, ta.first_child, ta.prev, ta.my_root \
         =  cur.first_child, None, cur, self.m_root
      cur.first_child = ta
      if ta.sib != None:
         ta.sib.prev = ta
      self.m_size += 1
      return True

   # stringizers ------------------------------------------------
   def __str__(self):
      ret_str = "The Tree -----------------------\n" \
                + self.str_recurse(self.m_root, 0) \
                + "---------- End of Tree --------\n"

      return ret_str

   def str_recurse(self, tree_node, level = 0):
      """ recursive tree stringizer (with indentation)
          for subtree with root tree_node in this instance's tree """

      ret_str = ""

      # multi-purpose termination:  error, None or not-in-self 
      if not self.valid_node_in_tree(tree_node):
         return ret_str

      # stop runaway indentation, otherwise set indent for this level
      if  level > self.BLANK_STR_LEN - 1:
         return self.BLANK_STRING +  " ... "

      # this call's node
      indent = self.BLANK_STRING[0:level]
      ret_str += (indent + str(tree_node) + "\n")

      # recurse over children
      ret_str += self.str_recurse(tree_node.first_child, level + 1)

      # recurse over siblings
      if level > 0:
         ret_str += self.str_recurse( tree_node.sib, level )

      return ret_str

   # helpers ---------------------------------------
   def valid_node_to_add(self, am_i_valid):
      """ insists that node is an FhTreeNode """
      if (not isinstance(am_i_valid, FhTreeNode)):
         return False
      return True

   def valid_node_in_tree(self, am_i_valid):
      """ insists that node is an FhTreeNode AND in this tree """
      if (not isinstance(am_i_valid, FhTreeNode)) \
            or (am_i_valid.my_root != self.m_root):
         return False
      return True

   # END CLASS FhTree ----------------------------------------
# BEGIN CLASS FhDataTreeNode ----------------------------------------
class FhDataTreeNode(FhTreeNode):
   """ FhDataTreeNode subclass of FhTreeNode. 
   It is the node class for a data tree.
   Requires data item, x, be vetted by client (FhDataTree) """

   # constructor ------------------------------------------------
   def __init__(self, x,
                sib = None, first_child = None, prev = None,
                root = None):

      # first chain to base class
      super().__init__(sib, first_child, prev, root)

      # added attribute
      self.data = x

   # stringizer(s) ----------------------------------------------
   # ultimate client, main(), can provide data stringizer if needed
   def __str__(self):
      return str(self.data)

# END CLASS FhDataTreeNode ----------------------------------------
# BEGIN CLASS FhDataTree ----------------------------------------
class FhDataTree(FhTree):
   """ FhDataTree subclass of FhTree """
   # default type is string
   DEFAULT_TYPE = type("")

   # constructor -----------------------------------------------
   def __init__(self, tree_type = None):
      super().__init__()
      self.set_tree_type(tree_type)

   # current pointer mutators --------------------------------------
   def find(self, x):
      """ look for x in entire tree.
          if found and valid, current will point to it and return T,
          else current None and return F (all done by find_rec())"""

      self.reset_cur()
      return self.find_in_cur_subtree(x)

   def find_in_cur_subtree(self, x):
      """ look for x in subtree rooted at self.current.
         if x valid and found, current will point to it and return T,
         else current None and return F """

      if not self.current or not self.valid_data(x):
         return False

      return (self.find_rec(x, self.current) != None)

   def find_rec(self, x, root):
      """ recursively search for x in subtree rooted at root.
         if found, current set to node and returned,
         else current/return = None.
         x and current vetted by non-recursive originator """

      # default current if all recursive calls fail
      self.current = None

      # not found (in this sub-search)
      if not root:
         return None

      # found (current will survive all higher-level calls)
      if root.data == x:
         self.current = root
         return root

      # recurse children
      child = root.first_child
      while child:
         test_result = self.find_rec(x, child)
         if test_result:
            return test_result
         child = child.sib

      return None

   # tree mutators --------------------------------------------------
   def set_tree_type(self, the_type):
      # make sure it's a subclass of type
      if isinstance(the_type, type):
         self.tree_type = the_type
      else:
         self.tree_type = self.DEFAULT_TYPE

   def remove(self, x):
      """ looks for x in entire tree.
         if valid and found, remove node, return T (cur reset by base
         call, remove_at_cur()). else curr = None and return F """

      self.current = None   # prepare for not found or error return
      if self.size() == 0 or (not self.valid_data(x)):
         return False

      found_node = self.find_rec(x, self.m_root)
      if not found_node:
         return False

      # found x
      self.current = found_node
      self.remove_at_cur()    # not overriden, so base call
      return True

   def add_child_to_cur(self, x):
      """ calls base add_child_node_to_cur(). no change to cur """
      if not self.valid_data(x):
         return False

      new_node = FhDataTreeNode(x)
      return( super().add_child_node_to_cur(new_node) )

   # helpers -------------------------------------------------
   def valid_data(self, am_i_valid):
      if not isinstance(am_i_valid, self.tree_type):
         return False
      #else
      return True
# BEGIN CLASS FhSdTreeNode -------------------------------------------
class FhSdTreeNode(FhTreeNode):
   def __init__(self, sib = None, first_child = None, prev = None, root = None, dltd = False):
      super().__init__(sib, first_child, prev, root)
      if isinstance(dltd, bool):
         self.dltd = dltd
      else:
         self.dltd = False


# END CLASS FhSdTreeNode -------------------------------------------
# BEGIN CLASS FhSdTree -------------------------------------------
class FhSdTree(FhTree):
   def __init__(self):
      super().__init__()

   def empty(self):
      """ traditionally, is_empty() is just called empty() """
      return (self.size() == 0)

   def size(self):
      """ traditionally, get() for size is just siae() """
      return self.size_rec(self.m_root)

   def size_rec(self, tree_node, level=0):
      """ recursive function that gets size of tree excluding "deleted" nodes"""
      count = 0

      # skips to return at bottom if tree_node == None
      if tree_node is not None:
         # if node not marked deleted iterate count and recuresively call first_child
         if not tree_node.dltd:
            count += 1
            if tree_node.first_child:
               count += self.size_rec(tree_node.first_child, level + 1)
         # if node is not root of sub-tree being searched, check sibling
         if level > 0 and tree_node.sib:
            count += self.size_rec(tree_node.sib, level)
      return count

   def set_cur(self, tree_node):
      if not self.valid_node_in_tree(tree_node) or tree_node.dltd:
         self.current = None
         return False
      # else
      return super().set_cur(tree_node)

   def add_child_node_to_cur(self, to_add = None):
      """check if node_to_add is valid/not deleted and (current is valid/not deleted or m_size == 0)
      if checks passed calls overriden method. Will duplicate some checks, but avoids code duplication.
      Aware of small performance hit and would re-think if it became a problem"""

      if self.valid_node_to_add(to_add) and not to_add.dltd \
            and ((self.valid_node_in_tree(self.current) and not self.current.dltd) or self.m_size == 0):
         return super().add_child_node_to_cur(to_add)
      # else
      return False

   def remove_at_cur(self):
      """ If not already deleted sets dltd flag to True, and resets cur
         handles all errors here to avoid repetition in rec call """

      ntd = self.current    # saves cur so we can reset early
      self.reset_cur()      # no matter what, we'll return fresh cur

      # bad current or empty tree
      if not self.valid_node_in_tree(ntd) or self.size() == 0 or self.current.dltd == True:
         return False

      # if ntd is root, call clear(), otherwise set curr.dltd to True
      if ntd == self.m_root:
         self.clear()
      else:
         ntd.dltd = True
      return True

   def size_physical(self):
      """"size of tree including deleted nodes"""
      return self.m_size

   def collect_garbage(self):
      return self.collect_garbage_rec(self.m_root)

   def collect_garbage_rec(self, tree_node):
      if not self.valid_node_in_tree(tree_node):
         return False

      # flag to return
      dltd_node = False

      # go to last sibling first
      if tree_node.sib:
         dltd_node = self.collect_garbage_rec(tree_node.sib)

      # node marked deleted -- delete and return True
      if tree_node.dltd:
         self.remove_node_rec(tree_node)
         return True

      # visit first child
      if tree_node.first_child:
         dltd_node = dltd_node or self.collect_garbage_rec(tree_node.first_child)

      return dltd_node

   def str_recurse(self, tree_node, level = 0):
      """ recursive tree stringizer (with indentation)
            for subtree with root tree_node in this instance's tree """

      ret_str = ""

      # multi-purpose termination:  error, None or not-in-self
      if not self.valid_node_in_tree(tree_node):
         return ret_str

      # stop runaway indentation, otherwise set indent for this level
      if  level > self.BLANK_STR_LEN - 1:
         return self.BLANK_STRING +  " ... "

      # if tree_node not deleted add string to ret_str and visit children
      if not tree_node.dltd:
         # this call's node
         indent = self.BLANK_STRING[0:level]
         ret_str += (indent + str(tree_node) + "\n")

         # recurse over children
         ret_str += self.str_recurse(tree_node.first_child, level + 1)

      # recurse over siblings, add returned value
      if level > 0:
         ret_str += self.str_recurse( tree_node.sib, level )

      return ret_str

   def str_physical(self):
      ret_str = "The Physical Tree -----------------------\n" \
                + self.str_recurse_phys(self.m_root, 0) \
                + "---------- End of Physical Tree --------\n"
      return ret_str


   def str_recurse_phys(self, tree_node, level = 0):
      """ recursive tree stringizer (with indentation)
          for subtree with root tree_node in this instance's tree """

      ret_str = ""

      # multi-purpose termination:  error, None or not-in-self
      if not self.valid_node_in_tree(tree_node):
         return ret_str


      # stop runaway indentation, otherwise set indent for this level
      if level > self.BLANK_STR_LEN - 1:
         return self.BLANK_STRING +  " ... "

      # this call's node

      indent = self.BLANK_STRING[0:level]
      if tree_node.dltd:
         del_str = " (D)"
      else:
         del_str = ""
      ret_str += (indent + str(tree_node) + del_str + "\n")

      # recurse over children
      ret_str += self.str_recurse_phys(tree_node.first_child, level + 1)

      # recurse over siblings
      if level > 0:
         ret_str += self.str_recurse_phys( tree_node.sib, level )

      # note as deleted if needed
      return ret_str

   # helpers --------------------------------------- refactored to chech for instance of FHSdTreeNode
   def valid_node_to_add(self, am_i_valid):
      """ insists that node is an FhTreeNode """
      if not isinstance(am_i_valid, FhSdTreeNode):
         return False
      return True

   def valid_node_in_tree(self, am_i_valid):
      """ insists that node is an FhTreeNode AND in this tree """
      if (not isinstance(am_i_valid, FhSdTreeNode)) \
            or (am_i_valid.my_root != self.m_root):
         return False
      return True

# END CLASS FhSdDataTreeNode -------------------------------------------
# BEGIN CLASS FhSdDataTree -------------------------------------------
class FhSdDataTreeNode(FhDataTreeNode, FhSdTreeNode):
   def __init__(self, x, sib = None, first_child = None, prev = None, root = None, dltd = False):
      # first chain to base class
      FhDataTreeNode.__init__(self, x, sib, first_child, prev, root)
      FhSdTreeNode.__init__(self, dltd=dltd)

      # added attribute
# END CLASS FhSdDataTree -------------------------------------------
class FhSdDataTree(FhSdTree, FhDataTree):
   """ FhDataTree subclass of FhSdTree, FhDataTree """
   # default type is string

   def __init__(self, tree_type = None):
      FhSdTree.__init__(self)
      FhDataTree.__init__(self, tree_type)

   def find_rec(self, x, root):
      """ recursively search for x in subtree rooted at root.
         if found, current set to node and returned,
         else current/return = None.
         x and current vetted by non-recursive originator """

      # default current if all recursive calls fail
      self.current = None

      # not found (in this sub-search)
      if not root:
         return None

      # found (current will survive all higher-level calls)
      # if root.dltd do not do any further checks or visit children
      if not root.dltd:
         if root.data == x:
            self.current = root
            return root

         # recurse children
         child = root.first_child
         while child:
            test_result = self.find_rec(x, child)
            if test_result:
               return test_result
            child = child.sib

      return None

   def add_child_to_cur(self, x):
      """ calls base add_child_node_to_cur(). no change to cur """
      if not self.valid_data(x):
         return False

      new_node = FhSdDataTreeNode(x)
      return self.add_child_node_to_cur(new_node)


# END CLASS FhSdTree -------------------------------------------
# -------------- main program -------------------
if __name__ == "__main__":
   main()
"""ASSIGNMENT 10 RUN
Starting tree empty? True

------------ Loaded Tree --------------- 
 The Tree -----------------------
room
 table
  south west leg
  south east leg
  north west leg
  north east leg
 Miguel the human
  torso
   right arm
    right hand
     pinky
     ring finger
     middle finger
     index finger
     thumb
   left arm
    left hand
     pinky
     ring finger
     middle finger
     index finger
     thumb
 Lily the canine
  torso
   wagging tail
   spare mutant paw
   left rear paw
   right rear paw
   left front paw
   right front paw
---------- End of Tree --------


----------- Virtual Tree ------------ 
 The Tree -----------------------
room
 table
  south west leg
  south east leg
  north west leg
  north east leg
 Lily the canine
---------- End of Tree --------


----------- Physical Tree ------------ 
 The Physical Tree -----------------------
room
 table
  south west leg
  south east leg
  north west leg
  north east leg
 Miguel the human (D)
  torso
   right arm
    right hand
     pinky
     ring finger
     middle finger
     index finger
     thumb
   left arm
    left hand
     pinky
     ring finger
     middle finger
     index finger
     thumb
 Lily the canine
  torso (D)
   wagging tail
   spare mutant paw (D)
   left rear paw
   right rear paw
   left front paw
   right front paw
---------- End of Physical Tree --------


----------- Miguel and Torsso should be gone ------------ 

good
good
good
good

------- Testing Sizes (compare with above) ------ 


virtual (soft) size: 7

physical (hard) size: 30

------------ Collecting Garbage ------------ 

found soft-deleted nodes? True
immediate collect again? False
-------- Hard Display after garb col ----------
 The Physical Tree -----------------------
room
 table
  south west leg
  south east leg
  north west leg
  north east leg
 Lily the canine
---------- End of Physical Tree --------

Semi-deleted tree empty? False
Completely-deleted tree empty? True

------------ Cloned Tree? ------------ 


----------- Virtual Tree ------------ 
 The Tree -----------------------
room
 table
  south west leg
  south east leg
  north west leg
  north east leg
 Miguel the human
  head
 Lily the canine
  torso
   wagging tail
   spare mutant paw
   right rear paw
   left front paw
   right front paw
---------- End of Tree --------


----------- Physical Tree ------------ 
 The Physical Tree -----------------------
room
 table
  south west leg
  south east leg
  north west leg
  north east leg
 Miguel the human
  head
  torso (D)
   right arm
    right hand
     pinky
     ring finger
     middle finger
     index finger
     thumb
   left arm
    left hand
     pinky
     ring finger
     middle finger
     index finger
     thumb
 Lily the canine
  torso
   wagging tail
   spare mutant paw
   left rear paw (D)
   right rear paw
   left front paw
   right front paw
---------- End of Physical Tree --------


------------ Testing find() ------------ 

good
good
good
good
good
good
good

Process finished with exit code 0

"""