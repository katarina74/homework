from copy import deepcopy
# Male and Female Optimal Solutions; The Shortlists


# отбираем холостяков из пар
def select_celibates(couples):
    celibates = list()
    for i in couples:
        if i[1] == 0:
            celibates.append(i[0])
    return celibates


# мужчины делают предложения женщинам
# формируем словаь вида женщина:предложения
def get_proposals(celibates, preferences):
    proposals = {}
    for man in celibates:
        woman = preferences["Market A"][man][0]
        if woman in proposals:
            mas = proposals[woman]
            mas.append(man)
            proposals[woman] = mas
        else:
            proposals[woman] = [man]
    return proposals


# выбор женщинами лучших предложений
def take_better_prop(proposals, couples, preferences):
    for woman, men in proposals.items():
        current = None
        for c in couples:
            if c[1] == woman:
                current = c[0]
                break
        if current:
            men.append(current)
        for man in preferences["Market B"][woman]:
            if man in men:
                if man != current:
                    couples[man-1] = [man, woman]
                    if current:
                        couples[current-1] = [current, 0]
                break
    return couples


# мужское оптимальное решение
def get_male_optimal(preferences0):
    preferences = deepcopy(preferences0)
    couples = [[i, 0] for i in range(1, len(preferences["Market A"])+1)]
    celibates = select_celibates(couples)
    while celibates:
        proposals = get_proposals(celibates, preferences)
        couples = take_better_prop(proposals, couples, preferences)
        # удаление первой женщины из списка предпочтений
        for men in celibates:
            preferences["Market A"][men] = preferences["Market A"][men][1:]
        celibates = select_celibates(couples)
    return couples


# выбрать из списка предпочтений агентов не хуже заданного
def take_better(list_of_pref, agent):
    return list_of_pref[:list_of_pref.index(agent)+1]


# выбрать из списка предпочтений агентов не лучше заданного
def take_worse(list_of_pref, agent):
    return list_of_pref[list_of_pref.index(agent):]


def update_preferences(preferences0):
    preferences = deepcopy(preferences0)
    for man, women in preferences["Market A"].items():
        for woman in deepcopy(women):
            if man not in preferences["Market B"][woman]:
                women.remove(woman)
        preferences["Market A"][man] = women
    for woman, men in preferences["Market B"].items():
        for man in deepcopy(men):
            if woman not in preferences["Market A"][man]:
                men.remove(man)
        preferences["Market B"][woman] = men
    return preferences


def get_shortlists(male_optimal, preferences0):
    preferences = deepcopy(preferences0)
    for man, woman in male_optimal:
        preferences["Market A"][man] = take_worse(preferences["Market A"][man], woman)
        preferences["Market B"][woman] = take_better(preferences["Market B"][woman], man)
    return update_preferences(preferences)
