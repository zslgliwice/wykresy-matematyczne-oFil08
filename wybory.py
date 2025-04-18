import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 8})

with open("dane.txt") as dane:
    nazwy = []
    liczbyGlosow = []

    for linijka in dane:
        label, glosy = linijka.split(";")
        nazwy.append(label)
        liczbyGlosow.append(int(glosy))

    sumGlosow = sum(liczbyGlosow);

    fig, ax = plt.subplots()
    bar_container = ax.bar(nazwy, liczbyGlosow)
    ax.set(ylabel='glosy w milionach')
    ax.set_title('Wybory 2023')
    ax.bar_label(bar_container, fmt=lambda x: f'{int(x)} ({round(x/sumGlosow*100,2)}%)')
    plt.rcParams.update({'font.size': 8})
    plt.show()