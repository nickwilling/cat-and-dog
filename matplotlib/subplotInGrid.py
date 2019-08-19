import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1:subplot2grid
##################################3
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
#本来是plt.xlabel()现在前面都要加set_
ax1.set_xlabel('this is x')
ax1.set_title('ax1_title')
#从第一行第0列开始
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
ax3 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
ax5 = plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)
#method 2:gridspec:GridSpecification规格
#################################3
plt.figure()
gs = gridspec.GridSpec(3,3)
ax6 = plt.subplot(gs[0,:])
ax7 = plt.subplot(gs[1,:2])
ax8 = plt.subplot(gs[1:,2])
ax9 = plt.subplot(gs[-1,0])
ax10 = plt.subplot(gs[-1,-2])
#method 3:easy to define structure
##################################
#返回值是return fig, axs
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[2,2])
plt.tight_layout()
plt.show()