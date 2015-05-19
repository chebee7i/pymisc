import numpy as np

def pubquality(fig_width_pt=246.0, cm=True):
    """
    Configure matplotlib for publication quality PDF output.

    Taken from: http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    Grab the figure width in points from LaTeX using \showthe\columnwidth or
    \showthe\textwidth depending on your intention.

    """
    # Convert pt to inch
    inches_per_pt = 1.0/72.27

    # Aesthetic ratio
    golden_mean = (np.sqrt(5)+1.0)/2.0 - 1

    # Width in inches
    fig_width = fig_width_pt*inches_per_pt
    # Height in inches
    fig_height = fig_width*(golden_mean * 1.2)

    fig_size =  [fig_width, fig_height]
    params = {'backend': 'pdf',
              'axes.titlesize': 10,
              'axes.labelsize': 8,
              'font.size': 8,
              'legend.fontsize': 8,
              'legend.handlelength': 2,
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'figure.subplot.left': 0.15,
              'figure.subplot.bottom': 0.15,
              'figure.figsize': fig_size,
              'pdf.fonttype': 42}

    import matplotlib.pyplot as plt
    plt.rcParams.update(params)

    plt.rcParams['font.sans-serif'].insert(0, 'Computer Modern Sans Serif')
    plt.rcParams['font.serif'].insert(0, 'Computer Modern Roman')
    plt.rcParams['font.monospace'].insert(0, 'Computer Modern Typewriter')
    family = plt.rcParams['font.family']
    try:
        family + []
    except:
        family = ['roman', family]
    else:
        family.insert(0, 'roman')
    plt.rcParams['font.family'] = family

