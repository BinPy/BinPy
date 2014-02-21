
import itertools
from QuineMcCluskey import QM
import random
import sys

"""
This class implements a Moore state machine solver. Using the Quine-McCluskey
algorithm it minimizes the necessary next state and output functions for a given
state machine.
"""

class StateMachineSolver:
  def __init__(self, state_tran, state_word_len, variables, outputs):
    """
Initialize the Moore state machine optimizer.

state_tran: a dictionary; key denotes the target state and value is a lambda
expression that evaluates to True when the machine should move to this
target state.
state_word_len: an integer that holds the count of bits used for
representing the state
variables: a list containing the names of the input variables of the machine
outputs: a list containing lambda expressions for calculating the outputs of
the state machine
"""

    self.state_tran = state_tran
    self.state_word_len = state_word_len
    self.outputs = outputs
    self.next_state = self.InternalOptimizer(state_word_len, variables)
    self.output = self.InternalOptimizer(state_word_len, [])

  def solve(self, state_map):
    """
Given a state map return the transition and output functions.

state_map: a dictionary; key is the state and value is the value of the
state word that identifies this state

returns: a tuple a,b,c; a is the sum of the functions' complexities, b is
the next state functions (one for each state word bit) and c is the output
functions
"""

    self.next_state.state_map = state_map
    self.output.state_map = state_map

    state_bit_on = {}
    state_bit_off = {}
    for i in xrange(self.state_word_len):
      state_bit_on[i] = []
      state_bit_off[i] = []
      for k,v in state_map.iteritems():
        if v & (1<<i):
          state_bit_on[i].append(k)
        else:
          state_bit_off[i].append(k)

    total_complexity = 0
    next_state_results = []
    output_results = []
    for i in xrange(self.state_word_len):
      f_on = map(lambda x: self.state_tran[x],state_bit_on[i])
      f_off = map(lambda x: self.state_tran[x],state_bit_off[i])
      complexity,function = self.next_state.solve(f_on, f_off)
      total_complexity += complexity
      next_state_results.append(function)
    for i in xrange(len(self.outputs)):
      complexity,function = self.output.solve([self.outputs[i]])
      total_complexity += complexity
      output_results.append(function)
    return total_complexity,next_state_results,output_results

  def print_solution(self,state_map,solution):
    """ Print a solution. """

    complexity,next_state_funcs,output_funcs = solution

    print 'Complexity = %d' % complexity
    for i in sorted(state_map.keys()):
      print 'State %d = %d' % (i,state_map[i])
    for i in xrange(len(next_state_funcs)):
      f = self.next_state.get_function(next_state_funcs[i])
      print 'S%d = %s' % (i, f)
    for i in xrange(len(output_funcs)):
      f = self.output.get_function(output_funcs[i])
      print 'OUT%d = %s' % (i, f)
    print '-'*80

  """ This class is used internally by the Moore state machine optimizer. """

  class InternalOptimizer:
    def __init__(self, state_word_len, variables):
      """ Initialize the internal helper class. """

      self.state_word_len = state_word_len
      self.variables = variables
      variable_names = map(lambda i:'S%d'%i, xrange(self.state_word_len))
      variable_names += self.variables
      self.qm = QM(variable_names)

    def solve(self, f_on, f_off = None):
      """
Returns a function that satisfies the conditions given.

f_on: a list of lambda expressions; if one of the lambda expressions
evaluates to True then the requested function should evaluate to True
f_off: a list of lambda expressions; if one of them evaluates to True
then the requested function whould evaluate to False

returns: a tuple a,b; a is the complexity of the function and b is the
function
"""

      self.state_env = self.State()
      self.variables_env = self.Variables(self.variables)

      c = self.state_word_len
      d = len(self.variables)
      ones = []
      dc = set(i for i in xrange(1<<(d+c)))
      for variables_word in xrange(1<<d):
        self.variables_env.word = variables_word
        for state,state_word in self.state_map.iteritems():
          self.state_env.state = state
          on = self.evaluate(f_on)
          if f_off == None:
            off = not on
          else:
            off = self.evaluate(f_off)
          assert not (on and off)
          if on:
            ones.append(variables_word<<c|state_word)
            dc.remove(variables_word<<c|state_word)
          elif off:
            dc.remove(variables_word<<c|state_word)

      dc = list(dc)
      return self.qm.solve(ones,dc)

    def evaluate(self, f_array):
      """
Evaluates a list of lambda expressions in the state and variables
environment. The lambda expressions are terms of an OR expression.

f_array: a list of lambda expressions

returns: the logical OR after evaluate the lambda expression in the setup
environment
"""

      for f in f_array:
        if f(self.state_env,self.variables_env):
          return True
      return False

    """
This class provides access to the state word from the lambda expressions.
"""

    class State:
      def __getitem__(self, item):
        return self.state == item

    """
This class provides access to the input variables from the lambda
expressions.
"""

    class Variables:
      def __init__(self, variables):
        self.variables = {}
        for i in xrange(len(variables)):
          self.variables[variables[i]] = 1<<i

      def __getitem__(self, item):
        return bool(self.word & self.variables[item])

    def get_function(self, minterms):
      """ Retrieve a human readable form of the given function. """

      return self.qm.get_function(minterms)

