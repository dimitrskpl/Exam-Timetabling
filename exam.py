import csp
import time


if __name__ == '__main__':
    file_name = "Subjects Details.csv"

    #dom_wdeg mac
    p1 = csp.programCSP(file_name)
    print("Running backtracking search with dom_wdeg, lcv, mac...")
    begin = time.time()
    sol = csp.backtracking_search(p1, select_unassigned_variable=csp.dom_wdeg, order_domain_values=csp.lcv, inference=csp.mac)
    end = time.time()
    print("The total time is: ", end-begin)
    print("The total assignments are: ", p1.nassigns)
    print("The total checks are ", p1.checks)
    print()
    # p1.display(sol)

    #dom_wdeg forward_checking
    p2 = csp.programCSP(file_name)
    print("Running backtracking search with dom_wdeg, lcv, forward_checking...")
    begin = time.time()
    sol = csp.backtracking_search(p2, select_unassigned_variable=csp.dom_wdeg, order_domain_values=csp.lcv, inference=csp.forward_checking)
    end = time.time()
    print("The total time is: ", end-begin)
    print("The total assignments are: ", p2.nassigns)
    print("The total checks are ", p2.checks)
    print()
    # p2.display(sol)

    #mrv mac
    p3 = csp.programCSP(file_name)
    print("Running backtracking search with mrv, lcv, mac...")
    begin = time.time()
    sol = csp.backtracking_search(p3, select_unassigned_variable=csp.mrv, order_domain_values=csp.lcv, inference=csp.mac)
    end = time.time()
    print("The total time is: ", end-begin)
    print("The total assignments are: ", p3.nassigns)
    print("The total checks are ", p3.checks)
    print()
    # p3.display(sol)

    #mrv forward_checking
    p4 = csp.programCSP(file_name)
    print("Running backtracking search with mrv, lcv, forward_checking...")
    begin = time.time()
    sol = csp.backtracking_search(p4, select_unassigned_variable=csp.mrv, order_domain_values=csp.lcv, inference=csp.forward_checking)
    end = time.time()
    print("The total time is: ", end-begin)
    print("The total assignments are: ", p4.nassigns)
    print("The total checks are ", p4.checks)
    print()
    # p4.display(sol)

    #min conflicts
    p5 = csp.programCSP(file_name)
    print("Running min_conflicts...")
    begin = time.time()
    sol = csp.min_conflicts(p5)
    end = time.time()
    print("The total time is: ", end-begin)
    print("The total assignments are: ", p5.nassigns)
    print("The total checks are ", p5.checks)
    # p5.display(sol)