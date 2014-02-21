Title: Creating a Custom Section in Umbraco 6 - Part 2: The Tree
Date: 2013-07-17 13:53:32
Slug: creating-a-custom-section-in-umbraco-6-part-2-the-tree
Tags: umbraco

The tree needs a little bit more work to implement than the application.

Here is the initial class declaration.

    [Tree("appAlias", "treeAlias", "Tree Title")]
    public class MyApplicationTree : ITree
    {
    }

### Tree Attribute

The Tree attribute takes similar parameters to the Application attribute.

<dl>
<dt>appAlias</dt>
<dd>The alias of the application this tree belongs too.</dd>
<dt>alias</dt>
<dd>The alias for this tree.</dd>
<dt>title</dt>
<dd>The title of the tree, not entirely sure if this is used.</dd>
</dl>

### ITree

This has a few properties and methods we need to implement.

    public interface ITree
    {
        string app { set; }
        int id { set; }
        void Render(ref XmlDocument Tree);
        void RenderJS(ref StringBuilder Javascript);
    }

The first two are easily implemented with an automatic properties.

    public string app { get; set; }
    public int id { get; set; }

We use the RenderJS method to add javascript to the backoffice that will allow us to change the content on the right hand side frame. We will call this when we click on a node in the tree.

    public void RenderJS(ref StringBuilder javascript)
    {
        javascript.Append(@"function openLocation(url) { parent.right.document.location.href = url; }");
    }

Lastly we need to build our actual tree in the Render method. We need to build it in an XmlDocument and it's fairly straightforward once you've done it a few times.

    public void Render(ref XmlDocument tree)
    {
        // Add our base elements
        XmlNode root = tree.DocumentElement;

        if (this.id == -1)
        {
            // Get data from somewhere or create a static tree root
            // Add 10 nodes for an example
            for (int i = 1; i <= 10; i ++)
            {
                XmlElement treeElement = tree.CreateElement("tree");
                treeElement.SetAttribute("menu", string.Empty);
                treeElement.SetAttribute("nodeID", i.ToString());
                treeElement.SetAttribute("text", i.ToString());
                treeElement.SetAttribute("action", string.Format("javascript:openLocation('/Path/To/Document.aspx?id={0}');", i));
                treeElement.SetAttribute("src", string.Empty);
                treeElement.SetAttribute("icon", "myClosedIcon.png"); // Icons go in ~/Umbraco/Images/Umbraco/
                treeElement.SetAttribute("openIcon", "myOpenIcon.png");
                treeElement.SetAttribute("nodeType", "tree");
                	
                root.AppendChild(treeElement);
            }
        }
        else
        {
            // We'll come to this later.
        }
    }

This should create 10 nodes in your tree, you will probably want to switch this to get data from a database or something similar. Or you may have a few static root nodes that then load data when expanded.
Child Nodes

To load child nodes in a tree, you call the tree again with the id of the parent node. This is where that if (this.id == -1) comes in. You set the tree to call in the src attribute of the node.

    treeElement.SetAttribute("src", this.GetServiceUrl(i));

    // ... snip ...

    private string GetServiceUrl(int nodeId)
    {
        TreeService treeService = new TreeService(nodeId, "treeAlias", false, false, TreeDialogModes.fulllink, this.app);
        return treeService.GetServiceUrl();
    }

We then catch this like so:

    public void Render(ref XmlDocument tree)
    {
        // Add our base elements
        XmlNode root = tree.DocumentElement;
        
        if (this.id == -1)
        {
            // Get data from somewhere or create a static tree root
            // Add 10 nodes for an example
            for (int i = 1; i <= 10; i ++)
            {
                XmlElement treeElement = tree.CreateElement("tree");
                treeElement.SetAttribute("menu", string.Empty);
                treeElement.SetAttribute("nodeID", i.ToString());
                treeElement.SetAttribute("text", i.ToString());
                treeElement.SetAttribute("action", string.Format("javascript:openLocation('/Path/To/Document.aspx?id={0}');", i));
                treeElement.SetAttribute("src", string.Empty);
                treeElement.SetAttribute("icon", "myClosedIcon.png"); // Icons go in ~/Umbraco/Images/Umbraco/
                treeElement.SetAttribute("openIcon", "myOpenIcon.png");
                treeElement.SetAttribute("nodeType", "tree");
                
                root.AppendChild(treeElement);
            }
        }
        else
        {
            // Get items that have a parent node of this.id
            // Just as an example
            XmlElement childElement = tree.CreateElement("tree");
            childElement.SetAttribute("menu", string.Empty);
            childElement.SetAttribute("nodeID", 99);
            childElement.SetAttribute("text", "Child of " + this.id.ToString());
            childElement.SetAttribute("action", string.Format("javascript:openLocation('/Path/To/AnotherDocument.aspx?id={0}');", this.id));
            childElement.SetAttribute("src", string.Empty);
            childElement.SetAttribute("icon", "icon.png");
            childElement.SetAttribute("openIcon", "icon.png");
            childElement.SetAttribute("nodeType", "tree");
            
            root.AppendChild(childElement);
        }
    }

### Need More Node Ids?

The basic tree works really well if you have a unique Id for every item and hierarchy is defined within that by parent Ids, like the content in Umbraco content. But if you need multiple roots nodes, each showing items that may have conflicting Ids, then you can add another tree.

By default all trees for an application will be added to the root, this might be what you want, but if it's not, there is an overload for the Tree attribute to stop it being loaded.

    [Tree("appAlias", "treeAlias", "My Child Tree", ".sprTreeFolder", ".sprTreeFolder_o", "", false, false)]

It's the last boolean parameter which tells Umbraco not to initialize the tree, so it won't be added to the root. You can then change your src attributes on your nodes to point to the new tree.

    private string GetTreeServiceUrl(string treeAlias, int nodeId)
    {
        TreeService treeService = new TreeService(nodeId, treeAlias, false, false, TreeDialogModes.fulllink, this.app);
        return treeService.GetServiceUrl();
    }

### Context Menus

You can control the context menu available on a node by setting the menu attribute on the node. This isn't something I have implemented yet, there is more information for this available here.
