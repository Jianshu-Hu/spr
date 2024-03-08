import matplotlib.pyplot as plt
import numpy as np
import math
import os


def average_over_several_runs(folder):
    data_all = []
    min_length = np.inf
    runs = os.listdir(folder)
    for i in range(len(runs)):
        data = np.loadtxt(folder+'/'+runs[i]+'/files/score.csv', delimiter=',', skiprows=1)
        # evaluation_freq = data[2, -3]-data[1, -3]
        evaluation_freq = data[2, 0]-data[1, 0]
        data_all.append(data[:, -3])
        if data.shape[0] < min_length:
            min_length = data.shape[0]
    average = np.zeros([len(runs), min_length])
    for i in range(len(runs)):
        average[i, :] = data_all[i][:min_length]
    mean = np.mean(average, axis=0)
    std = np.std(average, axis=0)

    return mean, std, evaluation_freq


def plot_several_folders(prefix, folders, label_list=[], plot_or_save='save', title=""):
    plt.rcParams["figure.figsize"] = (5, 4)
    fig, axs_plot = plt.subplots(1, 1)
    for i in range(len(folders)):
        folder_name = 'saved_runs/'+prefix+folders[i]
        num_runs = len(os.listdir(folder_name))
        mean, std, eval_freq = average_over_several_runs(folder_name)
        # plot variance
        axs_plot.fill_between(eval_freq/1000*np.arange(len(mean)),
                    mean - std/math.sqrt(num_runs),
                    mean + std/math.sqrt(num_runs), alpha=0.4)
        if len(label_list) == len(folders):
            # specify label
            axs_plot.plot(eval_freq/1000 * np.arange(len(mean)), mean, label=label_list[i])
        else:
            axs_plot.plot(eval_freq/1000 * np.arange(len(mean)), mean, label=folders[i])

        axs_plot.set_xlabel('iterations(x1000)')
        axs_plot.set_ylabel('human normalized score')
        axs_plot.legend(fontsize=10)
        # axs_plot.set_title(eval_env_type[j])
        axs_plot.set_title(title)
    if plot_or_save == 'plot':
        plt.show()
    else:
        plt.savefig('saved_figs/'+title)


prefix = 'pong/'
folders_1 = ['rainbow', 'rainbow_simhash_repeat']
# label_list = ['drqv2', 'ours']
plot_several_folders(prefix, folders_1, title='pong')

prefix = 'alien/'
folders_1 = ['rainbow', 'rainbow_simhash_repeat']
# label_list = ['drqv2', 'ours']
plot_several_folders(prefix, folders_1, title='alien')

prefix = 'battlezone/'
folders_1 = ['rainbow', 'rainbow_simhash_repeat']
# label_list = ['drqv2', 'ours']
plot_several_folders(prefix, folders_1, title='battlezone')
