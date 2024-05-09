import matplotlib.pyplot as plt
import numpy as np
import math
import os


def average_over_one_episode(prob):
    num_episode = int(prob.shape[0]/1000)
    mean = []
    for i in range(num_episode):
        mean.append(np.mean(prob[i*1000:(i+1)*1000]))
    return np.array(mean)


def plot_repeat_prob(game, folders, title, plot_or_save='save'):
    # plot
    plt.rcParams["figure.figsize"] = (6, 5)
    # plt.rcParams["figure.figsize"] = (15, 12)
    fig, axs = plt.subplots(1, 1)
    # load
    for i in range(len(folders)):
        folder = 'saved_runs/'+game+'/'+folders[i]+'/'
        files = os.listdir(folder)
        prob = np.load(folder+files[0]+'/files/repeat_prob.npz')['repeat_prob']
        prob = np.clip(prob, 0, 1)
        prob = average_over_one_episode(prob)

        axs.plot(np.arange(prob.shape[0]), prob, label=folders[i])
        axs.set_xlabel('x1000 steps')
        axs.set_ylabel('stats')
        axs.legend(fontsize=10)
    axs.set_title(title)
    if plot_or_save == 'plot':
        plt.show()
    else:
        plt.savefig('saved_figs/repeat_prob/' + title)


# game = 'pong'
# folders = ['spr_simhash_repeat_c1', 'spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
# plot_repeat_prob(game, folders, title='pong_spr')
#
# folders = ['spr_epsilon_simhash_repeat_c05', 'spr_epsilon_simhash_repeat_c01',
#            'spr_epsilon_repeat_type_2_simhash_repeat_c1',
#            'spr_epsilon_repeat_type_2_simhash_repeat_c05',
#            'spr_epsilon_repeat_type_2_simhash_repeat_c01']
# plot_repeat_prob(game, folders, title='pong_spr_epsilon')

game = 'alien'
folders = ['spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
plot_repeat_prob(game, folders, title='alien_spr')
game = 'battle_zone'
folders = ['spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
plot_repeat_prob(game, folders, title='battle_zone_spr')

game = 'alien'
folders = ['spr_frame_skip_2_simhash_repeat_c1', 'spr_frame_skip_2_simhash_repeat_c05']
plot_repeat_prob(game, folders, title='alien_spr_frame_skip_2')
