import matplotlib.pyplot as plt
import numpy as np
import math
import os

atari_human_scores = dict(
    alien=7127.7, amidar=1719.5, assault=742.0, asterix=8503.3,
    bank_heist=753.1, battle_zone=37187.5, boxing=12.1,
    breakout=30.5, chopper_command=7387.8, crazy_climber=35829.4,
    demon_attack=1971.0, freeway=29.6, frostbite=4334.7,
    gopher=2412.5, hero=30826.4, jamesbond=302.8, kangaroo=3035.0,
    krull=2665.5, kung_fu_master=22736.3, ms_pacman=6951.6, pong=14.6,
    private_eye=69571.3, qbert=13455.0, road_runner=7845.0,
    seaquest=42054.7, up_n_down=11693.2
)

atari_der_scores = dict(
    alien=739.9, amidar=188.6, assault=431.2, asterix=470.8,
    bank_heist=51.0, battle_zone=10124.6, boxing=0.2,
    breakout=1.9, chopper_command=861.8, crazy_climber=16185.3,
    demon_attack=508, freeway=27.9, frostbite=866.8,
    gopher=349.5, hero=6857.0, jamesbond=301.6,
    kangaroo=779.3, krull=2851.5, kung_fu_master=14346.1,
    ms_pacman=1204.1, pong=-19.3, private_eye=97.8, qbert=1152.9,
    road_runner=9600.0, seaquest=354.1, up_n_down=2877.4,
)

atari_nature_scores = dict(
    alien=3069, amidar=739.5, assault=3359,
    asterix=6012, bank_heist=429.7, battle_zone=26300.,
    boxing=71.8, breakout=401.2, chopper_command=6687.,
    crazy_climber=114103, demon_attack=9711., freeway=30.3,
    frostbite=328.3, gopher=8520., hero=19950., jamesbond=576.7,
    kangaroo=6740., krull=3805., kung_fu_master=23270.,
    ms_pacman=2311., pong=18.9, private_eye=1788.,
    qbert=10596., road_runner=18257., seaquest=5286., up_n_down=8456.
)

atari_random_scores = dict(
    alien=227.8, amidar=5.8, assault=222.4,
    asterix=210.0, bank_heist=14.2, battle_zone=2360.0,
    boxing=0.1, breakout=1.7, chopper_command=811.0,
    crazy_climber=10780.5, demon_attack=152.1, freeway=0.0,
    frostbite=65.2, gopher=257.6, hero=1027.0, jamesbond=29.0,
    kangaroo=52.0, krull=1598.0, kung_fu_master=258.5,
    ms_pacman=307.3, pong=-20.7, private_eye=24.9,
    qbert=163.9, road_runner=11.5, seaquest=68.4, up_n_down=533.4
)


def average_over_several_runs(folder, game):
    data_all = []
    min_length = np.inf
    runs = os.listdir(folder)
    for i in range(len(runs)):
        data = np.loadtxt(folder+'/'+runs[i]+'/files/score.csv', delimiter=',', skiprows=1)
        # evaluation_freq = data[2, -3]-data[1, -3]
        evaluation_freq = data[2, 0]-data[1, 0]
        # data_all.append(data[:, 1]*(atari_human_scores[game]-atari_random_scores[game])+atari_random_scores[game])
        data_all.append(data[:, -1])
        if data.shape[0] < min_length:
            min_length = data.shape[0]
    average = np.zeros([len(runs), min_length])
    for i in range(len(runs)):
        average[i, :] = data_all[i][:min_length]
    mean = np.mean(average, axis=0)
    std = np.std(average, axis=0)

    return mean, std, evaluation_freq


def plot_several_folders(prefix, folders, label_list=[], plot_or_save='save', title=""):
    # plt.rcParams["figure.figsize"] = (5, 4)
    plt.rcParams["figure.figsize"] = (10, 8)
    fig, axs_plot = plt.subplots(1, 1)
    print(title)
    for i in range(len(folders)):
        folder_name = 'saved_runs/'+prefix+'/'+folders[i]
        num_runs = len(os.listdir(folder_name))
        mean, std, eval_freq = average_over_several_runs(folder_name, prefix)
        print(folders[i]+': '+str(mean[-1]))
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


# 5.2
prefix = 'amidar'
folders_1 = ['spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_01']
plot_several_folders(prefix, folders_1, title=prefix+'_spr')

prefix = 'ms_pacman'
folders_1 = ['spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_01']
plot_several_folders(prefix, folders_1, title=prefix+'_spr')

prefix = 'pong'
folders_1 = ['spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_01']
plot_several_folders(prefix, folders_1, title=prefix+'_spr')

prefix = 'bank_heist'
folders_1 = ['spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_01']
plot_several_folders(prefix, folders_1, title=prefix+'_spr')

