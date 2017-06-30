# Lab documentation #

## Lab ##

### usage ###

```python
@lab.setup("lab-name", []) # list of resources
def setup(proj):
    print "project setup to go here"
```

### description###

A Lab is considered a top-level object and represents the entire project. There is no limit to the number of labs you can have in a single file but generally it is one per project. Labs contain all the Resource objects that the project has access to these can be as ambiguous as files or as specific as C artifacts.

---

*not all of the things documented here are fully or even partial implemented so be wary of what you use*

