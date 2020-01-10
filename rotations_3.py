from male_optimal_solution_2 import get_male_optimal, get_shortlists
import networkx as nx
import matplotlib.pyplot as plt
from max_flow import Graph
from copy import deepcopy
import functools
import operator


# Поиск циклов в графе, обход в глубину
def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))


# найти циклы в графе, одна вершина участвует только в одном цикле
def find_cycles(graph):
    vertices = []
    cycles = []
    for node in graph:
        if node in vertices:
            continue
        for path in dfs(graph, node, node):
            vertices = vertices+path
            cycles.append([node]+path)
    return cycles


# получить граф в виде словаря {вершина: дети}
def male_graph(shortlists, couples):
    graph = dict()
    for man, pref in shortlists["Market A"].items():
        if len(pref) > 0:
            try:
                graph[man] = [next(x for x in couples if x[-1] == pref[1])[0]]
            except Exception:
                graph[man] = []
    return graph


# получить ротацию по циклу
def get_rotation(cycle, shortlists):
    return [[man, shortlists["Market A"][man][0]] for man in cycle[:-1]]


# получить все ротации по циклам
def get_rotations(cycles, shortlists):
    return [get_rotation(cycle, shortlists) for cycle in cycles]


# вес ротации
def get_weight(preferences, rotation):
    r = len(rotation)
    return sum([
        preferences["Market A"][rotation[i][0]].index(rotation[i][1]) -
        preferences["Market A"][rotation[i][0]].index(rotation[(i+1) % r][1]) +
        preferences["Market B"][rotation[i][1]].index(rotation[i][0]) -
        preferences["Market B"][rotation[i][1]].index(rotation[(i-1) % r][0])
        for i in range(r)])


def get_weights(preferences, rotations):
    return [get_weight(preferences, rotation) for rotation in rotations]


def rotate(lst):
    return lst[1:] + lst[:1]


def rotate2(lst):
    return lst[-1:] + lst[:-1]


def gcrw(shortlists, couples, preferences):
    graph = male_graph(shortlists, couples)
    cycles = find_cycles(graph)
    rotations = get_rotations(cycles, shortlists)
    weights = get_weights(preferences, rotations)
    return cycles, rotations, weights


# исключить ротации
def eliminate_rotations(couples0, preferences, rotations):
    for_replace = []
    for_eliminate = []
    men_all = []
    rotated_all = []
    women_all = []
    for rotation in rotations:
        men = []
        women = []
        for el in rotation:
            men.append(el[0])
            women.append(el[1])
        men_all.append(men)
        women_all.append(women)
        rotated_all.append(rotate2(men))
        for_eliminate = for_eliminate+men
        for_replace = for_replace+list(map(list, zip(men, rotate(women))))
    couples = list(filter(lambda x: x[0] not in for_eliminate, couples0)) + for_replace
    return men_all, women_all, rotated_all, couples, get_shortlists(couples, preferences)


# заполнение на первой итерации
def fill1(array_men, couples0, preferences, rotations, cycles, weights, shortlists):
    assoc_rotations = {}
    num_of_rotations = len(rotations)
    (men_all, women_all, rotated_all, couples, shortlists1) = eliminate_rotations(couples0, preferences, rotations)
    eliminated_all = []
    for men, women, rotated in zip(men_all, women_all, rotated_all):
        eliminated = {}
        for man in array_men:
            eliminated[man] = []
        for m, w, r in zip(men, women, rotated):
            elim_men = shortlists["Market B"][w][shortlists["Market B"][w].index(r) + 1:
                                                 shortlists["Market B"][w].index(m)]
            for man in elim_men:
                eliminated[man] = eliminated[man] + [w]
        eliminated_all.append(eliminated)

    for i in range(1, num_of_rotations+1):
        assoc_rotations[i] = {
            "cycle": cycles[i - 1],
            "weights": weights[i - 1],
            "predecessors": [],  # непосредственные предки
            "rotation": rotations[i - 1],
            "shortlist": shortlists,  # до исплючения
            "eliminated": eliminated_all[i - 1]
        }
    return couples, shortlists1, 1, num_of_rotations, assoc_rotations


# определение предков
def get_predecessors(cycles, rotations, assoc_rotations, filled0, filled1):
    predecessors = []
    for rotation, cycle in zip(rotations, cycles):
        pred = []
        for i in range(filled0, filled1+1):  # потенциальные предки
            for man in cycle[:-1]:
                pref_list = assoc_rotations[i]["shortlist"]["Market A"][man]
                pos = pref_list.index(rotation[cycle[:-1].index(man)][1])
                if [man, pref_list[pos - 1]] in assoc_rotations[i]["rotation"] or \
                        pref_list[pos + 1] in assoc_rotations[i]["eliminated"][man]:
                    pred.append(i)
                    break
        predecessors.append(pred)
    return predecessors


