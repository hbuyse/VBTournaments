# CHEAT SHEET

## Access dictionary

The Django template language supports looking up dictionary keys as follows:

```python
{{ json.key1 }}
```

See the template docs on variables and lookups.

The template language does not provide a way to display **json[key]**, where **key** is a variable.
You can write a template filter to do this, as suggested in the answers to this [Stack Overflow question](http://stackoverflow.com/questions/8000022/django-template-how-to-lookup-a-dictionary-value-with-a-variable)


## Following relationships “backward”

If a model has a ForeignKey, instances of the foreign-key model will have access to a Manager that returns all instances of the first model.
By default, this Manager is named FOO_set, where FOO is the source model name, lowercased.
This Manager returns QuerySets, which can be filtered and manipulated as described in the “Retrieving objects” section above.

Example:
```python
>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all() # Returns all Entry objects related to Blog.

# b.entry_set is a Manager that returns QuerySets.
>>> b.entry_set.filter(headline__contains='Lennon')
>>> b.entry_set.count()
```

You can override the FOO_set name by setting the related_name parameter in the ForeignKey definition.
For example, if the Entry model was altered to blog = ForeignKey(Blog, related_name='entries'), the above example code would look like this:
```python
>>> b = Blog.objects.get(id=1)
>>> b.entries.all() # Returns all Entry objects related to Blog.

# b.entries is a Manager that returns QuerySets.
>>> b.entries.filter(headline__contains='Lennon')
>>> b.entries.count()
```



## [Built-in template tags and filters](https://docs.djangoproject.com/en/1.8/ref/templates/builtins)

### linebreaks

Replaces line breaks in plain text with appropriate HTML; a single newline becomes an HTML line break (`<br />`) and a new line followed by a blank line becomes a paragraph break (`</p>`).

Example:
```python
{{ value|linebreaksbr }}
```
If value is `Joel\nis a slug`, the output will be `<p>Joel<br />is a slug</p>`.


### safe

Marks a string as not requiring further HTML escaping prior to output.
When autoescaping is off, this filter has no effect.

> Note
> 
> If you are chaining filters, a filter applied after safe can make the contents unsafe again.
> For example, the following code prints the variable as is, unescaped:
> ```python
> {{ var|safe|escape }}
> ```



## Using Pytest for Django

Create in the project directory a file called pytest.ini.
It is a configuration file for pytest.

```ini
[pytest]
DJANGO_SETTINGS_MODULE = vbtournaments.settings

minversion = 2.6.4

python_files = test_*.py
```

You can launch PyTest with the command
```sh
$ py.test
```
