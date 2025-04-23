import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")

g = sns.FacetGrid(anscombe, col="dataset", col_wrap=2, height=4, aspect=1)

g.map_dataframe(sns.scatterplot, x="x", y="y")
g.map_dataframe(sns.lineplot, x="x", y="y", estimator=None, lw=1, color="red", linestyle="--")
g.map_dataframe(sns.regplot, x="x", y="y", scatter=False, ci=None, line_kws={"color":"blue"})

g.set_titles("Dataset {col_name}")
g.set_axis_labels("x", "y")
plt.subplots_adjust(hspace=0.3)
g.fig.suptitle("Anscombe Quartet",y=1.06)


plt.tight_layout()

plt.show()