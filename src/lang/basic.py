'''
Created on Aug 9, 2015

Basic representation language constructs

@author: karurosu
'''
from exceptions import LangParseException

class token(object):
    """
    A single token, either a variable, a property or an atom
    """
    def __init__(self):
        self.name = None
        
    def __eq__(self, other):
        if isinstance(other, token):
            return self.name == other.name
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return self.name

class variable(token):
    """
    A variable, it is a token of the name var-<name> and a separate property called varname.
    """
    def __init__(self, name="unnamed"):
        super(variable, self).__init__()
        self.name = 'var-'+name
        self.varname = name
    
    def __eq__(self, other):
        if isinstance(other, token):
            return True
        return False

class category(object):
    """
    A category, always represented by its head and a body.
    head is always an atom, body can be an atom, a list of atoms or a variable
    """
    def __init__(self, *args):
        self.header = None
        self.body = set(args)
    
    def __eq__(self, other):
        if isinstance(other, category):
            return self.header == other.header
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return str(self.header)

class status(object):
    """
    represents the current status of the world, a STATUS(X) class.
    It has a category and a value.
    """
    def __init__(self, cat, value):
        if not isinstance(cat, category):
            raise LangParseException("Status must have a category")
        self.category = cat
        self.value = value
        self.negated = False
        self.variable = isinstance(self.value, variable)
        
    def isVariable(self):
        return self.variable
    
    def __neg__(self):
        self.negated = not self.negated
        return self
    
    def __eq__(self, other):
        if isinstance(other, status):
            return self.category == other.category and self.value == other.value
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return "status({0},{1})".format(self.category,self.value)
        
class compositeSet(object):
    """
    Represents a two piece set, used for post conditions and preconditions.
    It has a positive set and a negative set
    """
    def __init__(self, *args):
        self.positive = []
        self.negative = []
        
        for clause in args:
            if clause.isVariable():
                raise LangParseException("Compositeset must always be fully defined, no variables allowed.")
            if clause.negated:
                self.negative.append(clause)
            else:
                self.positive.append(clause)

class statusSet(object):
    def __init__(self, initial = None):
        if initial is None:
            self.values = []
        else:
            self.values = initial
    
    def __contains__(self, clause):
        """
        Check if the specified status is contained in the world
        """
        for st in self.values:
            if clause == st:
                return True
        return False
    
    def add(self, clause):
        if clause in self:
            return
        
        self.values.append(clause)
    
    def extend(self, iterable):
        for i in iterable:
            self.add(i)
    
    def remove(self, clause):
        out = []
        
        for st in self.values:
            if st == clause:
                continue
            out.append(st)
        
        self.values = out
    
    def clone(self):
        return statusSet(list(self.values))
    
    def clear(self):
        self.values = []
    
    def __iter__(self):
        return iter(self.values)
    
    def __len__(self):
        return len(self.values)
    
    def __str__(self):
        return ",".join([str(x) for x in self.values])

class rule(object):
    def __init__(self, head, function):
        if not isinstance(head, status):
            raise LangParseException("Head must be an status instance")
        self.head = head
        self.body = None
        self.function = function
    
    def verify(self, world):
        return False
    
    def __str__(self):
        return "{0}({1})".format(self.function,str(self.head))

class unique(rule):
    def __init__(self, head):
        #allow to pass simply a category
        if isinstance(head, category):
            head = status(head, variable())
        
        super(unique, self).__init__(head,"unique")
        
        if not self.head.isVariable():
            raise LangParseException("Head must have a variable")
    
    def verify(self, status):
        found = 0
        for st in status:
            if st == self.head:
                found += 1
                if found > 1:
                    return False
        return True

class depends(rule):
    def __init__(self, head):
        rule.__init__(self, head, "depends")
        self.body = []
    
    def And(self, clause):
        if not isinstance(clause, status):
            raise LangParseException("Clause must be an status instance")
        
        self.body.append(clause)
        return self
    
    def verify(self, status):
        #first check if the head is present
        if self.head not in status:
            return True
        
        for clause in self.body:
            r = clause in status
            if (clause.negated and r) or (not clause.negated and not r):
                return False
            
        return True

class rules(object):
    def __init__(self):
        self.rules = []
    
    def unique(self, head):
        i = unique(head)
        self.rules.append(i)
        return i
    
    def depends(self, head):
        i = depends(head)
        self.rules.append(i)
        return i
    
class World(object):
    """
    A representation of the world, holds generation rules, tokens and relationships
    """
    def __init__(self):
        self.tokens = {}
        self.generationRules = {}
        self.representationRules = []
        self.status = statusSet()
    
    def __str__(self):
        return ",".join([str(st) for st in self.status])
            
        
    
    def compatible(self, conditions):
        for condition in conditions:
            r = condition in self.status
            if (condition.negated and r) or (not condition.negated and not r):
                return False
        return True
    
    def modify(self, composite_set):
        """
        Alter the world by applying a composite_set.
        Validate rules, returns True if the change was successful, false if it is not compatible
        """
        old = self.status.clone()
        
        for newclause in composite_set.positive:
            self.status.add(newclause)
        
        for removeclause in composite_set.negative:
            self.status.remove(removeclause)
            
        if self.validate():
            del old
            return True
        else:
            print "The world is inconsistent, rejecting changes"
            self.status = old
            return False
    
    def validate(self):
        for reprule in self.representationRules:
            if not reprule.verify(self.status):
                print "Validation failed on:",reprule
                return False
        return True
    
    def addTokensFromModule(self, module):
        """
        Scan tokens from the passed module
        """
        for name,obj in module.__dict__.items():
            if isinstance(obj, token) and obj.name is None and obj not in self.tokens.keys():
                print "Registering token",name
                obj.name = name
                self.tokens[name] = obj
    
    def addGenerationRulesFromModule(self, module):
        """
        Scan generation rules from the specified module
        """
        for name,obj in module.__dict__.items():
            if isinstance(obj, category) and obj.header is None and obj not in self.generationRules.keys():
                obj.header = name
                self.generationRules[name] = obj
                
                for el in obj.body:
                    if not isinstance(el, token) or el.name is None or el.name not in self.tokens.keys():
                        raise LangParseException("Invalid token "+str(el))
                
                print "Registering Rule for category",name,"(",len(obj.body),")"
        
    def addRepresentationRulesFromModule(self, module):
        """
        Scan representation rules from the specified module
        """
        for obj in module.__dict__.values():
            if isinstance(obj, rules):
                for rule in obj.rules:
                    self.representationRules.append(rule)
        
        print "Registered",len(self.representationRules),"rules"