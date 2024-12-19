# function to create 4-bus system
# initially no inj, no power flows


# create diagram of 4-bus network
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
    axis.annotate(n,xy=(x+0.12,y-0.06), fontsize=8)
    axis.annotate(pu,xy=(x+0.1,y+.1), fontsize=8,color='green')
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
    axis.annotate(n,xy=(x+0.12,y-0.07), fontsize=8)
    axis.annotate(pu,xy=(x-.04,y-.2), fontsize=8,color='red')
    ps = [bar_patch,arrow]
    [axis.add_patch(p) for p in ps]
    return

def create_fig_4bus(fig_pf=None,fig_inj=None):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.path import Path
    if fig_pf == None: 
        fig_pf = {(1,2):None,(1,3):None,(1,4):None,(2,4):None,(3,4):None}
    if fig_inj == None:
        fig_inj = {1:None,2:None,3:None,4:None}
    # transmission lines 
    verts = [(0.4,1.6),(0.4,1.5),(1.65,1.5),(1.65,1.6),
            (1.8,1.6),(1.8,0.3),(1.65,0.3),(1.65,0.4),
            (0.4,0.4),(0.4,0.3), (0.3,0.3),(0.25,0.3),
            (0.25,1.6), (0.32,1.6), (0.32,1.3), (1.75,0.5),
            (1.75,0.3)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO,
             Path.LINETO, Path.LINETO, Path.LINETO, Path.MOVETO,
             Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO,
             Path.LINETO]
    pf_lab_pos = {(1,2):(1,1.55),(1,3):(0.06,1),(1,4):(1,0.95),(2,3):(0,0),(2,4):(1.85,1),(3,4):(1,0.3)}
    tx_lines = patches.PathPatch(Path(verts,codes),facecolor='none')
    # build figure
    fig, ax = plt.subplots()
    add_gen_bus(x=0.3,y=1.7,axis=ax,n=1,pu=fig_inj[1])
    add_gen_bus(x=1.7,y=1.7,axis=ax,n=2, pu=fig_inj[2])
    add_load_bus(x=0.3,y=0.3,axis=ax,n=3,pu=fig_inj[3])
    add_load_bus(x=1.7,y=0.3,axis=ax,n=4,pu=fig_inj[4])
    ax.add_patch(tx_lines)
    for i in fig_pf:
        ax.annotate(fig_pf[i],xy=pf_lab_pos[i],fontsize=8)
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    ax.axis('off')
    plt.show()