""" This class is the base for creating a Moore state machine optimizer. """

class StateMachineOptimizer:
  def __init__(self, state_tran, state_word_len, variables, outputs, **kwargs):
    """ Initialize the state machine optimizer. """

    self.state_tran = state_tran
    self.state_word_len = state_word_len
    self.sms = StateMachineSolver(state_tran, state_word_len, variables,
      outputs)

    self.print_all = kwargs.get('print_all', False)
    self.print_best = kwargs.get('print_best', False)

  def calc_total(self):
    """
Calculate the total count of possible permutations of state configurations.
"""

    total = 1
    begin = (1<<self.state_word_len)-len(self.state_tran)+1
    end = (1<<self.state_word_len)+1
    for i in xrange(begin,end):
      total *= i
    return total

"""
This class implements a Moore state machine optimizer that tries all possible
permutations for assignment of state word values to states.
"""

class StateMachineOptimizer_AllPermutations(StateMachineOptimizer):
  def optimize(self):
    total = self.calc_total()

    min_complexity = 99999999
    counter = 0
    elements = range(1<<self.state_word_len)
    for permutation in itertools.permutations(elements, len(self.state_tran)):
      counter += 1
      if counter & 0xff == 0:
        sys.stderr.write('%%%3.2f done\r' % (100.0*counter/total))

      state_map = {}
      for i in xrange(len(self.state_tran)):
        state_map[i] = permutation[i]
      solution = self.sms.solve(state_map)
      if self.print_all:
        print '%r' % ((state_map,solution),)

      if solution[0]<min_complexity:
        min_complexity=solution[0]
        if self.print_best:
          self.sms.print_solution(state_map,solution)

"""
This class implements a Moore state machine optimizer that tries permutations at
random.
"""

class StateMachineOptimizer_Random(StateMachineOptimizer):
  def optimize(self, tries = 1000):
    total = self.calc_total()

    min_complexity = 99999999
    for counter in xrange(tries):
      if counter & 0xff == 0:
        sys.stderr.write('Tried %d random permutations out of %d.\r' % (counter,
          total))

      permutation = range(1<<self.state_word_len)
      random.shuffle(permutation)

      state_map = {}
      for i in xrange(len(self.state_tran)):
        state_map[i] = permutation[i]
      solution = self.sms.solve(state_map)
      if self.print_all:
        print '%r' % ((state_map,solution),)

      if solution[0]<min_complexity:
        min_complexity=solution[0]
        if self.print_best:
          self.sms.print_solution(state_map,solution)

"""
This class is used for testing the state machine optimizer.
"""

class StateMachineOptimizer_FileAndVerify(StateMachineOptimizer):
  def optimize(self, file):
    for line in open(file,'r').readlines():
      input,expected_output = eval(line)
      output = self.sms.solve(input)
      assert expected_output == output

def main():
  state_tran = {
    0: lambda s,v: s[5],
    1: lambda s,v: (s[0] and not v['A'])or(s[1] and not v['B']),
    2: lambda s,v: (s[0] and v['A'])or(s[2] and not v['B']),
    3: lambda s,v: s[1] and v['B'],
    4: lambda s,v: s[2] and v['B'],
    5: lambda s,v: s[3] or s[4],
  }

  outputs = [
    lambda s,v: not s[5],
    lambda s,v: s[1] or s[3],
    lambda s,v: s[2] or s[3] or s[4],
  ]

  variables = ['A', 'B']

  state_word_len = 3
  opti = StateMachineOptimizer_Random(state_tran, state_word_len, variables, outputs, print_best = True)
  opti.optimize()

  #state_word_len = 3
  #sms = StateMachineSolver(state_tran, state_word_len, variables, outputs)
  #state_map = {0:0,1:1,2:2,3:3,4:4,5:5}
  #solution = sms.solve(state_map)
  #sms.print_solution(state_map,solution)

  #state_word_len = 3
  #opti = StateMachineOptimizer_AllPermutations(state_tran, state_word_len, variables, outputs, print_best = True)
  #opti.optimize()

  #state_word_len = 4
  #opti = StateMachineOptimizer_Random(state_tran, state_word_len, variables, outputs, print_best = True)
  #opti.optimize(tries = 500)

  #state_word_len = 3
  #opti = StateMachineOptimizer_FileAndVerify(state_tran, state_word_len, variables, outputs)
  #opti.optimize('testdata.txt')

if __name__ == '__main__':
  main()
