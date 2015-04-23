import os
import imp


def open_formula(alias):
    f = open(os.getcwd() + "/core/Aliases/" + alias[0], "r")
    formula_name = f.readline()
    module = imp.load_source(formula_name, "core/Formula/" + formula_name + ".py")
    formula = module.Formula(request=alias[1:])
    formula.main()