# заполнение после первой итерации
def fill(couples0, preferences, array_men, rotations, cycles, weights, shortlists, assoc_rotations, filled0, filled1):
    num_of_rotations = len(rotations)
    counter = num_of_rotations+filled1
    predecessors = get_predecessors(cycles, rotations, assoc_rotations, filled0, filled1)
    (men_all, women_all, rotated_all, couples1, shortlists1) = eliminate_rotations(couples0, preferences, rotations)
    eliminated_all = []

    for men, women, rotated in zip(men_all, women_all, rotated_all):
        eliminated = {}
        for man in array_men:
            eliminated[man] = []
        for m, w, r in zip(men, women, rotated):
            elim_men = shortlists["Market B"][w][shortlists["Market B"][w].index(r)+1:
                                                 shortlists["Market B"][w].index(m)]
            for man in elim_men:
                eliminated[man] = eliminated[man] + [w]
        eliminated_all.append(eliminated)

    for i in range(num_of_rotations):
        current_cycle = cycles[i]
        assoc_rotations[i+filled1+1] = {
            "cycle": current_cycle,
            "weights": weights[i],
            "predecessors": predecessors[i],
            "rotation": rotations[i],
            "shortlist": shortlists,
            "eliminated": eliminated_all[i]
        }
    return couples1, shortlists1, filled1+1, counter, assoc_rotations


def find_rotations(male_optimal, preferences, shortlists0):  # если assoc пустой то это единственное решение
    array_men = list(range(1, len(male_optimal) + 1))
    # первый поиск ротаций
    (cycles, rotations, weights) = gcrw(shortlists0, male_optimal, preferences)
    (couples, shortlists, filled0, filled1, assoc_rotations) = fill1(array_men, male_optimal, preferences, rotations,
                                                                     cycles, weights, shortlists0)
    # после первой итерации
    while rotations:
        (cycles, rotations, weights) = gcrw(shortlists, couples, preferences)
        (couples, shortlists, filled0, filled1, assoc_rotations) = fill(couples, shortlists0, array_men, rotations,
                                                                        cycles, weights, shortlists, assoc_rotations,
                                                                        filled0, filled1)
    return assoc_rotations


def get_edges(assoc_rotations):
    edges_list = list()
    labels = dict()
    t = len(assoc_rotations) + 1
    labels[0] = "s"
    labels[t] = "t"
    nodes = list()

    for child, pred in assoc_rotations.items():
        nodes.append(child)
        labels[child] = "p({}),{}".format(child, pred["weights"])
        if pred["weights"] < 0:
            edges_list.append([0, child])
        elif pred["weights"] > 0:
            edges_list.append([child, t])
        for p in pred["predecessors"]:
            edges_list.append([p, child])

    nodes = [0] + nodes + [t]
    return t, labels, nodes, edges_list


def get_matrix(t, nodes, edges_list, assoc_rotations):
    matrix = []
    for node1 in nodes:
        string = []
        for node2 in nodes:
            if node1 == 0 and [node1, node2] in edges_list:
                string.append(abs(assoc_rotations[node2]["weights"]))
            elif node2 == t and [node1, node2] in edges_list:
                string.append(assoc_rotations[node1]["weights"])
            elif [node1, node2] in edges_list:
                string.append(float("Inf"))
            else:
                string.append(0)
        matrix.append(string)
    return matrix


def get_subset(vertex, assoc_rotations):
    result = []
    queue = [vertex]
    while queue:
        vertex = queue[-1]
        result = [vertex] + result
        queue = assoc_rotations[vertex]["predecessors"] + queue
        queue = queue[:-1]
    return result


def get_solution(male_optimal, rotations, assoc_rotations):
    for rotation in rotations:
        men = []
        women = []
        for el in assoc_rotations[rotation]["rotation"]:
            men.append(el[0])
            women.append(el[1])
        male_optimal = list(filter(lambda x: x[0] not in men, male_optimal))+list(map(list, zip(men, rotate(women))))
    return male_optimal


def get_main(preferences):
    male_optimal = get_male_optimal(preferences)
    shortlists0 = get_shortlists(male_optimal, preferences)

    assoc_rotations = find_rotations(male_optimal, preferences, shortlists0)

    if assoc_rotations:
        (t, labels, nodes, edges_list) = get_edges(assoc_rotations)
        matrix = get_matrix(t, nodes, edges_list, assoc_rotations)
        g = Graph(deepcopy(matrix))
        min_cut = g.minCut(0, t)

        vertices = list()
        for p in list(set(nodes[1:-1:])-set(functools.reduce(operator.iconcat, min_cut, []))):
            if assoc_rotations[p]["weights"] > 0:
                vertices.append(p)
        vertices.reverse()

        closed_subset = []
        for vertex in vertices:
            if vertex not in closed_subset:
                closed_subset = closed_subset + get_subset(vertices[0], assoc_rotations)

        solution = get_solution(male_optimal, list(set(closed_subset)), assoc_rotations)

        black_edges = list()
        for edge in edges_list:
            if edge not in min_cut:
                black_edges.append(edge)

        graph = nx.DiGraph()
        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges_list)

        pos = nx.shell_layout(graph)
        nx.draw_networkx_edges(graph, pos=pos, width=2, edgelist=min_cut, edge_color='red', style="dashed",
                               arrows=False, label="минимальный разрез")
        nx.draw_networkx_edges(graph, pos=pos, width=2, edgelist=black_edges, edge_color='#1f78b4')
        nx.draw_networkx_nodes(graph, pos)
        nx.draw_networkx_labels(graph, pos, labels)

        plt.legend()
        plt.title('s-t граф ротаций', fontsize=22)
        return plt, solution
    else:
        plt.legend()
        plt.title('s-t граф ротаций', fontsize=22)
        return plt, male_optimal