prefix = 'demon_attack'
folders_1 = ['spr_auto_et', 'spr_auto_shift_et',
             'spr_auto_shift_et_normalize_moving_avg_c_sqrt2',
             'spr_auto_shift_et_normalize_moving_avg_c_sqrt2_2',
             'spr_auto_shift_et_default_para_normalize_moving_avg_c_sqrt2',
             'spr_auto_shift_et_default_para_normalize_moving_avg_c_sqrt2_2',
             'spr_auto_shift_et_default_para_normalize_running_max_c_sqrt2_2',
             'spr_auto_shift_et_default_para_normalize_running_max_c_01',
             'spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_01']
plot_several_folders(prefix, folders_1, title=prefix+'_spr_auto')

# prefix = 'kangaroo'
# folders_1 = ['spr_auto_shift_et_default_para_normalize_moving_avg_c_sqrt2_2',
#              'spr_auto_shift_et_default_para_normalize_running_max_c_01',
#              'spr_auto_et_shift_et_default_para_normalize_moving_avg_c_sqrt2_2',
#              'spr_auto_et_shift_et_default_para_normalize_running_max_c_01']
# plot_several_folders(prefix, folders_1, title=prefix+'_spr_auto')

prefix = 'kangaroo'
folders_1 = ['et_21_32_1', 'et_17_48_1.2', 'shift_et_21_32_1', 'shift_et_17_48_1.2']
plot_several_folders(prefix, folders_1, title=prefix+'_spr')

prefix = 'kangaroo'
folders_1 = ['spr_auto_shift_et_normalize_running_max_c_1',
             'spr_auto_shift_et_normalize_running_max_c_05',
             'spr_auto_shift_et_normalize_running_max_c_01',
             'spr_auto_shift_et_default_para_normalize_moving_avg_c_sqrt2_2',
             'spr_auto_shift_et_default_para_normalize_running_max_c_1',
             'spr_auto_shift_et_default_para_normalize_running_max_c_05',
             'spr_auto_shift_et_default_para_normalize_running_max_c_01',
             'spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_1',
             'spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_05',
             'spr_auto_shift_et_default_para_ker_21_6_normalize_running_max_c_01']
plot_several_folders(prefix, folders_1, title=prefix+'_spr_auto')

# 4.25
# prefix = 'alien'
# folders_1 = ['spr_frame_skip_2', 'spr_frame_skip_2_simhash_repeat_c1', 'spr_frame_skip_2_simhash_repeat_c05']
# plot_several_folders(prefix, folders_1, title='alien_frame_skip_2')
#
# prefix = 'roadrunner'
# folders_1 = ['spr_frame_skip_2', 'spr_frame_skip_2_simhash_repeat_c1', 'spr_frame_skip_2_simhash_repeat_c05']
# plot_several_folders(prefix, folders_1, title='roadrunner_frame_skip_2')

# 3.14
# prefix = 'pong'
# folders_1 = ['rainbow', 'rainbow_simhash_repeat_c1', 'rainbow_simhash_repeat_c05', 'rainbow_simhash_repeat_c01']
# plot_several_folders(prefix, folders_1, title='pong_rainbow_simhash')
#
# prefix = 'pong'
# folders_1 = ['spr', 'spr_simhash_repeat_c1', 'spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
# plot_several_folders(prefix, folders_1, title='pong_spr_simhash')
#
# prefix = 'alien'
# folders_1 = ['rainbow', 'rainbow_simhash_repeat_c05', 'rainbow_simhash_repeat_c01']
# plot_several_folders(prefix, folders_1, title='alien_rainbow_simhash')
#
# prefix = 'alien'
# folders_1 = ['spr', 'spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
# plot_several_folders(prefix, folders_1, title='alien_spr_simhash')
#
# prefix = 'battle_zone'
# folders_1 = ['spr', 'spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
# plot_several_folders(prefix, folders_1, title='battlezone_spr_simhash')
#
# prefix = 'pong'
# folders_1 = ['spr_epsilon', 'spr_epsilon_simhash_repeat_c05', 'spr_epsilon_simhash_repeat_c01',
#              'spr_epsilon_repeat_type_2_simhash_repeat_c1',
#              'spr_epsilon_repeat_type_2_simhash_repeat_c05',
#              'spr_epsilon_repeat_type_2_simhash_repeat_c01',
#              'spr_epsilon_zeta_2']
# plot_several_folders(prefix, folders_1, title='pong_epsilon')
#
# prefix = 'breakout'
# folders_1 = ['spr', 'spr_simhash_repeat_c05', 'spr_simhash_repeat_c01']
# plot_several_folders(prefix, folders_1, title='breakout_spr_simhash')
