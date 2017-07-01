# Lab documentation #

## Lab ##

### usage ###

```python
@lab.setup("lab-name", []) # list of resources
def setup(proj):
    print "project setup to go here"
```

### description ###

A Lab is considered a top-level object and represents the entire project. There is no limit to the number of labs you can have in a single file but generally it is one per project. Labs contain all the Resource objects that the project has access to these can be as ambiguous as files or as specific as C artifacts.

### Too long don't read ###

the main purpose for the Lab class is to merely contain a suite of tasks and Resources that can be manipulated in order to create a general purpose build system with little constraints.

## Selector ##

### usage ###

```python
MySelector = Utilities.Selector(MyResourceList)
print MySeletor.MyResource.fetch()[0].name
```

if MyResource is the name of a Resource belonging to MyResourceList the above will print "MyResource" otherwise it will throw an error because the empty list has no 0 index.

### description ###

The Selector class serves as a way to search complex Resource structures by their properties. In future more methods like filter (which will search everything that fulfills the requirements of a function) will be added to enhance this feature.

---

*not all of the things documented here are fully or even partial implemented so be wary of what you use*
