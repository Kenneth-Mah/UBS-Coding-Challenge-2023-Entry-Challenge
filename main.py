from typing import Dict, List


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  # Fill in your solution here and return the correct output based on the given input
  classNames = []
  for classDict in classes:
    className = list(classDict.keys())[0]
    classNames.append(className)
  print(classNames)
  
  return {}
