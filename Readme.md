# Matplotlib & Seaborn Visualization

Chart-building practice notebooks part of a structured data science sprint.

## Progress

### Matplotlib & Seaborn:
- [x] Introduction to Data Visualization
- [x] Plotting Charts using Matplotlib
- [x] Bar Charts in Matplotlib
- [x] Pie Charts in Matplotlib
- [x] Stack Plots in Matplotlib
- [x] Histograms in Matplotlib
- [x] Scatter Plots in Matplotlib
- [x] Subplots in Matplotlib
- [x] Introduction to Seaborn
- [x] Basic Plot Types in Seaborn

## Notebooks
- `Intro To Matplotlib.ipynb` — plt.plot(), xlabel/ylabel/title, legend(), grid(), format strings ('ro--'), readable format (color, linestyle, marker, ms, linewidth), plt.show()
- `Bar Charts in Matplotlib.ipynb` — plt.bar(), grouped bars with np.arange+width offset, bar labels with plt.text(), color
- `Pie Charts in Matplotlib.ipynb` — plt.pie(), labels, colors, explode, shadow, startangle, autopct='%1.1f%%', wedgeprops, donut charts
- `Stack Plots in Matplotlib.ipynb` — plt.stackplot(), *args for multiple y-values, labels, colors, alpha transparency, legend positioning
- `Histograms in Matplotlib.ipynb` — plt.hist(), bins, edgecolor, plt.axvline() for reference lines, frequency distribution visualization
- `Scatter Plots in Matplotlib.ipynb` — plt.scatter(), size (s=), color (c=), colormap, alpha, correlation visualization
- `Subplots in Matplotlib.ipynb` — plt.subplots(), fig/ax syntax, axes indexing, sharing axes, tight_layout()
- `Seaborn intro.ipynb` — seaborn vs matplotlib, sns.set_theme(), built-in datasets, high-level API
- `Seaborn plots.ipynb` — sns.barplot(), sns.histplot(), sns.scatterplot(), sns.boxplot(), sns.heatmap(), sns.pairplot(), hue parameter for grouping

## Notes
- Format strings ('ro--') are compact but don't allow size control — use readable format (color, linestyle, marker, ms) when customization needed.
- `plt.barh()` for horizontal bars when labels are long; `plt.bar()` for vertical.
- `np.arange()` + `width` offset = standard pattern for grouped bar charts.
- `plt.xticks()` replaces numeric index labels with real category names.
- `plt.tight_layout()` prevents label overlap — use it whenever subplots or long labels are involved.
- Pie charts: avoid when comparing many slices — use bar charts instead. Use `explode` to highlight, `autopct='%1.1f%%'` for percentages, `startangle` to rotate.
- `plt.stackplot(x, y1, y2, y3)` — shows cumulative totals over time; use `alpha` for transparency when colors overlap visually.
- Histograms show frequency distribution of continuous data; `bins` controls granularity, `axvline()` marks reference points like mean/median.
- Scatter plots show correlation between two continuous variables; use `c=` + colormap to add a third dimension.
- Subplots: always use `fig, ax = plt.subplots(rows, cols)` syntax — gives full control over each axis independently.
- Seaborn is built on Matplotlib — use Seaborn for statistical plots with less code, drop to Matplotlib when you need fine-grained control.
- `hue=` parameter adds a categorical grouping dimension to any Seaborn plot without extra code.

## Assignment: Pie vs Bar Chart Comparison
- `Filename` — assignment.py
- Compare mobile OS market share (Android 72%, iOS 27%, Others 1%) using both a pie chart and horizontal bar chart.
- Observation: Bar chart makes size differences clearer at a glance — pie charts struggle when one slice dominates heavily.
