import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy
from scipy import signal
import sys

matplotlib.use("pgf")
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "font.size": 6,
    "legend.fontsize": 5,
    "ytick.labelsize": 4,
    "text.usetex": True,
    "pgf.rcfonts": False
});

env = sys.argv[1]

plt.figure(figsize=(2.65, 1.5))
data_path = "./"

envs = ['kaz', 'pistonball', 'pong', 'prison']
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
i = envs.index(env) 

#for i, env in enumerate(envs):
df = pd.read_csv(os.path.join(data_path+env, 'progress.csv'))
df = df[['episodes_total', "episode_reward_mean"]]
data = df.to_numpy()
filtered = data[:,1]
#filtered = scipy.signal.savgol_filter(data[:, 1], int(len(data[:, 1])/30)+1, 5)
plt.plot(data[:, 0], filtered, label=env.capitalize(), linewidth=0.6, color=colors[i], linestyle='-')

plt.xlabel('Episode', labelpad=1)
plt.ylabel('Average Total Reward', labelpad=1)
#plt.title('Multiwalker')
plt.xticks(ticks=[10000,20000,30000,40000],labels=['10k','20k','30k','40k'])
plt.xlim(0, 50000)
#plt.yticks(ticks=[-150,-100,-50,0],labels=['-150','-100','-50','0'])
#plt.ylim(-200, 50)
plt.tight_layout()
#plt.legend(loc='lower center', ncol=1, labelspacing=.2, columnspacing=.25, borderpad=.25)
plt.margins(x=0)
plt.savefig("butterfly_{}.pgf".format(env), bbox_inches = 'tight',pad_inches = .025)
plt.savefig("butterfly_{}.png".format(env), bbox_inches = 'tight',pad_inches = .025, dpi=600)
