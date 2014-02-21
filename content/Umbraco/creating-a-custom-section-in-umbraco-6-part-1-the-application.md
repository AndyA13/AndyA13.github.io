Title: Creating a Custom Section in Umbraco 6 - Part 1: The Application
Date: 2013-07-16 13:28:42
Slug: creating-a-custom-section-in-umbraco-6-part-1-the-application
Tags: umbraco

I’ve been doing a bit of work lately creating a custom section in an Umbraco v6.1 install. I needed a nice tree for my custom section, so after a lot of googling and digging through the Umbraco source, I managed to get it all working nicely.  I’ve put this guide together to hopefully make the process a little easier for myself and any other weary internet travellers who happen to stumble upon it.

### The Application

This is much easier now in version 6, to add a new application you just new to create a class that implements umbraco.interfaces.IApplication and has the Application attribute.

    [Application("alias", "Real Name", "images/nada.gif", 10)]
    public class MyApplication : IApplication
    {
    }

### IApplication

This interface actually has no definitions, so it’s a piece of cake to implement :)

### Application Attribute

This takes a few parameters:

<dl>
<dt>alias</dt>
<dd>Your application alias, usually starts lowercase eg “myApplication”</dd>
<dt>name</dt>
<dd>The nice name for your application, e.g. “My Application”</dd>
<dt>icon</dt>
<dd>The icon to be displayed in umbraco, you’ll need to do a bit of css jiggery pokery to get it right. I’ve used nada then added my icon to the existing tray sprite and added a css class to position it.</dd>
<dt>sortOrder</dt>
<dd>You can put it at the start or in between existing apps, I set mine to 10 to make sure it was at the end.</dd>
</dl>

### applications.config

That should be your app set up, when you first run umbraco after creating that class, it should update the ~/config/applications.config automatically for you. I’ve found changing anything defined in the Application attribute after this point won’t be reflected in the applications.config, so if you need to make any changes, remember check that the applications.config reflects the new values.
Application Name

At the top of the tree on your application page, you will see that it is showing your application alias instead of the name, to update this you need to add a key setting to ~/umbraco/Config/Lang/en.xml (swapping “en” for whatever language you are using).

    <area alias="sections">
        ...
        <!-- Add this line -->
        <key alias="myApplication">My Application</key>
    </area>

Your app should now have a nice name.

I will post a guide to the trees later this week.


