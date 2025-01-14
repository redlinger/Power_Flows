# function to create 3-bus system
# initially no inj, no power flows

# create diagram of 3-bus network
# function to add generator bus
def add_gen_bus(x,y,axis,n,pu):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.path import Path
    circle = patches.Circle((x,y+.08),0.08,fill=False)
    line = Path([(x,y),(x,y-0.09)],[Path.MOVETO, Path.LINETO])
    line_patch = patches.PathPatch(line,facecolor='black',lw=2)
    bar = Path([(x-0.12,y-0.11),(x+0.17,y-0.11)],[Path.MOVETO, Path.LINETO])
    bar_patch = patches.PathPatch(bar,facecolor='black',lw=4)
    axis.annotate('G',xy=(x-0.02,y+0.06), fontsize=8)
    axis.annotate(n,xy=(x+0.12,y-0.06), fontsize=10)
    axis.annotate(pu,xy=(x+0.1,y+.1), fontsize=10,color='black')
    ps = [circle,line_patch,bar_patch]
    [axis.add_patch(p) for p in ps]
    return
# function to add load bus
def add_load_bus(x,y,axis,n,pu):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.path import Path
    bar = Path([(x-0.12,y),(x+0.17,y)],[Path.MOVETO, Path.LINETO])
    bar_patch = patches.PathPatch(bar,facecolor='black',lw=4)
    arrow = patches.Arrow(x+0.025,y,0,-0.15, width=0.04,color='black')
    axis.annotate(n,xy=(x+0.12,y-0.07), fontsize=10)
    axis.annotate(pu,xy=(x-.04,y-.2), fontsize=10,color='black')
    ps = [bar_patch,arrow]
    [axis.add_patch(p) for p in ps]
    return

def create_fig_3bus(s):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.path import Path
    # transmission lines 
    verts = [(0.4,1.6),(0.4,1.5),(1.65,1.5),(1.65,1.6),
            (0.25,1.6), (0.25,1.3), (0.95,1),(0.95,0.8),
            (1.8,1.6), (1.8,1.3), (1.1,1),(1.1,0.8)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
    tx_lines = patches.PathPatch(Path(verts,codes),facecolor='none')
    tx_labels = ['A','B','C']
    tx_lab_pos = [(1,1.55),(0.6,1.17),(1.35,1.17)]
    # build figure
    fig, ax = plt.subplots()
    add_gen_bus(x=0.3,y=1.7,axis=ax,n=1,pu=s[0])
    add_gen_bus(x=1.7,y=1.7,axis=ax,n=2, pu=s[1])
    add_load_bus(x=1,y=0.8,axis=ax,n=3,pu=s[2])
    ax.add_patch(tx_lines)
    for i,lab in enumerate(tx_labels): ax.annotate(lab,xy=tx_lab_pos[i])
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    ax.axis('off')
    plt.show()