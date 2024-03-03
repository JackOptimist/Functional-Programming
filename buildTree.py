from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

def build_decision_tree(data, target):

    clf = DecisionTreeClassifier()

    clf.fit(data, target)

    return clf
iris = load_iris()
data = iris.data
target = iris.target

decision_tree = build_decision_tree(data, target)

tree_structure = export_text(decision_tree, feature_names=iris.feature_names)
print(tree_structure)
